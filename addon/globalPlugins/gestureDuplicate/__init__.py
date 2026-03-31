# __init__.py
# Copyright (C) 2026 Chai Chaimee
# Licensed under GNU General Public License. See COPYING.txt for details.

import addonHandler
import globalPluginHandler
import gui
import wx
import time
import ui
from scriptHandler import script
from logHandler import log

addonHandler.initTranslation()

# Safe imports for sub-modules
try:
	from . import CleanConfig, CheckDuplicateGestures, mygesturesManagement
except ImportError as e:
	log.error(f"GestureDuplicate sub-modules missing: {e}")
	CleanConfig = CheckDuplicateGestures = mygesturesManagement = None

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	scriptCategory = "Gesture Duplicate"
	_tap_count = 0
	_last_tap_time = 0
	_threshold = 0.4

	# Menu items will be stored to remove them on termination
	_tools_menu_items = []

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self._add_tools_menu()

	def _add_tools_menu(self):
		"""Add a 'Gesture Duplicate' submenu to NVDA's Tools menu."""
		try:
			tools_menu = gui.mainFrame.sysTrayIcon.toolsMenu
			if not tools_menu:
				tools_menu = gui.mainFrame.toolsMenu
			if not tools_menu:
				return

			# Create submenu
			self.gesture_menu = wx.Menu()
			item_check = self.gesture_menu.Append(wx.ID_ANY, _("Check Duplicate Gestures..."))
			self.gesture_menu.Bind(wx.EVT_MENU, self.onCheckDuplicates, item_check)
			item_manage = self.gesture_menu.Append(wx.ID_ANY, _("Manage Custom Gestures..."))
			self.gesture_menu.Bind(wx.EVT_MENU, self.onManageGestures, item_manage)
			item_clean = self.gesture_menu.Append(wx.ID_ANY, _("Clean Configuration..."))
			self.gesture_menu.Bind(wx.EVT_MENU, self.onCleanConfig, item_clean)

			# Insert submenu into Tools menu
			pos = tools_menu.GetMenuItemCount()
			tools_menu.Insert(pos, wx.ID_ANY, _("Gesture Duplicate"), self.gesture_menu)

			# Store for cleanup
			self._tools_menu_items.append(self.gesture_menu)
		except Exception as e:
			log.error(f"Failed to add tools menu: {e}")

	def onCheckDuplicates(self, evt):
		"""Show duplicate gestures dialog."""
		if CheckDuplicateGestures:
			ui.message(_("Checking duplicate gestures..."))
			wx.CallAfter(lambda: CheckDuplicateGestures.DuplicateGesturesDialog(
				gui.mainFrame,
				CheckDuplicateGestures.find_duplicate_gestures_data()
			).Show())

	def onManageGestures(self, evt):
		"""Show gesture management dialog."""
		if mygesturesManagement:
			ui.message(_("Opening gestures management..."))
			wx.CallAfter(lambda: mygesturesManagement.MyGesturesManagementDialog(gui.mainFrame).Show())

	def onCleanConfig(self, evt):
		"""Show clean config dialog."""
		if CleanConfig:
			ui.message(_("Opening clean configuration..."))
			wx.CallAfter(lambda: CleanConfig.CleanConfigDialog(gui.mainFrame).Show())

	@script(
		description=_("Multi-tap: 1=Check, 2=Manage, 3=Clean"),
		category="Gesture Duplicate",
		gestures=["kb:windows+shift+g"]
	)
	def script_multiTap(self, gesture):
		now = time.time()
		if now - self._last_tap_time > self._threshold:
			self._tap_count = 1
		else:
			self._tap_count += 1
		self._last_tap_time = now
		wx.CallLater(int(self._threshold * 1000), self._execute_action, self._tap_count)

	def _execute_action(self, count_at_time):
		if count_at_time != self._tap_count:
			return
		taps = self._tap_count
		self._tap_count = 0

		if taps == 1:
			self.onCheckDuplicates(None)
		elif taps == 2:
			self.onManageGestures(None)
		elif taps >= 3:
			self.onCleanConfig(None)

	def terminate(self):
		# Remove menu items to prevent memory leaks
		for item in self._tools_menu_items:
			try:
				item.Destroy()
			except:
				pass
		self._tools_menu_items.clear()
		super().terminate()