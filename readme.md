<p align="center">
  <img src="https://www.nvaccess.org/files/nvda/documentation/userGuide/images/nvda.ico" alt="NVDA Logo" width="100">
</p>

<p align="center">
  <h1><b>gestureDuplicate</b></h1>
</p>

<p align="center">
  <br>
  <b>Identifies conflicting keyboard shortcuts and cleans up your NVDA configuration.</b>
  <br><br>
  <b>Author:</b> Chai Chaimee<br>
  <b>URL:</b> <a href="https://github.com/chaichaimee/gestureDuplicate">https://github.com/chaichaimee/gestureDuplicate</a>
  <br>
</p>

---

## **Description**

**gestureDuplicate** is a professional-grade NVDA add-on designed to maintain the health and efficiency of your screen reader's configuration. It helps you identify conflicting input gestures, manage custom mappings, and perform deep cleaning of leftover configuration data from uninstalled add-ons.

### **The Three Pillars of Maintenance:**

1.  **Check Duplicate Gestures:** Detects and lists all duplicate gestures across all contexts (global, app modules, etc.).
2.  **My Gestures Management:** Allows you to view and safely remove custom gestures assigned to add-ons that are no longer installed.
3.  **Clean Configuration (nvda.ini):** Identifies and removes obsolete configuration sections belonging to uninstalled add-ons.

> [!IMPORTANT]
> Over time, uninstalling add-ons often leaves "ghost" settings in `nvda.ini` and `gestures.ini`. This can lead to increased memory usage or unexpected behavior. This tool ensures your NVDA remains lean and stable.

<br>

## **Hot Keys**

The add-on features a smart **Multi-Tap** system for the primary shortcut:

| Gesture | Action |
| :--- | :--- |
| **Windows + Shift + G** (Single Tap) | Open **Check Duplicate Gestures** dialog |
| **Windows + Shift + G** (Double Tap) | Open **My Gestures Management** dialog |
| **Windows + Shift + G** (Triple Tap) | Open **Clean Configuration** dialog |

> [!TIP]
> You can also access these tools via:
> **NVDA Menu > Tools > gestureDuplicate**

<br>

## **Key Features**

* **Conflict Detection:** Scans all loaded mappings (Core + Add-ons) to find functional conflicts.
* **Intelligent Navigation:** One-click jump to NVDA's standard "Input Gestures" dialog with the relevant script pre-selected.
* **Ghost Gesture Cleanup:** Specifically targets `gestures.ini` to find entries linked to missing add-ons (displayed in gray).
* **Advanced Config Purge:** Scans the primary `nvda.ini` for leftover sections from uninstalled add-ons for safe deletion.
* **Accessibility First:** All dialogs are fully keyboard accessible with support for **Enter** (execute), **Space** (toggle), **Delete** (remove), and **Escape** (close).

<br>

## **How to Clean Your Configuration**

To keep NVDA performing at its best, follow this workflow:

1.  Open the **Clean Configuration** tool (**Triple tap** `Windows+Shift+G`).
2.  Review the list of sections found in your `nvda.ini`.
3.  Check the boxes for add-ons you have already uninstalled.
4.  Press **Remove Selected** to safely delete those sections.

> [!TIP]
> **Pro Recommendation:** Run "My Gestures Management" and "Clean Configuration" after every major add-on cleanup to prevent potential conflicts.

<br>

## **Support the Project**

If **gestureDuplicate** has improved your productivity or made your NVDA management easier, please consider supporting its continued development.

<p align="center">
  <strong><a href="https://github.com/chaichaimee/gestureDuplicate">Visit the Repository on GitHub</a></strong>
</p>

<br>

<p align="center">
  &copy; 2026 Chai Chaimee • Released under GNU GPL v2+
</p>