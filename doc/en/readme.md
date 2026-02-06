# gestureDuplicate

<p align="center">
  <img src="https://www.nvaccess.org/files/nvda/documentation/userGuide/images/nvda.ico" alt="NVDA Logo" width="120">
</p>

<p align="center">
  Identifies and manages conflicting keyboard shortcuts in your NVDA configuration
</p>

<p align="center">
  <strong>author:</strong> chai chaimee<br>
  <strong>url:</strong> <a href="https://github.com/chaichaimee/gestureDuplicate">https://github.com/chaichaimee/gestureDuplicate</a>
</p>

---

## Description

gestureDuplicate is an NVDA add-on that helps you identify and manage conflicting input gestures (duplicate shortcuts) as well as clean up leftover custom gestures from uninstalled add-ons in your NVDA configuration.

The add-on includes two powerful tools:

- **Check Duplicate Gestures** — detects and lists all duplicate gestures across all contexts (global, app modules, etc.)
- **My Gestures Management** — lets you view and safely remove custom gestures assigned to add-ons that are no longer installed

> **Important:**  
> After uninstalling add-ons, many custom shortcut assignments often remain in *gestures.ini* causing confusion or conflicts. This add-on helps you clean them up easily and safely.

## Hot Keys

**Windows+Shift+G**

- Single tap → Open **Check Duplicate Gestures** dialog
- Double tap → Open **My Gestures Management** dialog

Or via menu:

**NVDA → Tools → gestureDuplicate →**

- Check Duplicate Gestures
- My Gestures Management

## Features

- **Duplicate gesture detection** — scans all loaded gesture mappings in NVDA (core + add-ons)
- Clean, readable list showing gesture, function name, and context/category
- One-click jump to NVDA's standard Input Gestures dialog with pre-filtered script name
- **Management of leftover gestures** from previously installed (now uninstalled) add-ons
- Only shows gestures belonging to add-ons (ignores built-in NVDA gestures)
- Gray text for gestures of add-ons that are no longer installed
- Remove individual gestures or delete all gestures of a specific add-on at once
- **Clear All** function — removes custom gestures from all add-ons in one operation
- Double-tap support on hotkeys for quick switching between both tools
- Fully keyboard accessible dialogs (Enter, Delete, Escape support)

> **Recommendation:**  
> After uninstalling any add-on, use "My Gestures Management" to clean up remaining assignments and prevent potential conflicts.