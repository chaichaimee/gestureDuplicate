<p align="center">
  <img src="https://www.nvaccess.org/files/nvda/documentation/userGuide/images/nvda.ico" alt="NVDA Logo" width="120">
</p>

# Gesture Duplicate

Find shortcut conflicts, clear out leftover add-on gestures, and tidy your NVDA configuration, all from one hotkey.

---

**author:** chai chaimee  
**url:** https://github.com/chaichaimee/gestureDuplicate

---

### Introduction

When you install many NVDA add-ons, two of them will sooner or later want the same keyboard shortcut. When that happens, one of the shortcuts silently stops doing what you expect, and it is hard to tell which add-on is responsible. Removing an add-on also does not always remove the shortcuts you assigned to it, so old entries stay behind in your configuration files.

**Gesture Duplicate** solves these problems with three simple tools:

1. **Check Duplicate Gestures** : shows every shortcut that is assigned to more than one function, and takes you straight to NVDA's Input Gestures dialog to fix it.
2. **Manage Custom Gestures** : lists the custom shortcuts that add-ons and applications have saved in your `gestures.ini` file, and lets you remove them, including those left behind by add-ons you have already uninstalled.
3. **Clean Configuration** : lets you browse the sections of your `nvda.ini` file and remove stale sections or individual settings.

All three tools are available from one hotkey, and also from a **Gesture Duplicate** submenu in NVDA's **Tools** menu.

---

### Hot Keys

> **Windows+Shift+G**  
> Single Tap : Check Duplicate Gestures  
> Double Tap : Manage Custom Gestures  
> Triple Tap : Clean Configuration

**How the taps work:**

1. Press **Windows+Shift+G** one or more times in quick succession. Each press must come within 0.4 seconds of the previous one to count as part of the same series.
2. After you stop pressing, the add-on waits 0.4 seconds, then counts the taps.
3. One tap opens Check Duplicate Gestures, two taps open Manage Custom Gestures, and three or more taps open Clean Configuration.

> **Note:** This shortcut appears in NVDA's Input Gestures dialog under the category **Gesture Duplicate**, so you can change it to any key you prefer. The same three tools can also be opened without any hotkey: go to **NVDA menu > Tools > Gesture Duplicate** and choose **Check Duplicate Gestures...**, **Manage Custom Gestures...** or **Clean Configuration...**.

---

### Features

### 1. Check Duplicate Gestures

This tool scans every shortcut that NVDA currently knows about and reports the ones that are assigned to more than one function.

**How it works, step by step:**

1. The add-on reads all gesture mappings that NVDA has registered for the current focus.
2. Each shortcut is normalized by removing the keyboard layout label (for example, the "(desktop)" or "(laptop)" part), so the same key combination is treated as identical in either layout.
3. Exact repeats of the same shortcut, function and source are ignored so that you do not see false conflicts.
4. Every shortcut that is still used by more than one function is collected and sorted alphabetically, so conflicting entries sit next to each other.
5. A dialog called **Duplicate Gestures** opens and announces how many duplicate entries were found.

**The list contains three columns:**

* **Gesture** : the key combination.
* **Function** : the name of the script it triggers.
* **Context** : where the function comes from. For an add-on, the add-on's module name is shown. For an application-specific function, it is shown as "Application: " followed by the application name.

**Fixing a conflict:**

1. Select an entry in the list. The **Open Input Gestures** button becomes available.
2. Press **Enter**, double-click the entry, or activate the button (**Alt+O**).
3. The duplicate list closes and NVDA's own **Input Gestures** dialog opens, already filtered by the name of the selected function.
4. The first item in the tree is expanded and selected, and focus is placed on the tree, so you can move through it with the arrow keys and use the **Add** and **Remove** buttons to change the shortcut.

Press **Escape** or **Close** (**Alt+C**) to leave the dialog.

### 2. Manage Custom Gestures

When you assign or change a shortcut for an add-on or an application, NVDA records it in your `gestures.ini` file. If you later uninstall that add-on, the record stays behind. This tool lets you review and remove those records.

**What it shows:**

1. The add-on opens `gestures.ini` from your NVDA configuration folder.
2. It lists only entries that belong to add-ons (`globalPlugins`) and to applications (`appModules`). NVDA's own built-in sections are not listed. Entries whose function is set to "None" are skipped.
3. Every entry is shown as one line in the form **Gesture | Function | Context**.
4. Entries that belong to an add-on which is no longer installed are marked in gray. Application entries are always treated as installed.

**Filtering by add-on:**

Use the **Addon name** combo box to choose **All addons** or a single add-on. The list then shows only the gestures of that add-on.

**Removing gestures, step by step:**

1. In the list, move to an item and press **Space** to check it. Each change is announced, for example the item text followed by "checked" or "not checked". Pressing **Enter** on an item also toggles its check mark.
2. Press **Delete** or activate the **Remove Checked** button.
3. A confirmation message asks whether you want to remove the selected gestures. Choose Yes to continue.
4. The chosen entries are deleted from `gestures.ini`. If a section becomes empty, the section itself is removed too.

**Removing a whole add-on's gestures:**

When a single add-on is selected in the combo box, the button changes to **Remove addon**. Activating it (or pressing **Delete**) removes **all** custom gestures of that add-on, after you confirm the number of gestures that will be deleted.

**Clear All:**

The **Clear All** button removes every add-on and application gesture shown in this tool, after a warning that tells you how many gestures and how many add-ons are affected. It is disabled when there is nothing to clear.

> **Restart required:** After any successful removal, the dialog announces "Gestures cleaned. Restart NVDA now to apply the changes." The **Close** button is replaced by **Restart NVDA Now** (**Alt+R**) and focus moves to it. Closing the dialog in any way (Escape or the window's close button) also restarts NVDA, because NVDA only fully forgets the old gesture mappings when it starts again.

### 3. Clean Configuration

This tool lets you look inside your `nvda.ini` settings and remove sections that no longer belong to anything, for example settings left behind by an add-on you have uninstalled.

**Step 1: Choose sections**

1. The **Clean NVDA.ini Sections** dialog opens with an alphabetical list of the top-level sections of your base (normal) configuration profile.
2. Each line shows the section name and, when it has content, how many subsections and settings it holds, for example "name (2 subsections, 5 settings)".
3. Press **Space** to check a section. The change is announced.
4. Press **Delete** or activate **Remove Selected**. After you confirm "Delete N sections?", the checked sections are removed and the configuration is saved.
5. Both the stored values and the section's definition are removed, so the section does not come back as an empty entry. Sections you removed during the current session stay hidden from the list.

**Step 2: Choose individual items inside a section**

If you do not want to delete a whole section, open it instead:

1. Focus a section and press **Enter** or activate **Details...**.
2. A new dialog opens, titled with the path to the section, for example "Clean NVDA.ini: sectionName".
3. Subsections are listed first, followed by individual settings. Each setting is shown as `name = value`, and long values are shortened to 40 characters followed by "...".
4. Check the items you want to remove and press **Delete** or **Remove Selected**, then confirm.
5. Only the stored values are removed, and the configuration is saved. Removed settings simply return to their default values.
6. To go deeper, focus a subsection and press **Enter** again. The title shows the full path, with each level separated by " > ".
7. When you close a details dialog, the list behind it refreshes and keeps your position.

**Messages you may hear:**

* "No items selected." : you pressed delete without checking anything.
* "No item focused." : nothing was focused when you opened details.
* "This section has no items to choose from." : the section is empty.
* "This item has no subsections." : you pressed Enter on a plain setting.
* "Removed successfully." : the deletion finished and was saved.

> **Caution:** Changes made in this tool are saved to your NVDA configuration immediately after you confirm. Remove only sections and settings that you recognize as leftovers, and consider keeping a backup copy of your `nvda.ini` file before cleaning.

### 4. Tools Menu Integration

When NVDA starts, the add-on adds a **Gesture Duplicate** submenu at the end of the **Tools** menu. It contains **Check Duplicate Gestures...**, **Manage Custom Gestures...** and **Clean Configuration...**, which open the same three tools described above. The submenu is removed again when the add-on is unloaded or NVDA exits.

### 5. Dialog Behavior

All dialogs stay on top of other windows, so they are not hidden behind the application you were using (such as File Explorer). Every dialog can be closed with **Escape**.

---

## Support Me

If this tool has made your life easier, consider fueling the next update with a small donation.

[![Support me](https://img.shields.io/badge/Donate-Support%20Me-blue?style=for-the-badge&logo=stripe)](https://buy.stripe.com/dRm9AU1xQ3Ds22N6VK1VK01)

Your support means the world. Let's build something great together.

---

&copy; 2026 Chai Chaimee NVDA Add-on Released under GNU GPL