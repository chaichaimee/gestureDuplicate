# __init__.py

import addonHandler
import globalPluginHandler
from globalVars import appArgs
import gui
import wx
import config
from typing import Callable, List, Dict, Optional, Tuple, Set
from logHandler import log
from scriptHandler import script
from inputCore import InputGesture
import inputCore
import ui
import time

try:
    addonHandler.initTranslation()
except addonHandler.AddonError:
    log.warning("Unable to init translations. This may be because the addon is running from NVDA scratchpad.")
_: Callable[[str], str]
curAddon = addonHandler.getCodeAddon()
ADDON_NAME: str = curAddon.manifest['name']
ADDON_SUMMARY: str = curAddon.manifest['summary']


class DuplicateGesturesDialog(wx.Dialog):
    """Dialog to display duplicate gestures and manage them."""
    def __init__(self, parent, duplicates: List[Dict], plugin: 'GlobalPlugin', *args, **kwargs):
        # Translators: Title of the duplicate gestures dialog
        title = _("Duplicate Gestures")
        super().__init__(parent, title=title, size=(800, 500), *args, **kwargs)
        self.parent = parent
        self.plugin = plugin
        self.duplicates = duplicates
        self.selected_item_index = -1
       
        self.SetEscapeId(wx.ID_CLOSE)
        self._setup_ui()
        self.Bind(wx.EVT_CLOSE, self.onClose)

    def _normalize_gesture(self, gesture: str) -> str:
        """Normalize a gesture string by removing keyboard layout information."""
        norm_gesture = gesture
        try:
            if 'keyboard' in config.conf and 'keyboardLayout' in config.conf['keyboard']:
                keyboard_layout = config.conf['keyboard']['keyboardLayout']
                if keyboard_layout:
                    layout_str = f"({keyboard_layout})"
                    norm_gesture = norm_gesture.replace(layout_str, "")
        except Exception as e:
            log.error(f"Error normalizing gesture {gesture}: {e}")
        return norm_gesture

    def _get_gesture_display(self, gesture: str) -> str:
        """Get a clean display text for gesture."""
        try:
            display_text = inputCore.getDisplayTextForGestureIdentifier(gesture)
            if display_text and len(display_text) >= 2:
                # Return only the description part without source
                return display_text[1]
        except:
            pass
        return gesture

    def _setup_ui(self):
        """Setup the user interface."""
        main_sizer = wx.BoxSizer(wx.VERTICAL)
       
        instructions = wx.StaticText(
            self,
            # Translators: Instructions for the duplicate gestures dialog
            label=_("Select a duplicate gesture and use the buttons or context menu to manage it.")
        )
        main_sizer.Add(instructions, 0, wx.ALL | wx.EXPAND, 10)
       
        self.stats_text = wx.StaticText(
            self,
            # Translators: Statistics about duplicate gestures found
            label=_("Found {} duplicate gestures").format(len(self.duplicates))
        )
        main_sizer.Add(self.stats_text, 0, wx.LEFT | wx.RIGHT | wx.BOTTOM, 10)
       
        label = wx.StaticText(self, label=_("Duplicate gestures:"))
        main_sizer.Add(label, 0, wx.LEFT | wx.RIGHT | wx.TOP, 10)
       
        self.gesturesList = wx.ListCtrl(
            self,
            style=wx.LC_REPORT | wx.LC_SINGLE_SEL | wx.BORDER_SUNKEN,
            size=(780, 350)
        )
       
        self.gesturesList.InsertColumn(0, _("Gesture"), width=150)
        self.gesturesList.InsertColumn(1, _("Function"), width=350)
        self.gesturesList.InsertColumn(2, _("Category/Context"), width=250)
       
        main_sizer.Add(self.gesturesList, 1, wx.LEFT | wx.RIGHT | wx.BOTTOM | wx.EXPAND, 10)
       
        info_text = wx.StaticText(
            self,
            # Translators: Information about duplicate gestures
            label=_("Note: Gestures are checked from all contexts (global and application-specific).")
        )
        info_text.SetForegroundColour(wx.Colour(100, 100, 100))
        main_sizer.Add(info_text, 0, wx.LEFT | wx.RIGHT | wx.BOTTOM, 10)
       
        button_sizer = wx.BoxSizer(wx.HORIZONTAL)
       
        self.deleteButton = wx.Button(self, label=_("&Delete Gesture"))
        self.deleteButton.Bind(wx.EVT_BUTTON, self.onDeleteButton)
        self.deleteButton.Disable()
        button_sizer.Add(self.deleteButton, 0, wx.RIGHT, 10)
       
        self.editInInputGesturesButton = wx.Button(self, label=_("&Edit in Input Gestures..."))
        self.editInInputGesturesButton.Bind(wx.EVT_BUTTON, self.onEditInInputGestures)
        self.editInInputGesturesButton.Disable()
        button_sizer.Add(self.editInInputGesturesButton, 0, wx.RIGHT, 20)
       
        self.closeButton = wx.Button(self, wx.ID_CLOSE, label=_("&Close"))
        self.closeButton.Bind(wx.EVT_BUTTON, lambda evt: self.Close())
        button_sizer.Add(self.closeButton, 0)
       
        main_sizer.Add(button_sizer, 0, wx.ALIGN_RIGHT | wx.ALL, 10)
       
        self.SetSizerAndFit(main_sizer)
       
        self._populate_list()
       
        self.gesturesList.Bind(wx.EVT_LIST_ITEM_SELECTED, self.onItemSelected)
        self.gesturesList.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.onItemActivated)
        self.gesturesList.Bind(wx.EVT_CONTEXT_MENU, self.onContextMenu)

    def postInit(self):
        """Called after the dialog is fully shown to set correct focus."""
        if self.gesturesList.GetItemCount() > 0 and len(self.duplicates) > 0:
            self.gesturesList.SetFocus()
            self.gesturesList.Focus(0)
            self.gesturesList.Select(0)
            self._update_selection_and_buttons(0)
        else:
            self.closeButton.SetFocus()
            self.editInInputGesturesButton.Disable()
            self.deleteButton.Disable()

    def _populate_list(self):
        """Populate the list with the current list of duplicate gestures."""
        self.gesturesList.DeleteAllItems()
        self.selected_item_index = -1
       
        if not self.duplicates:
            self.gesturesList.InsertItem(0, _("No duplicate gestures found"))
            for i in range(1, 3):
                self.gesturesList.SetItem(0, i, "")
            self.editInInputGesturesButton.Disable()
            self.deleteButton.Disable()
            return
       
        # Group by normalized gesture
        grouped_duplicates = {}
        normalize_func = self.plugin._normalize_gesture
       
        for item in self.duplicates:
            norm_gesture = normalize_func(item['gesture'])
            if norm_gesture not in grouped_duplicates:
                grouped_duplicates[norm_gesture] = []
            grouped_duplicates[norm_gesture].append(item)
       
        index = 0
        for norm_gesture, items in grouped_duplicates.items():
            # Only show groups that have actual duplicates (more than 1 item)
            if len(items) <= 1:
                continue
               
            for i, item in enumerate(items):
                # Get clean gesture display without source info
                gesture_display = self._get_gesture_display(item['gesture'])
               
                self.gesturesList.InsertItem(index, gesture_display)
               
                display_name = item['displayName'] or item['scriptName']
                self.gesturesList.SetItem(index, 1, display_name)
               
                category_context = item['category'] or f"[{item['moduleName']}]"
                if item['className'] and item['className'] != item['category']:
                    category_context += f" ({item['className']})"
                self.gesturesList.SetItem(index, 2, category_context)
               
                try:
                    data_index = self.duplicates.index(item)
                    self.gesturesList.SetItemData(index, data_index)
                except ValueError:
                    self.gesturesList.SetItemData(index, -1)
               
                # Color code duplicates
                if i == 0:
                    self.gesturesList.SetItemTextColour(index, wx.Colour(200, 0, 0))  # Red for first in group
                else:
                    self.gesturesList.SetItemTextColour(index, wx.Colour(0, 150, 0))  # Green for others
               
                index += 1
       
        self.selected_item_index = -1

    def _update_selection_and_buttons(self, list_index):
        """Update the selected item index and button enabled state."""
        if list_index >= 0:
            data_index = self.gesturesList.GetItemData(list_index)
            if data_index != -1 and self.gesturesList.GetItemText(list_index, 0) != _("No duplicate gestures found"):
                self.selected_item_index = data_index
                self.editInInputGesturesButton.Enable()
                self.deleteButton.Enable()
                return
        self.selected_item_index = -1
        self.editInInputGesturesButton.Disable()
        self.deleteButton.Disable()

    def onItemSelected(self, event):
        list_index = event.GetIndex()
        self._update_selection_and_buttons(list_index)

    def onItemActivated(self, event):
        list_index = event.GetIndex()
        self._update_selection_and_buttons(list_index)
        self._open_input_gestures_filtered()

    def onEditInInputGestures(self, event):
        if self.selected_item_index != -1:
            self._open_input_gestures_filtered()

    def onDeleteButton(self, event):
        if self.selected_item_index != -1:
            self._delete_gesture()

    def onContextMenu(self, event):
        pos = event.GetPosition()
        pos = self.gesturesList.ScreenToClient(pos)
        item_index, flags = self.gesturesList.HitTest(pos)
       
        if item_index == -1:
            list_index = self.gesturesList.GetFirstSelected()
        else:
            list_index = item_index
       
        if list_index == -1:
            return
       
        self.gesturesList.Select(list_index)
        self._update_selection_and_buttons(list_index)
       
        menu = wx.Menu()
       
        edit_item = menu.Append(wx.ID_EDIT, _("&Edit in Input Gestures..."))
        self.Bind(wx.EVT_MENU, self.onContextMenuEdit, edit_item)
       
        delete_item = menu.Append(wx.ID_DELETE, _("&Delete Gesture"))
        self.Bind(wx.EVT_MENU, self.onContextMenuDelete, delete_item)
       
        if self.selected_item_index == -1:
            edit_item.Enable(False)
            delete_item.Enable(False)
       
        self.gesturesList.PopupMenu(menu)
        menu.Destroy()

    def onContextMenuEdit(self, event):
        if self.selected_item_index != -1:
            self._open_input_gestures_filtered()

    def onContextMenuDelete(self, event):
        if self.selected_item_index != -1:
            self._delete_gesture()

    def _get_selected_gesture_data(self) -> Optional[Dict]:
        if self.selected_item_index != -1 and 0 <= self.selected_item_index < len(self.duplicates):
            return self.duplicates[self.selected_item_index]
        return None

    def _open_input_gestures_filtered(self):
        data = self._get_selected_gesture_data()
        if not data:
            return
       
        function_name = data['displayName'] or data['scriptName']
        self._open_input_gestures_dialog(search_query=function_name)

    def _delete_gesture(self):
        data = self._get_selected_gesture_data()
        if not data:
            return
        gesture = data['gesture']
        script_name = data['scriptName']
        class_name = data['className']
       
        msg = _("Are you sure you want to delete the gesture '{gesture}' for the function '{function}' in context '{context}'?").format(
            gesture=gesture, function=data['displayName'] or script_name, context=class_name
        )
       
        if wx.MessageBox(msg, _("Confirm Deletion"), wx.YES_NO | wx.ICON_WARNING) != wx.YES:
            return
        try:
            inputCore.manager.removeGestureMapping(gesture, script_name, class_name)
            ui.message(_("Gesture '{gesture}' deleted successfully.").format(gesture=gesture))
            self.Close()
            self.plugin.onCheckDuplicates_unified(None)
        except Exception as e:
            log.error(f"Error deleting gesture {gesture} for script {script_name} in {class_name}: {e}")
            ui.message(_("Error: Cannot delete the gesture. (May be a non-customizable default gesture)"))

    def _open_input_gestures_dialog(self, search_query: str):
        self.Close()
        try:
            from gui.inputGestures import InputGesturesDialog
            dialog = InputGesturesDialog(gui.mainFrame)
            if search_query:
                dialog.filterCtrl.SetValue(search_query)
            dialog.Show()
            dialog.Raise()
        except ImportError:
            log.error("Could not import gui.inputGestures.InputGesturesDialog")
            ui.message(_("Cannot open Input Gestures dialog. NVDA's Input Gestures dialog module is missing."))
        except Exception as e:
            log.error(f"Error opening Input Gestures dialog: {e}")
            ui.message(_("Cannot open Input Gestures dialog"))

    def onClose(self, event):
        self.Destroy()


class GlobalPlugin(globalPluginHandler.GlobalPlugin):
    scriptCategory: str = ADDON_SUMMARY

    def __init__(self, *args, **kwargs) -> None:
        super(GlobalPlugin, self).__init__(*args, **kwargs)
        if appArgs.secure or config.isAppX:
            return
        self.createMenu()

    def createMenu(self) -> None:
        self.menu: wx.Menu = gui.mainFrame.sysTrayIcon.toolsMenu
        self.subMenu = wx.Menu()
        repeatItem: wx.MenuItem = self.subMenu.Append(wx.ID_ANY, _("&Check Duplicate Gestures"))
        gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.onCheckDuplicates_unified, repeatItem)
        self.mainItem: wx.MenuItem = self.menu.AppendSubMenu(self.subMenu, _(ADDON_SUMMARY))

    def terminate(self, *args, **kwargs) -> None:
        super().terminate(*args, **kwargs)
        try:
            self.menu.Remove(self.mainItem)
        except (RuntimeError, AttributeError):
            pass

    def _find_duplicate_gestures_data(self) -> List[Dict]:
        """Find duplicate gestures from inputCore only, filtering out self-duplicates."""
        all_gestures = []
        seen_gestures: Set[Tuple[str, str, str]] = set()  # (normalized_gesture, script_name, class_name)
       
        # Get gestures from inputCore (registered gestures) only
        # Don't include globalPluginHandler to avoid duplicate entries
        try:
            all_mappings = inputCore.manager.getAllGestureMappings()
            for category in all_mappings:
                for script_name in all_mappings[category]:
                    script_info = all_mappings[category][script_name]
                    for gesture in script_info.gestures:
                        norm_gesture = self._normalize_gesture(gesture)
                        # Create unique key to avoid duplicate entries for the same gesture in same context
                        unique_key = (norm_gesture, script_info.scriptName, script_info.className)
                       
                        # Skip if we've already seen this exact combination
                        if unique_key in seen_gestures:
                            continue
                           
                        seen_gestures.add(unique_key)
                       
                        all_gestures.append({
                            'gesture': gesture,
                            'norm_gesture': norm_gesture,
                            'category': script_info.category,
                            'displayName': script_info.displayName,
                            'className': script_info.className,
                            'moduleName': script_info.moduleName,
                            'scriptName': script_info.scriptName,
                            'source': 'inputCore'
                        })
        except Exception as e:
            log.error(f"Error getting gesture mappings from inputCore: {e}")
       
        # Count normalized gestures
        normalized_counts: Dict[str, int] = {}
        for gesture in all_gestures:
            norm_gesture = gesture['norm_gesture']
            normalized_counts[norm_gesture] = normalized_counts.get(norm_gesture, 0) + 1
       
        # Filter only gestures that have duplicates (count > 1)
        duplicate_norm_gestures = {norm for norm, count in normalized_counts.items() if count > 1}
        duplicates = [gest for gest in all_gestures if gest['norm_gesture'] in duplicate_norm_gestures]
       
        # Sort by normalized gesture for better grouping in dialog
        duplicates.sort(key=lambda x: x['norm_gesture'])
       
        return duplicates

    def _normalize_gesture(self, gesture: str) -> str:
        """Normalize a gesture string by removing keyboard layout information."""
        norm_gesture = gesture
        try:
            if 'keyboard' in config.conf and 'keyboardLayout' in config.conf['keyboard']:
                keyboard_layout = config.conf['keyboard']['keyboardLayout']
                if keyboard_layout:
                    layout_str = f"({keyboard_layout})"
                    norm_gesture = norm_gesture.replace(layout_str, "")
        except Exception as e:
            log.error(f"Error normalizing gesture {gesture}: {e}")
        return norm_gesture

    def onCheckDuplicates_unified(self, event: Optional[wx.PyEvent]) -> None:
        """Handle menu item or script to check for duplicate gestures."""
        wx.CallAfter(self._show_dialog_deferred)

    def _show_dialog_deferred(self):
        """Second deferred call to ensure gesture maps are fully loaded."""
        wx.CallLater(100, self._show_dialog_with_gestures)

    def _show_dialog_with_gestures(self):
        """Find duplicate gestures and show dialog."""
        try:
            # Try multiple times to get all gestures
            max_attempts = 5
            duplicates_data = []
            for attempt in range(max_attempts):
                duplicates_data = self._find_duplicate_gestures_data()
                if duplicates_data or attempt == max_attempts - 1:
                    break
                time.sleep(0.1)
               
            # Update statistics text
            log.info(f"Found {len(duplicates_data)} duplicate gestures")
           
            # Show dialog
            dlg = DuplicateGesturesDialog(gui.mainFrame, duplicates=duplicates_data, plugin=self)
            dlg.Show()
            wx.CallAfter(self._focus_dialog_list, dlg)
           
        except Exception as e:
            log.error(f"Error showing duplicate gestures dialog: {e}")
            ui.message(_("Error checking for duplicate gestures"))

    def _focus_dialog_list(self, dlg):
        """Set focus to the list in the dialog."""
        try:
            if dlg and dlg.gesturesList.GetItemCount() > 0:
                dlg.gesturesList.SetFocus()
                dlg.gesturesList.Focus(0)
                dlg.gesturesList.Select(0)
                dlg._update_selection_and_buttons(0)
        except Exception as e:
            log.error(f"Error focusing dialog list: {e}")

    @script(
        description=_("Check for duplicate input gestures"),
        gestures=["kb:windows+shift+g"]
    )
    def script_duplicates(self, gesture: InputGesture) -> None:
        """Script to check for duplicate gestures."""
        self.onCheckDuplicates_unified(None)
