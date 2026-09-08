<div align="center">

<img src="https://www.nvaccess.org/files/nvda/documentation/userGuide/images/nvda.ico" alt="NVDA Logo" width="120" style="display: block; margin: 0 auto 20px;" />

# Gesture Duplicate

Find, fix and clean up messy keyboard gesture assignments — before they cause conflicts.

</div>

---

<div align="center">

**author:** chai chaimee  
**url:** [https://github.com/chaichaimee/GestureDuplicate](https://github.com/chaichaimee/GestureDuplicate)

</div>

---

## Introduction

Gesture Duplicate is a housekeeping tool for NVDA's keyboard shortcuts and configuration. Over time, as you install and remove add-ons, your NVDA setup can accumulate two kinds of clutter: keyboard gestures that are assigned to more than one command at once (so only one of them actually fires), and leftover custom gesture entries or configuration sections belonging to add-ons you no longer have installed.

This add-on gives you three simple tools to deal with that clutter: a scanner that finds duplicate gesture assignments and lets you jump straight to fixing them, a manager for custom gestures tied to add-ons, and a cleaner for stray sections left behind in your NVDA settings file. All three are reachable from a single hotkey or from a new submenu in NVDA's Tools menu.

---

### Hot Keys

> **Windows+Shift+G**  
> Single Tap : Check Duplicate Gestures  
> Double Tap : Manage Custom Gestures  
> Triple Tap (or more) : Clean Configuration

> **How the multi-tap works:**  
> Gesture Duplicate uses a single hotkey for all three tools, distinguishing between them by counting how many times you press it in quick succession.
> 
> Each time you press Windows+Shift+G, the add-on checks how long it has been since your last press. If that gap is under 0.4 seconds, your tap is added to a running count for the current "burst"; if more time has passed, the count restarts at 1. After every tap, a 0.4-second timer is (re)armed. If you tap again before the timer fires, the previous timer is cancelled and a fresh one is started, so the add-on keeps waiting as long as you keep tapping.
> 
> Only once the timer finally elapses without a new tap does the add-on act on the total number of taps recorded: 1 tap opens Check Duplicate Gestures, 2 taps opens Manage Custom Gestures, and 3 or more taps opens Clean Configuration.

> **Note:** All three tools are also available at any time from NVDA's **Tools menu → Gesture Duplicate** submenu, as separate menu items: "Check Duplicate Gestures...", "Manage Custom Gestures...", and "Clean Configuration...". This submenu is added automatically when NVDA starts and removed cleanly when the add-on is disabled or NVDA exits.

---

## Features

### 1. Check Duplicate Gestures

This tool scans every gesture currently registered in NVDA — across all add-ons, app modules, and NVDA's own commands — to find any keyboard (or other input) gesture that has been assigned to more than one command. When two commands share the same gesture, only one of them can actually run, which is usually a sign of a conflict you'll want to resolve.

**Step by step:**

1. The add-on asks NVDA's input manager for the complete map of every gesture registered to every script, across every category.

2. Each gesture is "normalized" first — if your keyboard layout name (for example, "desktop") is embedded in the gesture string, it's stripped out, so the same physical key combination is recognized as identical regardless of layout.

3. The add-on counts how many distinct commands use each normalized gesture. Any gesture used by more than one command is flagged as a duplicate.

4. The duplicates are shown in a list dialog with three columns: the human-readable Gesture, the Function (command) it triggers, and the Context (which add-on or application module it belongs to). Duplicates are sorted alphabetically by gesture so related conflicts sit together.

5. Selecting an entry and choosing "Open Input Gestures" (or pressing Enter) closes this dialog and opens NVDA's own Input Gestures dialog, automatically filtered to the conflicting command and with the relevant tree branch expanded and focused, so you can add or remove the gesture immediately without hunting for it.

### 2. Manage Custom Gestures

This tool is aimed specifically at custom gestures that were created for add-ons — the entries NVDA stores in its gestures.ini file. Its main purpose is to clean up gestures left behind for add-ons you've since uninstalled, which otherwise sit in your configuration indefinitely.

**Step by step:**

1. The add-on reads your gestures.ini file directly and collects every custom gesture that belongs to an add-on section (either a global plugin or an application module), ignoring NVDA's own built-in "main"/"run" sections.

2. For each entry it checks whether the owning add-on is still installed on your system. Entries belonging to add-ons that are no longer installed are shown in gray text so they stand out as safe-to-remove clutter.

3. Each gesture is listed with its display text, the function it's mapped to, and the add-on or application it belongs to. A drop-down lets you filter the list down to a single add-on, or show gestures from all add-ons at once.

4. You can check individual entries and click "Remove Checked" to delete just those, or select a specific add-on in the filter and click "Remove addon" to strip every custom gesture belonging to it in one go. "Clear All" removes every custom add-on gesture in the file. Every removal asks for confirmation first.

5. Because NVDA caches gesture mappings in memory for the running session, cleaned-up entries won't fully disappear from NVDA's own view until NVDA restarts. After any successful cleanup, the dialog switches into a "restart required" mode: the Close button is replaced with a "Restart NVDA Now" button (closing the dialog, including via Escape or the window's close box, triggers the same restart) so the change is guaranteed to take effect.

### 3. Clean Configuration

This tool lets you remove whole top-level sections from your NVDA configuration profile (nvda.ini) — for example, leftover settings sections created by add-ons you no longer use.

**Step by step:**

1. The add-on lists every top-level section name currently present in your active NVDA configuration profile, sorted alphabetically, as a checkable list.

2. You check the sections you want to remove (Space toggles a checkbox; Delete also triggers removal) and click "Remove Selected".

3. After you confirm, each selected section is purged in two parts: its stored values are deleted, and its entry in the configuration's validation schema is also removed. Deleting only the stored values isn't enough, since NVDA would otherwise regenerate an empty stub for that section the next time it validates your profile, making it silently reappear.

4. The configuration is saved immediately, and the list refreshes to confirm the sections are gone.

> **Note:** All three tools are defensive by design — every scan and load operation is wrapped so that an unexpected error is logged rather than crashing NVDA, and destructive actions (removing gestures, removing config sections) always ask for confirmation before making changes.

---

## Support Me

If this tool has made your life easier, consider fueling the next update with a small donation.

[![Support me](https://img.shields.io/badge/Donate-Support%20Me-blue?style=for-the-badge&logo=stripe)](https://buy.stripe.com/dRm9AU1xQ3Ds22N6VK1VK01)

Your support means the world. Let's build something great together

&copy; 2026 Chai Chaimee NVDA Add-on Released under GNU GPL