<!DOCTYPE html>
<html lang="fr">
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
        <img src="https://www.nvaccess.org/files/nvda/documentation/userGuide/images/nvda.ico" alt="Logo NVDA" class="nvda-logo">
        <h1>gestureDuplicate</h1>
        <br>
        <p style="text-align: center;">Identifie et gère les conflits de raccourcis clavier et nettoie votre configuration NVDA.</p>
    </div>
    <br>
    <div class="section">
        <p style="text-align: center;"><b>Auteur :</b> Chai Chaimee</p>
        <p style="text-align: center;"><b>URL :</b> <a href="https://github.com/chaichaimee/gestureDuplicate">https://github.com/chaichaimee/gestureDuplicate</a></p>
    </div>
    <hr>
    <div class="section">
        <h2>Description</h2>
        <p><b>gestureDuplicate</b> est une extension NVDA professionnelle conçue pour maintenir la santé et l'efficacité de la configuration de votre lecteur d'écran. Elle vous aide à identifier les gestes d'entrée en conflit (raccourcis en double), à gérer les assignations personnalisées et à effectuer un nettoyage en profondeur des restes de configuration des extensions désinstallées.</p>
        <p>L'extension propose trois outils de maintenance essentiels :</p>
        <ul>
            <li><strong>Vérifier les gestes en double</strong> — Détecte et répertorie tous les gestes en double dans tous les contextes (global, modules d'application, etc.).</li>
            <li><strong>Gestion de mes gestes</strong> — Vous permet de visualiser et de supprimer en toute sécurité les gestes personnalisés assignés aux extensions qui ne sont plus installées.</li>
            <li><strong>Nettoyer la configuration (nvda.ini)</strong> — Identifie et supprime les sections de configuration obsolètes appartenant aux extensions désinstallées qui résident encore dans votre fichier <em>nvda.ini</em> principal.</li>
        </ul>
        <div class="note">
            <strong>Important :</strong> Au fil du temps, la désinstallation d'extensions laisse souvent des paramètres "fantômes" dans <em>nvda.ini</em> et <em>gestures.ini</em>. Cela peut entraîner une consommation accrue de mémoire ou des conflits. Cet outil garde votre NVDA léger et stable.
        </div>
    </div>
    <br>
    <div class="section">
        <h2>Touches de raccourci</h2>
        <div class="hotkey">
            <strong>Windows + Shift + G</strong><br>
            • <b>Appui simple :</b> Ouvrir le dialogue <strong>Vérifier les gestes en double</strong><br>
            • <b>Appui double :</b> Ouvrir le dialogue <strong>Gestion de mes gestes</strong><br>
            • <b>Appui triple :</b> Ouvrir le dialogue <strong>Nettoyer la configuration</strong>
        </div>
        <br>
        <p style="padding-left: 20px;">
            <strong>Accès menu : Menu NVDA → Outils → gestureDuplicate →</strong><br>
                • Vérifier les gestes en double...<br>
                • Gérer les gestes personnalisés...<br>
                • Nettoyer la configuration...
        </p>
    </div>
    <br>
    <div class="section">
        <h2>Fonctionnalités</h2>
        <ul>
            <li class="feature-item"><strong>Détection des gestes en double :</strong> Scanne toutes les assignations chargées (Noyau + Extensions) pour trouver les conflits.</li>
            <li class="feature-item"><strong>Navigation intelligente :</strong> Accès direct au dialogue standard "Gestes de commande" de NVDA avec le script pertinent présélectionné.</li>
            <li class="feature-item"><strong>Nettoyage des gestes fantômes :</strong> Localise les entrées dans <em>gestures.ini</em> liées aux extensions manquantes (affichées en gris).</li>
            <li class="feature-item"><strong>Nettoyage avancé de la configuration :</strong> Scanne le <em>nvda.ini</em> à la recherche de restes d'extensions désinstallées pour les purger en toute sécurité.</li>
            <li class="feature-item"><strong>Actions groupées :</strong> Permet de supprimer des éléments individuels, tous les gestes d'une extension spécifique ou toutes les assignations d'extensions à la fois.</li>
            <li class="feature-item"><strong>Entièrement accessible :</strong> Tous les dialogues sont accessibles au clavier (Entrée, Espace, Suppr, Échap).</li>
        </ul>
    </div>
    <br>
    <div class="section">
        <h2>Comment nettoyer votre configuration</h2>
        <ol>
            <li>Ouvrez l'outil <strong>Nettoyer la configuration</strong> (Appui triple <b>Windows+Shift+G</b>).</li>
            <li>Passez en revue la liste des sections trouvées dans votre <em>nvda.ini</em>.</li>
            <li>Cochez les cases des extensions que vous avez déjà désinstallées.</li>
            <li>Appuyez sur <strong>Supprimer la sélection</strong> pour les effacer en toute sécurité.</li>
        </ol>
    </div>

<br><br>
<h2 style="text-align: center;">Soutenir le projet</h2>
    <p style="text-align: center;">Si <b>gestureDuplicate</b> a amélioré votre quotidien avec NVDA, merci d'envisager de soutenir son développement.</p>
    <p style="text-align: center;">
        <strong><a href="https://github.com/chaichaimee/gestureDuplicate">Visitez le dépôt sur GitHub</a></strong>
    </p>
    <br>
    <p style="text-align: center; font-size: 0.8em; color: #7f8c8d;">&copy; 2026 Chai Chaimee • Sous licence GNU GPL v2+</p>
</div>
</body>
</html>