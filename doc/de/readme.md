# gestureDuplicate

<p align="center">
  <img src="https://www.nvaccess.org/files/nvda/documentation/userGuide/images/nvda.ico" alt="NVDA Logo" width="120">
</p>

<p align="center">
  Erkennt und verwaltet kollidierende Tastenkombinationen in Ihrer NVDA-Konfiguration
</p>

<p align="center">
  <strong>Autor:</strong> chai chaimee<br>
  <strong>URL:</strong> <a href="https://github.com/chaichaimee/gestureDuplicate">https://github.com/chaichaimee/gestureDuplicate</a>
</p>

---

## Beschreibung

gestureDuplicate ist eine NVDA-Erweiterung, die Ihnen hilft, kollidierende Eingabegesten (doppelte Tastenkürzel) zu identifizieren und zu verwalten sowie übrig gebliebene benutzerdefinierte Gesten von deinstallierten Erweiterungen in Ihrer NVDA-Konfiguration zu bereinigen.

Die Erweiterung enthält zwei leistungsstarke Werkzeuge:

- **Doppelte Gesten prüfen** — erkennt und listet alle doppelten Gesten in allen Kontexten auf (global, App-Module usw.)
- **Meine Gesten-Verwaltung** — ermöglicht das Anzeigen und sichere Entfernen benutzerdefinierter Gesten, die Erweiterungen zugewiesen sind, die nicht mehr installiert sind

> **Wichtig:**  
> Nach der Deinstallation von Erweiterungen bleiben oft viele benutzerdefinierte Tastenzuweisungen in *gestures.ini* zurück und verursachen Verwirrung oder Konflikte. Diese Erweiterung hilft Ihnen, sie einfach und sicher zu bereinigen.

## Tastenkombinationen

**Windows+Shift+G**

- Einmal tippen → Öffnet den Dialog **Doppelte Gesten prüfen**
- Zweimal tippen → Öffnet den Dialog **Meine Gesten-Verwaltung**

Oder über das Menü:

**NVDA → Extras → gestureDuplicate →**

- Doppelte Gesten prüfen
- Meine Gesten-Verwaltung

## Funktionen

- **Erkennung doppelter Gesten** — scannt alle geladenen Gestenzuordnungen in NVDA (Kern + Erweiterungen)
- Saubere, lesbare Liste mit Geste, Funktionsname und Kontext/Kategorie
- Ein-Klick-Sprung zum standardmäßigen NVDA-Eingabegesten-Dialog mit vorgefiltertem Skriptnamen
- **Verwaltung übrig gebliebener Gesten** von zuvor installierten (jetzt deinstallierten) Erweiterungen
- Zeigt nur Gesten an, die zu Erweiterungen gehören (ignoriert integrierte NVDA-Gesten)
- Grauer Text für Gesten von Erweiterungen, die nicht mehr installiert sind
- Entfernen einzelner Gesten oder Löschen aller Gesten einer bestimmten Erweiterung auf einmal
- **Alles löschen**-Funktion — entfernt benutzerdefinierte Gesten aller Erweiterungen in einem Vorgang
- Unterstützung für Doppeltippen bei Hotkeys für schnelles Wechseln zwischen beiden Werkzeugen
- Vollständig tastaturzugängliche Dialoge (Enter, Delete, Escape-Unterstützung)

> **Empfehlung:**  
> Nach der Deinstallation einer Erweiterung verwenden Sie „Meine Gesten-Verwaltung“, um verbleibende Zuweisungen zu bereinigen und potenzielle Konflikte zu vermeiden.