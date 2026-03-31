<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8">
<title>gestureDuplicate NVDA Add-on</title>
<style>
body { font-family: Arial, sans-serif; line-height: 1.6; padding: 20px; background-color: #f4f4f4; }
.container { max-width: 800px; margin: auto; background: #fff; padding: 20px 40px; border-radius: 8px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
h1, h2, h3 { text-align: center; }
b { font-weight: bold; }
.section { margin-bottom: 30px; }
.nvda-logo { display: block; margin: 0 auto 20px; width: 120px; height: auto; }
.hotkey { background: #f8f9fa; border-left: 4px solid #3498db; padding: 15px; margin: 15px 0; border-radius: 0 4px 4px 0; }
.feature-item { margin: 15px 0; padding-left: 10px; }
.note { background: #fff3cd; border-left: 4px solid #ffc107; padding: 12px; margin: 15px 0; border-radius: 0 4px 4px 0; }
a { color: #3498db; text-decoration: none; }
a:hover { text-decoration: underline; }
</style>
</head>
<body>
<div class="container">
    <div class="section">
        <img src="https://www.nvaccess.org/files/nvda/documentation/userGuide/images/nvda.ico" alt="NVDA Logo" class="nvda-logo">
        <h1>gestureDuplicate</h1>
        <br>
        <p style="text-align: center;">Identifiziert und verwaltet widersprüchliche Tastenkombinationen und bereinigt Ihre NVDA-Konfiguration.</p>
    </div>
    <br>
    <div class="section">
        <p style="text-align: center;"><b>Autor:</b> Chai Chaimee</p>
        <p style="text-align: center;"><b>URL:</b> <a href="https://github.com/chaichaimee/gestureDuplicate">https://github.com/chaichaimee/gestureDuplicate</a></p>
    </div>
    <hr>
    <div class="section">
        <h2>Beschreibung</h2>
        <p><b>gestureDuplicate</b> ist ein professionelles NVDA-Add-on, das entwickelt wurde, um die Stabilität und Effizienz Ihrer Screenreader-Konfiguration zu erhalten. Es hilft Ihnen, widersprüchliche Eingabegesten (doppelte Shortcuts) zu identifizieren, benutzerdefinierte Zuweisungen zu verwalten und eine Tiefenreinigung von Konfigurationsresten deinstallierter Add-ons durchzuführen.</p>
        <p>Das Add-on bietet drei wesentliche Wartungswerkzeuge:</p>
        <ul>
            <li><strong>Doppelte Gesten prüfen</strong> — Erkennt und listet alle doppelten Gesten in allen Kontexten auf (Global, App-Module usw.).</li>
            <li><strong>Eigene Gestenverwaltung</strong> — Ermöglicht es Ihnen, benutzerdefinierte Gesten von nicht mehr installierten Add-ons anzuzeigen und sicher zu entfernen.</li>
            <li><strong>Konfiguration bereinigen (nvda.ini)</strong> — Identifiziert und entfernt veraltete Konfigurationsabschnitte deinstallierter Add-ons, die sich noch in Ihrer <em>nvda.ini</em> befinden.</li>
        </ul>
        <div class="note">
            <strong>Wichtig:</strong> Im Laufe der Zeit hinterlässt das Deinstallieren von Add-ons oft „Geister-Einstellungen“ in <em>nvda.ini</em> und <em>gestures.ini</em>. Dies kann zu erhöhtem Speicherverbrauch oder Konflikten führen. Dieses Tool hält Ihr NVDA schlank und stabil.
        </div>
    </div>
    <br>
    <div class="section">
        <h2>Tastenkombinationen</h2>
        <div class="hotkey">
            <strong>Windows + Shift + G</strong><br>
            • <b>Einmal drücken:</b> Dialog <strong>Doppelte Gesten prüfen</strong> öffnen<br>
            • <b>Zweimal drücken:</b> Dialog <strong>Eigene Gestenverwaltung</strong> öffnen<br>
            • <b>Dreimal drücken:</b> Dialog <strong>Konfiguration bereinigen</strong> öffnen
        </div>
        <br>
        <p style="padding-left: 20px;">
            <strong>Menüzugriff: NVDA-Menü → Extras → gestureDuplicate →</strong><br>
                • Doppelte Gesten prüfen...<br>
                • Eigene Gesten verwalten...<br>
                • Konfiguration bereinigen...
        </p>
    </div>
    <br>
    <div class="section">
        <h2>Funktionen</h2>
        <ul>
            <li class="feature-item"><strong>Erkennung doppelter Gesten:</strong> Scannt alle geladenen Zuweisungen (Core + Add-ons) auf Funktionskonflikte.</li>
            <li class="feature-item"><strong>Intelligente Navigation:</strong> Springt mit einem Klick zum Standard-NVDA-Dialog „Eingaben“ mit vorausgewähltem Skript.</li>
            <li class="feature-item"><strong>Bereinigung von Geister-Gesten:</strong> Findet Einträge in <em>gestures.ini</em>, die mit fehlenden Add-ons verknüpft sind (grau markiert).</li>
            <li class="feature-item"><strong>Erweiterte Konfigurationsreinigung:</strong> Scannt die <em>nvda.ini</em> nach Überresten deinstallierter Add-ons zum sicheren Löschen.</li>
            <li class="feature-item"><strong>Sammelaktionen:</strong> Löschen einzelner Elemente, aller Gesten eines Add-ons oder aller Add-on-Zuweisungen auf einmal.</li>
            <li class="feature-item"><strong>Barrierefreiheit im Fokus:</strong> Alle Dialoge sind vollständig über die Tastatur bedienbar (Enter, Leer, Entf, Esc).</li>
        </ul>
    </div>
    <br>
    <div class="section">
        <h2>So bereinigen Sie Ihre Konfiguration</h2>
        <ol>
            <li>Öffnen Sie das Werkzeug <strong>Konfiguration bereinigen</strong> (Dreimal <b>Windows+Shift+G</b>).</li>
            <li>Prüfen Sie die Liste der Abschnitte in Ihrer <em>nvda.ini</em>.</li>
            <li>Markieren Sie die Boxen für bereits deinstallierte Add-ons.</li>
            <li>Drücken Sie <strong>Ausgewählte entfernen</strong>, um diese sicher zu löschen.</li>
        </ol>
    </div>

<br><br>
<h2 style="text-align: center;">Unterstützen Sie das Projekt</h2>
    <p style="text-align: center;">Wenn <b>gestureDuplicate</b> Ihre NVDA-Verwaltung erleichtert hat, unterstützen Sie bitte die weitere Entwicklung.</p>
    <p style="text-align: center;">
        <strong><a href="https://github.com/chaichaimee/gestureDuplicate">Besuchen Sie das Repository auf GitHub</a></strong>
    </p>
    <br>
    <p style="text-align: center; font-size: 0.8em; color: #7f8c8d;">&copy; 2026 Chai Chaimee • Veröffentlicht unter GNU GPL v2+</p>
</div>
</body>
</html>