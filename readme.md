<p align="center">
  <img src="https://www.nvaccess.org/files/nvda/documentation/userGuide/images/nvda.ico" alt="NVDA Logo" width="120">
</p>

# <p align="center">gestureDuplicate</p>

<br>

<p align="center">Identifies and manages conflicting keyboard shortcuts and cleans up your NVDA configuration.</p>

<br>

<p align="center"><b>Author:</b> Chai Chaimee</p>
<p align="center"><b>URL:</b> <a href="https://github.com/chaichaimee/gestureDuplicate">https://github.com/chaichaimee/gestureDuplicate</a></p>

---

## Description
**gestureDuplicate** is a professional-grade NVDA add-on designed to maintain the health and efficiency of your screen reader's configuration. It helps you identify conflicting input gestures (duplicate shortcuts), manage custom mappings, and perform deep cleaning of leftover configuration data from uninstalled add-ons.

The add-on provides three essential maintenance tools:
* **Check Duplicate Gestures** — Detects and lists all duplicate gestures across all contexts (global, app modules, etc.).
* **My Gestures Management** — Allows you to view and safely remove custom gestures assigned to add-ons that are no longer installed.
* **Clean Configuration (nvda.ini)** — Identifies and removes obsolete configuration sections belonging to uninstalled add-ons that still reside in your main *nvda.ini* file.

> **Important:** Over time, uninstalling add-ons often leaves "ghost" settings in *nvda.ini* and *gestures.ini*. This can lead to increased memory usage, configuration conflicts, or unexpected behavior. This tool ensures your NVDA remains lean and stable.

<br>

## Hot Keys
> **Windows + Shift + G**
> <br>
> • **Single tap:** Open **Check Duplicate Gestures** dialog
> <br>
> • **Double tap:** Open **My Gestures Management** dialog
> <br>
> • **Triple tap:** Open **Clean Configuration** dialog

<br>

**Menu Access: NVDA Menu → Tools → gestureDuplicate →**
* Check Duplicate Gestures...
* Manage Custom Gestures...
* Clean Configuration...

<br>

## Features
* **Duplicate Gesture Detection:** Scans all loaded mappings (Core + Add-ons) to find functional conflicts.
* **Intelligent Navigation:** One-click jump to NVDA's standard "Input Gestures" dialog with the relevant script pre-selected for immediate fixing.
* **Ghost Gesture Cleanup:** Specifically targets *gestures.ini* to find entries linked to missing add-ons, displaying them in gray for easy identification.
* **Advanced Configuration Cleaning:** Scans the primary *nvda.ini* for leftover sections from uninstalled add-ons, allowing you to "purge" obsolete settings safely.
* **Bulk Actions:** Supports removing individual items, all gestures for a specific add-on, or clearing all custom addon mappings at once.
* **Multi-Tap Workflow:** Rapidly switch between detection, management, and cleaning tools using a single hotkey.
* **Accessibility Focused:** All dialogs are fully keyboard accessible with support for Enter (execute), Space (toggle), Delete (remove), and Escape (close).

<br>

## How to Clean Your Configuration
To keep NVDA performing at its best, follow these steps:
1. Open the **Clean Configuration** tool (Triple tap **Windows+Shift+G**).
2. Review the list of sections found in your *nvda.ini*.
3. Check the boxes for add-ons you have already uninstalled.
4. Press **Remove Selected** to safely delete those sections from your configuration file.

> **Recommendation:** Run "My Gestures Management" and "Clean Configuration" after every major add-on cleanup to prevent potential conflicts and keep your settings organized.

<br><br>

## Support Me
If this tool has made your life easier, consider fueling the next update with a small donation.

<br>

[![Support me](https://img.shields.io/badge/Donate-Support%20Me-blue?style=for-the-badge&logo=stripe)](https://buy.stripe.com/dRm9AU1xQ3Ds22N6VK1VK01)

<br>

Your support means the world. Let's build something great together

<br>

© 2026 Chai Chaimee NVDA Add-on Released under GNU