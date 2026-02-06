# gestureDuplicate

<p align="center">
  <img src="https://www.nvaccess.org/files/nvda/documentation/userGuide/images/nvda.ico" alt="NVDA Logo" width="120">
</p>

<p align="center">
  Identifie et gère les raccourcis clavier en conflit dans votre configuration NVDA
</p>

<p align="center">
  <strong>auteur :</strong> chai chaimee<br>
  <strong>url :</strong> <a href="https://github.com/chaichaimee/gestureDuplicate">https://github.com/chaichaimee/gestureDuplicate</a>
</p>

---

## Description

gestureDuplicate est une extension NVDA qui vous aide à identifier et gérer les gestes d'entrée en conflit (raccourcis dupliqués) ainsi qu'à nettoyer les gestes personnalisés restants des extensions désinstallées dans votre configuration NVDA.

L'extension inclut deux outils puissants :

- **Vérifier les gestes dupliqués** — détecte et liste tous les gestes dupliqués dans tous les contextes (global, modules d'applications, etc.)
- **Gestion de mes gestes** — vous permet de visualiser et de supprimer en toute sécurité les gestes personnalisés assignés aux extensions qui ne sont plus installées

> **Important :**  
> Après la désinstallation d'extensions, de nombreuses assignations de raccourcis personnalisés restent souvent dans *gestures.ini* causant confusion ou conflits. Cette extension vous aide à les nettoyer facilement et en toute sécurité.

## Raccourcis clavier

**Windows+Shift+G**

- Appui simple → Ouvre la boîte de dialogue **Vérifier les gestes dupliqués**
- Appui double → Ouvre la boîte de dialogue **Gestion de mes gestes**

Ou via le menu :

**NVDA → Outils → gestureDuplicate →**

- Vérifier les gestes dupliqués
- Gestion de mes gestes

## Fonctionnalités

- **Détection de gestes dupliqués** — analyse tous les mappages de gestes chargés dans NVDA (noyau + extensions)
- Liste propre et lisible montrant le geste, le nom de la fonction et le contexte/catégorie
- Saut en un clic vers la boîte de dialogue standard des Gestes d'entrée de NVDA avec nom de script préfiltré
- **Gestion des gestes restants** des extensions précédemment installées (maintenant désinstallées)
- Affiche uniquement les gestes appartenant aux extensions (ignore les gestes intégrés de NVDA)
- Texte gris pour les gestes des extensions qui ne sont plus installées
- Supprimer des gestes individuels ou supprimer tous les gestes d'une extension spécifique en une seule fois
- **Fonction Tout effacer** — supprime les gestes personnalisés de toutes les extensions en une opération
- Support d'appui double sur les raccourcis pour basculer rapidement entre les deux outils
- Boîtes de dialogue entièrement accessibles au clavier (support Entrée, Suppr, Échap)

> **Recommandation :**  
> Après la désinstallation de toute extension, utilisez « Gestion de mes gestes » pour nettoyer les assignations restantes et prévenir les conflits potentiels.