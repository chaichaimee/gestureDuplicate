# CleanConfig.py
# Part of NVDA Add-on Development (Chai Rules 2026)

import wx
import gui
import config
import ui
import addonHandler
from logHandler import log

addonHandler.initTranslation()

class CleanConfigDialog(wx.Dialog):
	def __init__(self, parent):
		# STAY_ON_TOP ensured. Added close event binding.
		super().__init__(parent, title=_("Clean NVDA.ini Sections"), size=(600, 700), 
						style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER | wx.STAY_ON_TOP)
		
		self.sections = []
		self._setup_ui()
		self._load_sections()
		
		# Bind Escape key and window close X button
		self.Bind(wx.EVT_CLOSE, self.onClose)
		self.Raise()

	def _setup_ui(self):
		main_sizer = wx.BoxSizer(wx.VERTICAL)
		
		info_text = wx.StaticText(self, label=_("Check sections to remove. Press Space to toggle, Delete to remove."))
		main_sizer.Add(info_text, 0, wx.ALL, 10)

		self.checkList = wx.CheckListBox(self)
		self.checkList.Bind(wx.EVT_KEY_DOWN, self.onKeyDown)
		self.checkList.Bind(wx.EVT_CHECKLISTBOX, self.onCheckToggle)
		main_sizer.Add(self.checkList, 1, wx.ALL | wx.EXPAND, 10)

		btn_sizer = wx.BoxSizer(wx.HORIZONTAL)
		
		self.delBtn = wx.Button(self, label=_("Remove Selected"))
		self.delBtn.Bind(wx.EVT_BUTTON, lambda e: self.confirm_and_delete())
		
		# Set ID as wx.ID_CANCEL to automatically handle Escape key
		self.closeBtn = wx.Button(self, wx.ID_CANCEL, label=_("Close"))
		self.closeBtn.Bind(wx.EVT_BUTTON, self.onClose)

		btn_sizer.Add(self.delBtn, 0, wx.RIGHT, 10)
		btn_sizer.Add(self.closeBtn, 0)
		main_sizer.Add(btn_sizer, 0, wx.ALIGN_RIGHT | wx.ALL, 10)
		
		self.SetSizer(main_sizer)

	def _load_sections(self):
		self.checkList.Clear()
		try:
			conf = config.conf.profiles[0]
			self.sections = sorted([str(k) for k in conf.keys()])
			self.checkList.AppendItems(self.sections)
		except Exception as e:
			log.error(f"Error loading config: {e}")

	def onCheckToggle(self, event):
		index = event.GetSelection()
		name = self.checkList.GetString(index)
		status = _("checked") if self.checkList.IsChecked(index) else _("not checked")
		ui.message(f"{name} {status}")

	def onKeyDown(self, event):
		key = event.GetKeyCode()
		if key == wx.WXK_DELETE:
			self.confirm_and_delete()
		else:
			event.Skip()

	def onClose(self, event):
		"""Properly destroy the dialog to free memory and return focus."""
		self.Destroy()

	def confirm_and_delete(self):
		indices = self.checkList.GetCheckedItems()
		if not indices:
			ui.message(_("No items selected."))
			return

		selected = [self.checkList.GetString(i) for i in indices]
		msg = _("Delete {count} sections?").format(count=len(selected))
		
		if gui.messageBox(msg, _("Confirm"), wx.YES_NO | wx.ICON_WARNING) == wx.YES:
			conf = config.conf.profiles[0]
			for name in selected:
				if name in conf:
					del conf[name]
			config.conf.save()
			ui.message(_("Removed successfully."))
			self._load_sections()