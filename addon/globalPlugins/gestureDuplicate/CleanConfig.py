# CleanConfig.py

# Part of NVDA Add-on Development (Chai Rules 2026)

import wx
import gui
import config
import ui
import addonHandler
from logHandler import log

addonHandler.initTranslation()

_VALUE_PREVIEW_MAX = 40


def _truncate(text, limit=_VALUE_PREVIEW_MAX):
	text = str(text).replace("\r", " ").replace("\n", " ")
	if len(text) <= limit:
		return text
	return text[:limit] + "..."


def _isSection(node):
	return isinstance(node, dict)


def _resolveNode(root, path):
	node = root
	for key in path:
		if not _isSection(node) or key not in node:
			return None
		node = node[key]
	return node if _isSection(node) else None


def _countEntries(section):
	subCount = sum(1 for key in section.keys() if _isSection(section[key]) and len(section[key]))
	emptyCount = sum(1 for key in section.keys() if _isSection(section[key]) and not len(section[key]))
	return subCount, len(section) - subCount - emptyCount


def _describeSection(name, section):
	subCount, settingCount = _countEntries(section)
	if not subCount and not settingCount:
		return name
	return _("{name} ({subs} subsections, {settings} settings)").format(
		name=name, subs=subCount, settings=settingCount
	)


class CleanConfigDialog(wx.Dialog):
	def __init__(self, parent):
		# STAY_ON_TOP ensured. Added close event binding.
		super().__init__(parent, title=_("Clean NVDA.ini Sections"), size=(600, 700), 
						style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER | wx.STAY_ON_TOP)
		
		self.sections = []
		self._removedSections = set()
		self._setup_ui()
		self._load_sections()
		
		# Bind Escape key and window close X button
		self.Bind(wx.EVT_CLOSE, self.onClose)
		self.Raise()

	def _setup_ui(self):
		main_sizer = wx.BoxSizer(wx.VERTICAL)
		
		info_text = wx.StaticText(self, label=_("Check sections to remove. Press Space to toggle, Delete to remove, Enter to choose individual items inside a section."))
		main_sizer.Add(info_text, 0, wx.ALL, 10)

		self.checkList = wx.CheckListBox(self)
		self.checkList.Bind(wx.EVT_KEY_DOWN, self.onKeyDown)
		self.checkList.Bind(wx.EVT_CHECKLISTBOX, self.onCheckToggle)
		main_sizer.Add(self.checkList, 1, wx.ALL | wx.EXPAND, 10)

		btn_sizer = wx.BoxSizer(wx.HORIZONTAL)
		
		self.detailsBtn = wx.Button(self, label=_("Details..."))
		self.detailsBtn.Bind(wx.EVT_BUTTON, lambda e: self.openDetails())

		self.delBtn = wx.Button(self, label=_("Remove Selected"))
		self.delBtn.Bind(wx.EVT_BUTTON, lambda e: self.confirm_and_delete())
		
		# Set ID as wx.ID_CANCEL to automatically handle Escape key
		self.closeBtn = wx.Button(self, wx.ID_CANCEL, label=_("Close"))
		self.closeBtn.Bind(wx.EVT_BUTTON, self.onClose)

		btn_sizer.Add(self.detailsBtn, 0, wx.RIGHT, 10)
		btn_sizer.Add(self.delBtn, 0, wx.RIGHT, 10)
		btn_sizer.Add(self.closeBtn, 0)
		main_sizer.Add(btn_sizer, 0, wx.ALIGN_RIGHT | wx.ALL, 10)
		
		self.SetSizer(main_sizer)

	def _load_sections(self, keepIndex=None):
		self.checkList.Clear()
		try:
			conf = config.conf.profiles[0]
			# Sections purged this session are kept out of the list even if
			# NVDA's config validation regenerates an empty default stub for
			# them, since that stub still carries no real settings.
			self.sections = sorted(
				str(k) for k in conf.keys()
				if str(k) not in self._removedSections
			)
			labels = []
			for name in self.sections:
				node = conf[name]
				labels.append(_describeSection(name, node) if _isSection(node) else name)
			self.checkList.AppendItems(labels)
			if keepIndex is not None and self.sections:
				self.checkList.SetSelection(min(keepIndex, len(self.sections) - 1))
		except Exception as e:
			log.error(f"Error loading config: {e}")

	def onCheckToggle(self, event):
		index = event.GetSelection()
		name = self.sections[index]
		status = _("checked") if self.checkList.IsChecked(index) else _("not checked")
		ui.message(f"{name} {status}")

	def onKeyDown(self, event):
		key = event.GetKeyCode()
		if key == wx.WXK_DELETE:
			self.confirm_and_delete()
		elif key in (wx.WXK_RETURN, wx.WXK_NUMPAD_ENTER):
			self.openDetails()
		else:
			event.Skip()

	def onClose(self, event):
		"""Properly destroy the dialog to free memory and return focus."""
		self.Destroy()

	def openDetails(self):
		index = self.checkList.GetSelection()
		if index == wx.NOT_FOUND:
			ui.message(_("No item focused."))
			return
		name = self.sections[index]
		node = _resolveNode(config.conf.profiles[0], (name,))
		if node is None or not len(node):
			ui.message(_("This section has no items to choose from."))
			return
		SectionDetailsDialog(self, (name,), onClosed=self._onDetailsClosed).Show()

	def _onDetailsClosed(self):
		if not self:
			return
		self._load_sections(keepIndex=self.checkList.GetSelection())
		self.checkList.SetFocus()

	def _purge_section(self, conf, name):
		"""Remove both the stored values and the schema entry for a section.
		Deleting only the values leaves the section name defined in the
		config's own validation spec, which recreates an empty stub for it
		the next time NVDA validates the profile, making the name reappear
		even though every setting under it is gone."""
		if name in conf:
			del conf[name]
		configSpec = getattr(conf, 'configspec', None)
		if configSpec is not None and name in configSpec:
			try:
				del configSpec[name]
			except Exception as e:
				log.debug(f"Could not remove configspec entry for {name}: {e}")

	def confirm_and_delete(self):
		indices = self.checkList.GetCheckedItems()
		if not indices:
			ui.message(_("No items selected."))
			return

		selected = [self.sections[i] for i in indices]
		msg = _("Delete {count} sections?").format(count=len(selected))
		
		if gui.messageBox(msg, _("Confirm"), wx.YES_NO | wx.ICON_WARNING) == wx.YES:
			conf = config.conf.profiles[0]
			for name in selected:
				self._purge_section(conf, name)
				self._removedSections.add(name)
			config.conf.save()
			ui.message(_("Removed successfully."))
			self._load_sections()


class SectionDetailsDialog(wx.Dialog):
	"""Selective cleaning of the entries inside one section (or subsection)."""

	def __init__(self, parent, path, onClosed=None):
		self._path = tuple(path)
		self._onClosed = onClosed
		self.entryNames = []
		super().__init__(
			parent,
			title=_("Clean NVDA.ini: {path}").format(path=" > ".join(self._path)),
			size=(600, 700),
			style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER | wx.STAY_ON_TOP
		)
		self._setup_ui()
		self._load_entries()
		self.Bind(wx.EVT_CLOSE, self.onClose)
		self.Raise()

	def _setup_ui(self):
		main_sizer = wx.BoxSizer(wx.VERTICAL)

		info_text = wx.StaticText(
			self,
			label=_("Check items to remove; unchecked items are kept. Press Space to toggle, Delete to remove, Enter to open a subsection.")
		)
		main_sizer.Add(info_text, 0, wx.ALL, 10)

		self.checkList = wx.CheckListBox(self)
		self.checkList.Bind(wx.EVT_KEY_DOWN, self.onKeyDown)
		self.checkList.Bind(wx.EVT_CHECKLISTBOX, self.onCheckToggle)
		main_sizer.Add(self.checkList, 1, wx.ALL | wx.EXPAND, 10)

		btn_sizer = wx.BoxSizer(wx.HORIZONTAL)

		self.detailsBtn = wx.Button(self, label=_("Details..."))
		self.detailsBtn.Bind(wx.EVT_BUTTON, lambda e: self.openDetails())

		self.delBtn = wx.Button(self, label=_("Remove Selected"))
		self.delBtn.Bind(wx.EVT_BUTTON, lambda e: self.confirm_and_delete())

		self.closeBtn = wx.Button(self, wx.ID_CANCEL, label=_("Close"))
		self.closeBtn.Bind(wx.EVT_BUTTON, self.onClose)

		btn_sizer.Add(self.detailsBtn, 0, wx.RIGHT, 10)
		btn_sizer.Add(self.delBtn, 0, wx.RIGHT, 10)
		btn_sizer.Add(self.closeBtn, 0)
		main_sizer.Add(btn_sizer, 0, wx.ALIGN_RIGHT | wx.ALL, 10)

		self.SetSizer(main_sizer)

	def _load_entries(self, keepIndex=None):
		self.checkList.Clear()
		self.entryNames = []
		section = _resolveNode(config.conf.profiles[0], self._path)
		if section is None:
			ui.message(_("This section no longer exists."))
			return
		subsections = []
		settings = []
		for key in section.keys():
			value = section[key]
			if _isSection(value):
				# Empty subsections are validation stubs with nothing to clean.
				if len(value):
					subsections.append(str(key))
			else:
				settings.append(str(key))
		labels = []
		for name in sorted(subsections):
			self.entryNames.append(name)
			labels.append(_describeSection(name, section[name]))
		for name in sorted(settings):
			self.entryNames.append(name)
			labels.append(f"{name} = {_truncate(section[name])}")
		self.checkList.AppendItems(labels)
		if keepIndex is not None and self.entryNames:
			self.checkList.SetSelection(min(keepIndex, len(self.entryNames) - 1))

	def onCheckToggle(self, event):
		index = event.GetSelection()
		name = self.entryNames[index]
		status = _("checked") if self.checkList.IsChecked(index) else _("not checked")
		ui.message(f"{name} {status}")

	def onKeyDown(self, event):
		key = event.GetKeyCode()
		if key == wx.WXK_DELETE:
			self.confirm_and_delete()
		elif key in (wx.WXK_RETURN, wx.WXK_NUMPAD_ENTER):
			self.openDetails()
		else:
			event.Skip()

	def onClose(self, event):
		onClosed = self._onClosed
		self._onClosed = None
		self.Destroy()
		if onClosed:
			onClosed()

	def openDetails(self):
		index = self.checkList.GetSelection()
		if index == wx.NOT_FOUND:
			ui.message(_("No item focused."))
			return
		name = self.entryNames[index]
		section = _resolveNode(config.conf.profiles[0], self._path)
		child = section.get(name) if section is not None else None
		if not _isSection(child):
			ui.message(_("This item has no subsections."))
			return
		SectionDetailsDialog(self, self._path + (name,), onClosed=self._onChildClosed).Show()

	def _onChildClosed(self):
		if not self:
			return
		self._load_entries(keepIndex=self.checkList.GetSelection())
		self.checkList.SetFocus()

	def confirm_and_delete(self):
		indices = self.checkList.GetCheckedItems()
		if not indices:
			ui.message(_("No items selected."))
			return

		selected = [self.entryNames[i] for i in indices]
		msg = _("Delete {count} items from {path}? Removed settings return to their default values.").format(
			count=len(selected), path=" > ".join(self._path)
		)
		if gui.messageBox(msg, _("Confirm"), wx.YES_NO | wx.ICON_WARNING) != wx.YES:
			return

		section = _resolveNode(config.conf.profiles[0], self._path)
		if section is None:
			ui.message(_("This section no longer exists."))
			return
		# Only stored values are removed here. The validation spec is left
		# untouched so NVDA can still resolve defaults for these keys.
		for name in selected:
			if name in section:
				del section[name]
		config.conf.save()
		ui.message(_("Removed successfully."))
		self._load_entries(keepIndex=self.checkList.GetSelection())
