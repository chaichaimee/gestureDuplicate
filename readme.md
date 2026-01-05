<div align="center">

![NVDA Logo](https://github.com/nvaccess/nvda/raw/master/source/NVDA.png)

# gestureDuplicate

Identifies and manages conflicting keyboard shortcuts in your NVDA configuration

</div>

**Author:** Chai Chaimee  
**Repository:** https://github.com/chaichaimee/gestureDuplicate

---

## Description

**gestureDuplicate** is an NVDA add-on that helps you identify and manage **conflicting/duplicate input gestures** (keyboard shortcuts) as well as clean up leftover custom gestures from uninstalled add-ons in your NVDA configuration.

It includes two powerful tools:

- **Check Duplicate Gestures**  
  Scans and lists all duplicate gestures across every context (global, app modules, etc.)

- **My Gestures Management**  
  View and safely remove custom gestures that belong to add-ons which have already been uninstalled

> **Important**  
> After uninstalling add-ons, many custom gesture assignments often remain in `gestures.ini`, causing confusion or conflicts.  
> This add-on helps you clean them up easily and safely.

## Hot Keys

| Shortcut                                   | Action                                          |
|--------------------------------------------|-------------------------------------------------|
| <kbd>Windows</kbd> + <kbd>Shift</kbd> + <kbd>G</kbd> (single tap)   | Open **Check Duplicate Gestures** dialog       |
| <kbd>Windows</kbd> + <kbd>Shift</kbd> + <kbd>G</kbd> (double tap)   | Open **My Gestures Management** dialog         |

Or access via menu:  
**NVDA → Tools → gestureDuplicate →**  
  • Check Duplicate Gestures  
  • My Gestures Management

## Features

- Detects **duplicate gestures** throughout all of NVDA (core + add-ons)
- Clean, readable list showing: gesture • script name • context/category
- One-click jump to NVDA's built-in **Input Gestures** dialog with pre-filtered script name
- Manages **leftover gestures** from previously installed (now uninstalled) add-ons
- Only shows gestures that belong to add-ons (ignores built-in NVDA gestures)
- Gestures from uninstalled add-ons are displayed in **gray text**
- Remove individual gestures or delete all gestures of a specific add-on at once
- **Clear All** function — removes custom gestures from all add-ons in one operation
- Supports **double-tap** on the hotkey for quick switching between both tools
- Fully keyboard accessible dialogs (Enter, Delete, Escape supported)

> **Recommendation**  
> After uninstalling any add-on, always use **My Gestures Management** to clean up remaining assignments and prevent potential conflicts.

---

Feedback, suggestions, bug reports, and pull requests are all very welcome!  
Happy to hear from you on the [Issues page](https://github.com/chaichaimee/gestureDuplicate/issues).