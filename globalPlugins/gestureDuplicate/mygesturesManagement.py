# mygesturesManagement.py

import wx
import os
import globalVars
import gui
import ui
from logHandler import log
import inputCore
import addonHandler
import globalPluginHandler
import appModuleHandler
from typing import List, Dict
try:
    addonHandler.initTranslation()
except addonHandler.AddonError:
    log.warning("Unable to init translations.")

class MyGesturesManagementDialog(wx.Dialog):
    """Dialog to manage custom user gestures for addons only."""

    def __init__(self, parent):
        super().__init__(parent, title=_("My Gestures Management"), size=(850, 600))
        self.user_gestures: List[Dict] = []
        self.all_gestures: List[Dict] = []
        self.selected_addon = ""
        self.addon_sections: Dict[str, List[str]] = {}  # addon_name -> list of sections
        self.ini_path = ""
        self.SetEscapeId(wx.ID_CLOSE)
        self._setup_ui()
        self._load_gestures_from_ini()
        self.Bind(wx.EVT_CLOSE, lambda e: self.Destroy())

        # Set initial focus
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
        """Clean and improve context name display for better readability"""
        if section.startswith("globalPlugins."):
            parts = section.split(".")
            if len(parts) >= 2:
                return parts[1]  # addon name
        return section

    def _setup_ui(self):
        main_sizer = wx.BoxSizer(wx.VERTICAL)

        instructions = wx.StaticText(self, label=_("Clean up gestures for uninstalled addons from gestures.ini:"))
        main_sizer.Add(instructions, 0, wx.ALL, 10)

        # Addon filter
        addon_sizer = wx.BoxSizer(wx.HORIZONTAL)
        addon_label = wx.StaticText(self, label=_("Addon name:"))
        addon_sizer.Add(addon_label, 0, wx.RIGHT | wx.ALIGN_CENTER_VERTICAL, 5)

        self.addon_combo = wx.ComboBox(self, style=wx.CB_READONLY)
        self.addon_combo.Bind(wx.EVT_COMBOBOX, self.onAddonChanged)
        addon_sizer.Add(self.addon_combo, 1, wx.EXPAND)

        main_sizer.Add(addon_sizer, 0, wx.LEFT | wx.RIGHT | wx.BOTTOM | wx.EXPAND, 10)

        self.gesturesList = wx.ListCtrl(self, style=wx.LC_REPORT | wx.LC_SINGLE_SEL | wx.BORDER_SUNKEN)
        self.gesturesList.InsertColumn(0, _("Gesture"), width=150)
        self.gesturesList.InsertColumn(1, _("Function"), width=350)
        self.gesturesList.InsertColumn(2, _("Context"), width=250)

        main_sizer.Add(self.gesturesList, 1, wx.LEFT | wx.RIGHT | wx.BOTTOM | wx.EXPAND, 10)

        btn_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.deleteBtn = wx.Button(self, label=_("&Remove addon"))
        self.deleteBtn.Disable()
        self.deleteBtn.Bind(wx.EVT_BUTTON, self.onDelete)

        self.clearBtn = wx.Button(self, label=_("C&lear All"))
        self.clearBtn.Bind(wx.EVT_BUTTON, self.onClearAll)

        closeBtn = wx.Button(self, wx.ID_CLOSE, label=_("&Close"))

        btn_sizer.Add(self.deleteBtn, 0, wx.LEFT, 10)
        btn_sizer.Add(self.clearBtn, 0, wx.LEFT, 10)
        btn_sizer.AddStretchSpacer()
        btn_sizer.Add(closeBtn, 0)
        main_sizer.Add(btn_sizer, 0, wx.ALL | wx.EXPAND, 10)

        self.SetSizer(main_sizer)

        self.gesturesList.Bind(wx.EVT_LIST_ITEM_SELECTED, self.onItemSelected)
        self.gesturesList.Bind(wx.EVT_CHAR_HOOK, self.onKeyDown)

    def _get_gestures_ini_path(self):
        """Get the path to gestures.ini file."""
        config_dir = getattr(globalVars.appArgs, 'configPath', None)
        if not config_dir:
            config_dir = os.path.join(os.environ.get('APPDATA', ''), 'nvda')

        ini_path = os.path.join(config_dir, "gestures.ini")
        return ini_path

    def _load_gestures_from_ini(self):
        """Load gestures from gestures.ini file in user config directory."""
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

                        # Only process addon gestures
                        is_addon = False
                        addon_name = ""
                        if section.startswith("globalPlugins."):
                            parts = section.split('.')
                            if len(parts) > 1:
                                addon_module_name = parts[1]
                                if addon_module_name.lower() not in ['main', 'run']:
                                    is_addon = True
                                    addon_name = addon_module_name

                                    if addon_name not in self.addon_sections:
                                        self.addon_sections[addon_name] = []
                                    if section not in self.addon_sections[addon_name]:
                                        self.addon_sections[addon_name].append(section)

                        # Only add addon gestures to the list
                        if is_addon:
                            display_name = self._get_script_display_name(script_name, section)

                            self.all_gestures.append({
                                'section': section,
                                'gesture': gesture_id,
                                'script': script_name,
                                'display_name': display_name,
                                'is_addon': True,
                                'addon_name': addon_name,
                                'is_still_installed': self._is_addon_still_installed(addon_name)
                            })

            self._apply_filter()
            self._populate_addon_combo()

        except Exception as e:
            log.error(f"Error loading gestures: {e}")

    def _is_addon_still_installed(self, addon_name: str) -> bool:
        """Check if an addon is still installed in NVDA."""
        try:
            for addon in addonHandler.getAvailableAddons():
                if (addon.name == addon_name or 
                    addon.manifest.get('name') == addon_name or
                    addon.manifest.get('summary') == addon_name):
                    return True
            return False
        except Exception as e:
            log.debug(f"Error checking if addon is installed: {e}")
            return False

    def _populate_addon_combo(self):
        """Populate the addon combo box with available addons sorted alphabetically."""
        self.addon_combo.Clear()
        self.addon_combo.Append(_("All addons"), "")

        addon_names = sorted(self.addon_sections.keys(), key=lambda x: x.lower())

        for addon_name in addon_names:
            self.addon_combo.Append(addon_name, addon_name)

        self.addon_combo.SetSelection(0)
        self.selected_addon = ""

    def _apply_filter(self):
        """Apply current filter to gestures list."""
        self.gesturesList.DeleteAllItems()
        self.user_gestures = []

        filtered_gestures = self.all_gestures
        
        if self.selected_addon and self.selected_addon in self.addon_sections:
            addon_sections = self.addon_sections[self.selected_addon]
            filtered_gestures = [g for g in filtered_gestures if g['section'] in addon_sections]

        for idx, item in enumerate(filtered_gestures):
            self.user_gestures.append(item)
            gesture_display = self._get_gesture_display(item['gesture'])
            gesture_display = gesture_display.replace(';', '').replace(':', '')
            self.gesturesList.InsertItem(idx, gesture_display)

            function_name = item['display_name']
            if function_name.startswith("Function: "):
                function_name = function_name[10:]
            function_name = function_name.replace(';', '').replace(':', '')
            self.gesturesList.SetItem(idx, 1, function_name)

            context_name = self._get_context_display(item['section'])
            context_name = context_name.replace(';', '').replace(':', '')
            self.gesturesList.SetItem(idx, 2, context_name)
            
            # Set item text color based on availability
            if not item['is_still_installed']:
                self.gesturesList.SetItemTextColour(idx, wx.Colour(128, 128, 128))  # Gray for unavailable

        self.clearBtn.Enable(len(self.all_gestures) > 0)
        self._update_delete_button()

        if self.gesturesList.GetItemCount() > 0:
            self.gesturesList.Select(0)
        else:
            self.deleteBtn.Disable()

    def _update_delete_button(self):
        """Update delete button label and state based on current selection."""
        selected_gesture_index = self.gesturesList.GetFirstSelected()

        if selected_gesture_index != -1:
            # If a specific gesture is selected, change label to "Remove Selected"
            self.deleteBtn.SetLabel(_("&Remove Selected"))
            self.deleteBtn.Enable()
        elif self.selected_addon:
            # If an addon is selected in combo but no gesture is selected in list, change to "Remove addon"
            self.deleteBtn.SetLabel(_("&Remove addon"))
            self.deleteBtn.Enable()
        else:
            self.deleteBtn.SetLabel(_("&Remove addon"))
            self.deleteBtn.Disable()

    def onAddonChanged(self, event):
        """Handle addon selection change."""
        selection = self.addon_combo.GetSelection()
        if selection == 0:
            self.selected_addon = ""
        else:
            self.selected_addon = self.addon_combo.GetClientData(selection)

        self._apply_filter()
        wx.CallAfter(self.addon_combo.SetFocus)

    def onItemSelected(self, event):
        self._update_delete_button()

    def onKeyDown(self, event):
        if event.GetKeyCode() == wx.WXK_DELETE:
            self.onDelete(None)
        elif event.GetKeyCode() == wx.WXK_ESCAPE:
            self.Close()
        else:
            event.Skip()

    def _remove_addon_from_ini_file(self, addon_name):
        """Remove all gestures for a specific addon from the gestures.ini file."""
        try:
            from configobj import ConfigObj
            conf = ConfigObj(self.ini_path, encoding="utf-8", list_values=False)

            sections_to_remove = []
            for section in conf.sections:
                if section.startswith("globalPlugins."):
                    parts = section.split('.')
                    if len(parts) > 1 and parts[1] == addon_name:
                        sections_to_remove.append(section)

            for section in sections_to_remove:
                if section in conf:
                    del conf[section]

            conf.write()
            return len(sections_to_remove) > 0
        except Exception as e:
            log.error(f"Error removing addon from ini file: {e}")

        return False

    def _clear_all_from_ini_file(self):
        """Clear all addon gestures from the ini file."""
        try:
            from configobj import ConfigObj
            conf = ConfigObj(self.ini_path, encoding="utf-8", list_values=False)

            sections_to_remove = []
            for section in conf.sections:
                if section.startswith("globalPlugins."):
                    parts = section.split('.')
                    if len(parts) > 1 and parts[1].lower() not in ['main', 'run']:
                        sections_to_remove.append(section)

            for section in sections_to_remove:
                if section in conf:
                    del conf[section]

            conf.write()
            return len(sections_to_remove) > 0
        except Exception as e:
            log.error(f"Error clearing ini file: {e}")

        return False

    def onDelete(self, event):
        """Handle delete action - either remove selected gesture or entire addon."""
        selected_gesture_index = self.gesturesList.GetFirstSelected()

        if selected_gesture_index != -1:
            # User selected a specific gesture in the list
            self._remove_selected_gesture(selected_gesture_index)
        elif self.selected_addon:
            # User selected an addon in combo but no specific gesture in list
            self._remove_selected_addon()
        else:
            return

    def _remove_selected_gesture(self, index):
        """Remove the selected gesture from the list and ini file."""
        item = self.user_gestures[index]
        
        # Get addon name for confirmation message
        addon_name = item['addon_name']
        gesture_display = self._get_gesture_display(item['gesture'])
        
        msg = _("Remove this custom gesture for addon '{}'?\n\nGesture: {}\nFunction: {}").format(
            addon_name, gesture_display, item['display_name'])
        
        if wx.MessageBox(msg, _("Confirm"), wx.YES_NO) == wx.YES:
            try:
                # Remove single gesture
                from configobj import ConfigObj
                conf = ConfigObj(self.ini_path, encoding="utf-8", list_values=False)
                
                section = item['section']
                gesture = item['gesture']
                script = item['script']
                
                if section in conf and gesture in conf[section]:
                    current_value = conf[section][gesture]
                    
                    if isinstance(current_value, list):
                        if script in current_value:
                            current_value.remove(script)
                            if not current_value:
                                del conf[section][gesture]
                            else:
                                conf[section][gesture] = current_value
                    else:
                        if current_value == script:
                            del conf[section][gesture]
                    
                    if section in conf and not conf[section]:
                        del conf[section]
                    
                    conf.write()
                    ui.message(_("Success"))
                    self._load_gestures_from_ini()
                    self._update_delete_button()
                    
                    # Focus back to addon combo
                    wx.CallAfter(self.addon_combo.SetFocus)
                else:
                    ui.message(_("Failed to remove gesture from configuration."))
            except Exception as e:
                log.error(f"Failed to remove gesture: {e}")
                ui.message(_("Failed to remove gesture."))

    def _remove_selected_addon(self):
        """Remove all gestures for the selected addon."""
        if not self.selected_addon or self.selected_addon not in self.addon_sections:
            return

        addon_name = self.selected_addon
        gesture_count = len([g for g in self.all_gestures if g['addon_name'] == addon_name])

        msg = _("Remove all {} custom gestures for addon '{}'?").format(gesture_count, addon_name)

        if wx.MessageBox(msg, _("Confirm"), wx.YES_NO) == wx.YES:
            try:
                if self._remove_addon_from_ini_file(addon_name):
                    ui.message(_("Success"))
                    self._load_gestures_from_ini()
                    self._update_delete_button()
                    
                    # Focus back to addon combo
                    wx.CallAfter(self.addon_combo.SetFocus)
                else:
                    ui.message(_("Failed to remove addon from configuration."))
            except Exception as e:
                log.error(f"Failed to remove addon gestures: {e}")
                ui.message(_("Error during addon gesture removal."))

    def onClearAll(self, event):
        """Clears all addon gestures from the ini file."""
        addon_count = len(self.addon_sections)
        gesture_count = len(self.all_gestures)
        
        if gesture_count == 0:
            ui.message(_("No addon gestures to clear."))
            return
            
        msg = _("Remove all {} custom gestures from {} addons?").format(gesture_count, addon_count)
        
        if wx.MessageBox(msg, _("Confirm"), wx.YES_NO | wx.ICON_WARNING) == wx.YES:
            try:
                if self._clear_all_from_ini_file():
                    ui.message(_("Success"))
                    self._load_gestures_from_ini()
                    self._update_delete_button()
                    
                    # Focus back to addon combo
                    wx.CallAfter(self.addon_combo.SetFocus)
                else:
                    ui.message(_("Failed to clear gestures from configuration."))
            except Exception as e:
                log.error(f"Failed to clear all gestures: {e}")
                ui.message(_("Error during mass deletion."))