# CheckDuplicateGestures.py

import wx
import gui
import inputCore
import config
from logHandler import log
import ui
from typing import List, Dict, Set, Tuple
import addonHandler
try:
    addonHandler.initTranslation()
except addonHandler.AddonError:
    log.warning("Unable to init translations.")

def _normalize_gesture(gesture: str) -> str:
    """Normalize a gesture string by removing keyboard layout information."""
    norm_gesture = gesture
    try:
        if 'keyboard' in config.conf and 'keyboardLayout' in config.conf['keyboard']:
            keyboard_layout = config.conf['keyboard']['keyboardLayout']
            if keyboard_layout:
                layout_str = f"({keyboard_layout})"
                norm_gesture = norm_gesture.replace(layout_str, "")
    except Exception as e:
        log.debug(f"Normalization skipped for {gesture}: {e}")
    return norm_gesture

def find_duplicate_gestures_data() -> List[Dict]:
    """Scans all registered gestures to find duplicates."""
    all_gestures = []
    seen_keys: Set[Tuple[str, str, str]] = set()

    try:
        all_mappings = inputCore.manager.getAllGestureMappings()
        for category, scripts in all_mappings.items():
            for script_name, script_info in scripts.items():
                if not hasattr(script_info, 'gestures'):
                    continue
                for gesture in script_info.gestures:
                    try:
                        norm = _normalize_gesture(gesture)
                        class_name = getattr(script_info, 'className', "Unknown")
                        unique_key = (norm, script_name, class_name)
                        if unique_key in seen_keys:
                            continue
                        seen_keys.add(unique_key)
                        all_gestures.append({
                            'gesture': gesture,
                            'norm_gesture': norm,
                            'category': category,
                            'displayName': getattr(script_info, 'displayName', script_name),
                            'className': class_name,
                            'scriptName': script_name
                        })
                    except:
                        continue
    except Exception as e:
        log.error(f"Critical error scanning gestures: {e}")

    counts: Dict[str, int] = {}
    for g in all_gestures:
        n = g['norm_gesture']
        counts[n] = counts.get(n, 0) + 1

    duplicates = [g for g in all_gestures if counts[g['norm_gesture']] > 1]
    duplicates.sort(key=lambda x: x['norm_gesture'])
    return duplicates

class DuplicateGesturesDialog(wx.Dialog):
    def __init__(self, parent, duplicates: List[Dict]):
        super().__init__(parent, title=_("Duplicate Gestures"), size=(800, 500))
        self.duplicates = duplicates
        self.selected_item_index = -1
        self.SetEscapeId(wx.ID_CLOSE)
        self._setup_ui()
        self.Bind(wx.EVT_CLOSE, lambda e: self.Destroy())

    def _get_gesture_display(self, gesture: str) -> str:
        try:
            display_text = inputCore.getDisplayTextForGestureIdentifier(gesture)
            if display_text and len(display_text) >= 2:
                return display_text[1]
        except:
            pass
        return gesture

    def _get_context_display(self, class_name: str) -> str:
        """Clean and improve context name display"""
        if class_name == "Unknown":
            return _("Unknown")
        if class_name.startswith("globalPlugins."):
            parts = class_name.split(".")
            if len(parts) >= 2:
                return parts[1]  # addon name
        if class_name.startswith("appModules."):
            parts = class_name.split(".")
            if len(parts) >= 2:
                return _("Application: ") + parts[1]
        return class_name

    def _setup_ui(self):
        main_sizer = wx.BoxSizer(wx.VERTICAL)

        txt = _("Found {} duplicate entries. Select an item and click 'Open' to fix.").format(len(self.duplicates))
        instructions = wx.StaticText(self, label=txt)
        main_sizer.Add(instructions, 0, wx.ALL, 10)

        self.gesturesList = wx.ListCtrl(self, style=wx.LC_REPORT | wx.LC_SINGLE_SEL | wx.BORDER_SUNKEN)
        self.gesturesList.InsertColumn(0, _("Gesture"), width=150)
        self.gesturesList.InsertColumn(1, _("Function"), width=350)
        self.gesturesList.InsertColumn(2, _("Context"), width=250)

        main_sizer.Add(self.gesturesList, 1, wx.ALL | wx.EXPAND, 10)

        btn_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.openBtn = wx.Button(self, label=_("&Open Input Gestures"))
        self.openBtn.Disable()
        self.openBtn.Bind(wx.EVT_BUTTON, self.onOpenInputGestures)

        closeBtn = wx.Button(self, wx.ID_CLOSE, label=_("&Close"))

        btn_sizer.Add(self.openBtn, 0, wx.RIGHT, 10)
        btn_sizer.Add(closeBtn, 0)
        main_sizer.Add(btn_sizer, 0, wx.ALIGN_RIGHT | wx.ALL, 10)

        self.SetSizer(main_sizer)
        self._populate_list()

        self.gesturesList.Bind(wx.EVT_LIST_ITEM_SELECTED, self.onItemSelected)
        self.gesturesList.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.onOpenInputGestures)
        self.gesturesList.Bind(wx.EVT_CHAR_HOOK, self.onKeyDown)

        wx.CallAfter(self.gesturesList.SetFocus)

    def _populate_list(self):
        self.gesturesList.DeleteAllItems()
        for i, item in enumerate(self.duplicates):
            gesture_display = self._get_gesture_display(item['gesture'])
            gesture_display = gesture_display.replace(';', '').replace(':', '')
            self.gesturesList.InsertItem(i, gesture_display)

            function_name = item['displayName']
            if function_name.startswith("Function: "):
                function_name = function_name[10:]
            function_name = function_name.replace(';', '').replace(':', '')
            self.gesturesList.SetItem(i, 1, function_name)

            context_name = self._get_context_display(item['className'])
            context_name = context_name.replace(';', '').replace(':', '')
            self.gesturesList.SetItem(i, 2, context_name)

    def onItemSelected(self, event):
        self.selected_item_index = event.GetIndex()
        self.openBtn.Enable()

    def onKeyDown(self, event):
        if event.GetKeyCode() in (wx.WXK_RETURN, wx.WXK_NUMPAD_ENTER):
            idx = self.gesturesList.GetFirstSelected()
            if idx != -1:
                self.selected_item_index = idx
                self.onOpenInputGestures(None)
        elif event.GetKeyCode() == wx.WXK_ESCAPE:
            self.Close()
        else:
            event.Skip()

    def onOpenInputGestures(self, event):
        if self.selected_item_index == -1:
            return

        selected_item = self.duplicates[self.selected_item_index]
        script_name = selected_item['scriptName']

        try:
            # Use the EXACT method from the old version that shows Add/Remove buttons
            from gui.inputGestures import InputGesturesDialog
            
            # Close current dialog first
            self.Close()
            
            # Create and show the Input Gestures dialog directly
            dialog = InputGesturesDialog(gui.mainFrame)
            if script_name and hasattr(dialog, 'filterCtrl'):
                dialog.filterCtrl.SetValue(script_name)
                # Try to call filter method with proper argument
                if hasattr(dialog, 'filter'):
                    dialog.filter(filterText=script_name)
            
            # Show the dialog
            dialog.Show()
            dialog.Raise()
            
            # Wait for dialog to be fully loaded and tree items to be available
            def expand_and_focus():
                try:
                    if hasattr(dialog, 'gesturesTree'):
                        tree = dialog.gesturesTree
                        
                        # Get the root item
                        root = tree.GetRootItem()
                        if root.IsOk():
                            # Find and expand the first child
                            item, cookie = tree.GetFirstChild(root)
                            if item.IsOk():
                                # Expand the item to show Remove button
                                tree.Expand(item)
                                tree.SelectItem(item)
                                tree.EnsureVisible(item)
                                
                                # Now move down to the first child to show Add/Remove buttons
                                child_item, child_cookie = tree.GetFirstChild(item)
                                if child_item.IsOk():
                                    tree.SelectItem(child_item)
                                    tree.EnsureVisible(child_item)
                                
                                # Set focus to tree
                                tree.SetFocus()
                                
                                # Announce that dialog is ready
                                ui.message(_("Input gestures dialog opened. Navigate with arrow keys to see Add and Remove buttons."))
                except Exception as e:
                    log.error(f"Error expanding tree: {e}")
            
            # Schedule the expansion after dialog is shown
            wx.CallLater(200, expand_and_focus)
            
        except Exception as e:
            log.error(f"Failed to open Input Gestures dialog: {e}")
            ui.message(_("Failed to open Input Gestures dialog"))


