<p align="center">
  <img src="https://www.nvaccess.org/files/nvda/documentation/userGuide/images/nvda.ico" alt="NVDA Logo" width="120">
</p>

# <p align="center">gestureDuplicate</p>

<br>

<p align="center">Identifiziert und verwaltet widersprüchliche Tastenkombinationen und bereinigt Ihre NVDA-Konfiguration.</p>

<br>

<p align="center"><b>Autor:</b> Chai Chaimee</p>
<p align="center"><b>URL:</b> <a href="https://github.com/chaichaimee/gestureDuplicate">https://github.com/chaichaimee/gestureDuplicate</a></p>

---

## Beschreibung
**gestureDuplicate** ist ein professionelles NVDA-Add-on, das entwickelt wurde, um die Integrität und Effizienz der Konfiguration Ihres Screenreaders zu erhalten. Es hilft Ihnen, widersprüchliche Eingabegesten (doppelte Tastenkombinationen) zu identifizieren, benutzerdefinierte Zuweisungen zu verwalten und eine Tiefenreinigung von verbliebenen Konfigurationsdaten deinstallierter Add-ons durchzuführen.

Das Add-on bietet drei wesentliche Wartungswerkzeuge:
* **Doppelte Gesten prüfen** — Erkennt und listet alle doppelten Gesten in allen Kontexten (global, Anwendungsmodule usw.) auf.
* **Meine Gesten-Verwaltung** — Ermöglicht es Ihnen, benutzerdefinierte Gesten anzuzeigen und sicher zu entfernen, die Add-ons zugewiesen sind, die nicht mehr installiert sind.
* **Konfiguration bereinigen (nvda.ini)** — Identifiziert und entfernt veraltete Konfigurationsabschnitte von deinstallierten Add-ons, die sich noch in Ihrer Hauptdatei *nvda.ini* befinden.

> **Wichtig:** Im Laufe der Zeit hinterlässt das Deinstallieren von Add-ons oft "Geister-Einstellungen" in *nvda.ini* und *gestures.ini*. Dies kann zu erhöhtem Speicherverbrauch, Konfigurationskonflikten oder unerwartetem Verhalten führen. Dieses Tool stellt sicher, dass Ihr NVDA schlank und stabil bleibt.

<br>

## Tastenkombinationen
> **Windows + Umschalt + G**
> <br>
> • **Einmal drücken:** Dialog **Doppelte Gesten prüfen** öffnen
> <br>
> • **Zweimal drücken:** Dialog **Meine Gesten-Verwaltung** öffnen
> <br>
> • **Dreimal drücken:** Dialog **Konfiguration bereinigen** öffnen

<br>

**Menüzugriff: NVDA-Menü → Extras → gestureDuplicate →**
* Doppelte Gesten prüfen...
* Benutzerdefinierte Gesten verwalten...
* Konfiguration bereinigen...

<br>

## Funktionen
* **Erkennung doppelter Gesten:** Scannt alle geladenen Zuweisungen (Kern + Add-ons), um funktionale Konflikte zu finden.
* **Intelligente Navigation:** Ein-Klick-Sprung zum Standard-Dialog "Eingaben" von NVDA, wobei das entsprechende Skript zur sofortigen Korrektur bereits ausgewählt ist.
* **Bereinigung von Geister-Gesten:** Zielt speziell auf die *gestures.ini* ab, um Einträge zu finden, die mit fehlenden Add-ons verknüpft sind, und stellt diese zur einfachen Identifizierung grau dar.
* **Erweiterte Konfigurationsreinigung:** Scannt die primäre *nvda.ini* nach verbliebenen Abschnitten deinstallierter Add-ons und ermöglicht das sichere Löschen veralteter Einstellungen.
* **Sammelaktionen:** Unterstützt das Entfernen einzelner Elemente, aller Gesten für ein bestimmtes Add-on oder das gleichzeitige Löschen aller benutzerdefinierten Add-on-Zuweisungen.
* **Multi-Tap-Workflow:** Schnelles Umschalten zwischen Erkennungs-, Verwaltungs- und Reinigungswerkzeugen mit einer einzigen Tastenkombination.
* **Barrierefreiheit im Fokus:** Alle Dialoge sind vollständig per Tastatur bedienbar mit Unterstützung für Eingabe (Ausführen), Leertaste (Umschalten), Entf (Entfernen) und Esc (Schließen).

<br>

## So bereinigen Sie Ihre Konfiguration
Um die beste Leistung von NVDA zu gewährleisten, befolgen Sie diese Schritte:
1. Öffnen Sie das Tool **Konfiguration bereinigen** (Dreimal **Windows+Umschalt+G** drücken).
2. Überprüfen Sie die Liste der in Ihrer *nvda.ini* gefundenen Abschnitte.
3. Markieren Sie die Kästchen für Add-ons, die Sie bereits deinstalliert haben.
4. Drücken Sie **Ausgewählte entfernen**, um diese Abschnitte sicher aus Ihrer Konfigurationsdatei zu löschen.

> **Empfehlung:** Führen Sie "Meine Gesten-Verwaltung" und "Konfiguration bereinigen" nach jeder größeren Add-on-Bereinigung aus, um potenzielle Konflikte zu vermeiden und Ihre Einstellungen organisiert zu halten.

<br><br>

## Unterstützen Sie mich
Wenn dieses Tool Ihr Leben erleichtert hat, ziehen Sie in Erwägung, das nächste Update mit einer kleinen Spende zu unterstützen.

<br>

[![Support me](https://img.shields.io/badge/Donate-Support%20Me-blue?style=for-the-badge&logo=stripe)](https://buy.stripe.com/dRm9AU1xQ3Ds22N6VK1VK01)

<br>

Ihre Unterstützung bedeutet mir viel. Lassen Sie uns gemeinsam etwas Großartiges aufbauen.

<br>

© 2026 Chai Chaimee NVDA Add-on Veröffentlicht unter GNU