# mygesturesManagement.py

import wx
import os
import globalVars
import gui
import ui
from logHandler import log
import inputCore
import addonHandler
from typing import List, Dict, Set

try:
	addonHandler.initTranslation()
except addonHandler.AddonError:
	log.warning("Unable to init translations.")

class MyGesturesManagementDialog(wx.Dialog):
	"""Dialog to manage custom user gestures for addons only."""

	def __init__(self, parent):
		# Add STAY_ON_TOP style
		super().__init__(parent, title=_("My Gestures Management"), size=(850, 600),
		                 style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER | wx.STAY_ON_TOP)
		self.all_gestures: List[Dict] = []
		self.selected_addon = ""
		self.addon_sections: Dict[str, List[str]] = {}
		self.ini_path = ""
		self.gestures_data: List[Dict] = []      # filtered list of gestures (current view)
		self.checked_indices: Set[int] = set()   # indices in gestures_data that are checked
		self.SetEscapeId(wx.ID_CLOSE)
		self._setup_ui()
		self._load_gestures_from_ini()
		self.Bind(wx.EVT_CLOSE, lambda e: self.Destroy())

		# Bring dialog to front
		self.Raise()
		wx.CallAfter(self.addon_combo.SetFocus)

	def _get_gesture_display(self, gesture: str) -> str:
		try:
			display_text = inputCore.getDisplayTextForGestureIdentifier(gesture)
			if display_text and len(display_text) >= 2:
				return display_text[1]
		except:
			pass
		return gesture

	def _get_script_display_name(self, script_name: str, section: str) -> str:
		try:
			all_mappings = inputCore.manager.getAllGestureMappings()
			if section in all_mappings and script_name in all_mappings[section]:
				info = all_mappings[section][script_name]
				return getattr(info, 'displayName', None) or script_name
		except:
			pass
		return script_name

	def _get_context_display(self, section: str) -> str:
		if section.startswith("globalPlugins."):
			parts = section.split(".")
			if len(parts) >= 2:
				return parts[1]
		elif section.startswith("appModules."):
			parts = section.split(".")
			if len(parts) >= 2:
				return _("Application: ") + parts[1]
		return section

	def _setup_ui(self):
		main_sizer = wx.BoxSizer(wx.VERTICAL)

		instructions = wx.StaticText(self, label=_("Clean up gestures for uninstalled addons from gestures.ini:"))
		main_sizer.Add(instructions, 0, wx.ALL, 10)

		# Addon filter combo
		addon_sizer = wx.BoxSizer(wx.HORIZONTAL)
		addon_label = wx.StaticText(self, label=_("Addon name:"))
		addon_sizer.Add(addon_label, 0, wx.RIGHT | wx.ALIGN_CENTER_VERTICAL, 5)

		self.addon_combo = wx.ComboBox(self, style=wx.CB_READONLY)
		self.addon_combo.Bind(wx.EVT_COMBOBOX, self.onAddonChanged)
		addon_sizer.Add(self.addon_combo, 1, wx.EXPAND)

		main_sizer.Add(addon_sizer, 0, wx.LEFT | wx.RIGHT | wx.BOTTOM | wx.EXPAND, 10)

		# Check list box (instead of ListCtrl)
		self.checkList = wx.CheckListBox(self, style=wx.BORDER_SUNKEN)
		self.checkList.Bind(wx.EVT_KEY_DOWN, self.onKeyDown)
		self.checkList.Bind(wx.EVT_CHECKLISTBOX, self.onCheckToggle)
		main_sizer.Add(self.checkList, 1, wx.ALL | wx.EXPAND, 10)

		btn_sizer = wx.BoxSizer(wx.HORIZONTAL)

		self.deleteBtn = wx.Button(self, label=_("Remove Checked"))
		self.deleteBtn.Bind(wx.EVT_BUTTON, self.onDelete)

		self.clearBtn = wx.Button(self, label=_("Clear All"))
		self.clearBtn.Bind(wx.EVT_BUTTON, self.onClearAll)

		closeBtn = wx.Button(self, wx.ID_CLOSE, label=_("Close"))

		btn_sizer.Add(self.deleteBtn, 0, wx.LEFT, 10)
		btn_sizer.Add(self.clearBtn, 0, wx.LEFT, 10)
		btn_sizer.AddStretchSpacer()
		btn_sizer.Add(closeBtn, 0)
		main_sizer.Add(btn_sizer, 0, wx.ALL | wx.EXPAND, 10)

		self.SetSizer(main_sizer)

	def _get_gestures_ini_path(self):
		config_dir = getattr(globalVars.appArgs, 'configPath', None)
		if not config_dir:
			config_dir = os.path.join(os.environ.get('APPDATA', ''), 'nvda')
		return os.path.join(config_dir, "gestures.ini")

	def _load_gestures_from_ini(self):
		self.all_gestures = []
		self.addon_sections = {}
		self.ini_path = self._get_gestures_ini_path()

		if not os.path.exists(self.ini_path):
			self.clearBtn.Disable()
			self._apply_filter()
			return

		try:
			from configobj import ConfigObj
			conf = ConfigObj(self.ini_path, encoding="utf-8", list_values=False)

			for section in conf.sections:
				for gesture_id in conf[section]:
					script_value = conf[section][gesture_id]
					if isinstance(script_value, list):
						script_list = script_value
					else:
						script_list = [script_value]

					for script_name in script_list:
						if script_name == "None":
							continue

						is_addon = False
						addon_name = ""
						if section.startswith("globalPlugins."):
							parts = section.split('.')
							if len(parts) > 1:
								addon_module_name = parts[1]
								if addon_module_name.lower() not in ['main', 'run']:
									is_addon = True
									addon_name = addon_module_name
						elif section.startswith("appModules."):
							parts = section.split('.')
							if len(parts) > 1:
								addon_name = parts[1]
								is_addon = True

						if is_addon:
							display_name = self._get_script_display_name(script_name, section)
							self.all_gestures.append({
								'section': section,
								'gesture': gesture_id,
								'script': script_name,
								'display_name': display_name,
								'is_addon': True,
								'addon_name': addon_name,
								'is_still_installed': self._is_addon_still_installed(addon_name, section)
							})
							if addon_name not in self.addon_sections:
								self.addon_sections[addon_name] = []
							if section not in self.addon_sections[addon_name]:
								self.addon_sections[addon_name].append(section)

			self._apply_filter()
			self._populate_addon_combo()
		except Exception as e:
			log.error(f"Error loading gestures: {e}")

	def _is_addon_still_installed(self, addon_name: str, section: str) -> bool:
		try:
			for addon in addonHandler.getAvailableAddons():
				if (addon.name == addon_name or
					addon.manifest.get('name') == addon_name or
					addon.manifest.get('summary') == addon_name):
					return True
			if section.startswith("appModules."):
				return True
			return False
		except:
			return False

	def _populate_addon_combo(self):
		self.addon_combo.Clear()
		self.addon_combo.Append(_("All addons"), "")
		for addon_name in sorted(self.addon_sections.keys(), key=lambda x: x.lower()):
			self.addon_combo.Append(addon_name, addon_name)
		self.addon_combo.SetSelection(0)
		self.selected_addon = ""

	def _apply_filter(self):
		"""Filter gestures based on selected addon and store in self.gestures_data."""
		filtered = self.all_gestures
		if self.selected_addon and self.selected_addon in self.addon_sections:
			addon_sections = self.addon_sections[self.selected_addon]
			filtered = [g for g in filtered if g['section'] in addon_sections]
		self.gestures_data = filtered
		self.checked_indices.clear()
		self._populate_checklist()

	def _populate_checklist(self):
		"""Populate the check list with formatted gesture strings."""
		self.checkList.Clear()
		for i, item in enumerate(self.gestures_data):
			gesture_display = self._get_gesture_display(item['gesture'])
			function_name = item['display_name']
			if function_name.startswith("Function: "):
				function_name = function_name[10:]
			context_name = self._get_context_display(item['section'])

			# Format: "Gesture: ... | Function: ... | Context: ..."
			label = f"{gesture_display} | {function_name} | {context_name}"
			self.checkList.Append(label)

			# Mark colour for uninstalled addons (gray text)
			if not item['is_still_installed']:
				self.checkList.SetItemForegroundColour(i, wx.Colour(128, 128, 128))

		self.clearBtn.Enable(len(self.all_gestures) > 0)
		self._update_delete_button()

	def onCheckToggle(self, event):
		index = event.GetSelection()
		label = self.checkList.GetString(index)
		status = _("checked") if self.checkList.IsChecked(index) else _("not checked")
		# Direct ui.message (no wx.CallAfter) as in CleanConfig
		ui.message(f"{label} {status}")
		if self.checkList.IsChecked(index):
			self.checked_indices.add(index)
		else:
			self.checked_indices.discard(index)

	def _update_delete_button(self):
		"""Enable delete button if there are checked items or if an addon is selected."""
		if self.selected_addon:
			self.deleteBtn.SetLabel(_("&Remove addon"))
			self.deleteBtn.Enable(True)
		else:
			self.deleteBtn.SetLabel(_("Remove Checked"))
			self.deleteBtn.Enable(bool(self.checked_indices))

	def onAddonChanged(self, event):
		selection = self.addon_combo.GetSelection()
		if selection == 0:
			self.selected_addon = ""
		else:
			self.selected_addon = self.addon_combo.GetClientData(selection)
		self._apply_filter()
		wx.CallAfter(self.addon_combo.SetFocus)

	def onKeyDown(self, event):
		key = event.GetKeyCode()
		if key == wx.WXK_DELETE:
			self.onDelete(None)
		elif key in (wx.WXK_RETURN, wx.WXK_NUMPAD_ENTER):
			selected = self.checkList.GetSelection()
			if selected != -1:
				current_state = self.checkList.IsChecked(selected)
				self.checkList.Check(selected, not current_state)
				label = self.checkList.GetString(selected)
				status = _("checked") if not current_state else _("not checked")
				# Direct ui.message
				ui.message(f"{label} {status}")
				if not current_state:
					self.checked_indices.add(selected)
				else:
					self.checked_indices.discard(selected)
				event.Skip(False)
				return
		event.Skip()

	def _remove_gestures_from_ini(self, items_to_remove: List[Dict]) -> bool:
		"""Remove given gesture entries from gestures.ini."""
		try:
			from configobj import ConfigObj
			conf = ConfigObj(self.ini_path, encoding="utf-8", list_values=False)

			for item in items_to_remove:
				section = item['section']
				gesture = item['gesture']
				script = item['script']

				if section in conf and gesture in conf[section]:
					current = conf[section][gesture]
					if isinstance(current, list):
						if script in current:
							current.remove(script)
							if not current:
								del conf[section][gesture]
							else:
								conf[section][gesture] = current
					else:
						if current == script:
							del conf[section][gesture]

				if section in conf and not conf[section]:
					del conf[section]

			conf.write()
			return True
		except Exception as e:
			log.error(f"Error removing gestures: {e}")
			return False

	def _remove_selected_addon(self):
		"""Remove all gestures for the currently selected addon."""
		if not self.selected_addon or self.selected_addon not in self.addon_sections:
			return

		addon_name = self.selected_addon
		items_to_remove = [g for g in self.all_gestures if g['addon_name'] == addon_name]
		if not items_to_remove:
			return

		msg = _("Remove all {} custom gestures for addon '{}'?").format(len(items_to_remove), addon_name)
		if wx.MessageBox(msg, _("Confirm"), wx.YES_NO) == wx.YES:
			if self._remove_gestures_from_ini(items_to_remove):
				ui.message(_("Success"))
				self._load_gestures_from_ini()
				self._update_delete_button()
				wx.CallAfter(self.addon_combo.SetFocus)
			else:
				ui.message(_("Failed to remove addon from configuration."))

	def _remove_checked_gestures(self):
		"""Remove all gestures that are currently checked."""
		if not self.checked_indices:
			ui.message(_("No items selected."))
			return

		items_to_remove = [self.gestures_data[i] for i in self.checked_indices]
		msg = _("Remove {} selected gesture(s)?").format(len(items_to_remove))
		if wx.MessageBox(msg, _("Confirm"), wx.YES_NO) == wx.YES:
			if self._remove_gestures_from_ini(items_to_remove):
				ui.message(_("Success"))
				self._load_gestures_from_ini()
				self._update_delete_button()
				wx.CallAfter(self.addon_combo.SetFocus)
			else:
				ui.message(_("Failed to remove selected gestures."))

	def onDelete(self, event):
		if self.selected_addon:
			self._remove_selected_addon()
		else:
			self._remove_checked_gestures()

	def onClearAll(self, event):
		"""Remove all addon gestures."""
		if not self.all_gestures:
			ui.message(_("No addon gestures to clear."))
			return

		msg = _("Remove all {} custom gestures from {} addons?").format(
			len(self.all_gestures), len(self.addon_sections))
		if wx.MessageBox(msg, _("Confirm"), wx.YES_NO | wx.ICON_WARNING) == wx.YES:
			items_to_remove = self.all_gestures[:]
			if self._remove_gestures_from_ini(items_to_remove):
				ui.message(_("Success"))
				self._load_gestures_from_ini()
				self._update_delete_button()
				wx.CallAfter(self.addon_combo.SetFocus)
			else:
				ui.message(_("Failed to clear gestures from configuration."))