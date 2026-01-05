# __init__.py
# Copyright (C) 2026 'CHAI CHAIMEE
# Licensed under GNU General Public License. See COPYING.txt for details.

import addonHandler
import globalPluginHandler
from globalVars import appArgs
import gui
import wx
import config
from logHandler import log
from scriptHandler import script
from inputCore import InputGesture
import time

try:
    addonHandler.initTranslation()
except addonHandler.AddonError:
    log.warning("Unable to init translations.")

curAddon = addonHandler.getCodeAddon()
ADDON_SUMMARY = curAddon.manifest['summary']

# Global variables for double-tap detection
_last_tap_time_check = 0
_last_tap_time_manage = 0
_tap_count_check = 0
_tap_count_manage = 0
_double_tap_threshold = 0.3

try:
    from . import CheckDuplicateGestures
    from . import mygesturesManagement
except ImportError:
    import CheckDuplicateGestures
    import mygesturesManagement

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
    scriptCategory = ADDON_SUMMARY

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if appArgs.secure or config.isAppX:
            return
        self.createMenu()

    def createMenu(self):
        """Creates the addon menu under NVDA Tools menu."""
        self.menu = gui.mainFrame.sysTrayIcon.toolsMenu
        self.subMenu = wx.Menu()
        
        item_check = self.subMenu.Append(wx.ID_ANY, _("&Check Duplicate Gestures"))
        gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.onCheckDuplicates, item_check)
        
        item_manage = self.subMenu.Append(wx.ID_ANY, _("&My Gestures Management"))
        gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.onManageUserGestures, item_manage)
        
        self.mainItem = self.menu.AppendSubMenu(self.subMenu, _(ADDON_SUMMARY))

    def terminate(self):
        try:
            if hasattr(self, 'mainItem'):
                self.menu.Remove(self.mainItem)
        except:
            pass
        super().terminate()

    def onCheckDuplicates(self, event):
        """Launch the Duplicate Gestures Dialog."""
        def run():
            try:
                duplicates_data = CheckDuplicateGestures.find_duplicate_gestures_data()
                dlg = CheckDuplicateGestures.DuplicateGesturesDialog(gui.mainFrame, duplicates=duplicates_data)
                dlg.Show()
                dlg.Raise()
                dlg.SetFocus()
            except Exception as e:
                log.error(f"Failed to launch CheckDuplicates: {e}")
        wx.CallAfter(run)

    def onManageUserGestures(self, event):
        """Launch the My Gestures Management Dialog."""
        def run():
            try:
                dlg = mygesturesManagement.MyGesturesManagementDialog(gui.mainFrame)
                dlg.Show()
                dlg.Raise()
                dlg.SetFocus()
            except Exception as e:
                log.error(f"Failed to launch ManageUserGestures: {e}")
        wx.CallAfter(run)

    @script(
        description=_("Check for duplicate input gestures (single tap), My Gestures Management (double tap)"),
        gestures=["kb:windows+shift+g"]
    )
    def script_duplicates(self, gesture):
        global _last_tap_time_check, _tap_count_check
        current_time = time.time()
        
        if current_time - _last_tap_time_check > _double_tap_threshold:
            _tap_count_check = 0
        
        _tap_count_check += 1
        _last_tap_time_check = current_time
        
        def execute_action():
            global _tap_count_check
            if _tap_count_check == 1:
                self.onCheckDuplicates(None)
            elif _tap_count_check >= 2:
                self.onManageUserGestures(None)
            
            _tap_count_check = 0
        
        wx.CallLater(int(_double_tap_threshold * 1000), execute_action)