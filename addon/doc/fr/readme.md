<p align="center">
  <img src="https://www.nvaccess.org/files/nvda/documentation/userGuide/images/nvda.ico" alt="NVDA Logo" width="120">
</p>

# <p align="center">gestureDuplicate</p>

<br>

<p align="center">Identifie et gère les conflits de raccourcis clavier et nettoie votre configuration NVDA.</p>

<br>

<p align="center"><b>Auteur :</b> Chai Chaimee</p>
<p align="center"><b>URL :</b> <a href="https://github.com/chaichaimee/gestureDuplicate">https://github.com/chaichaimee/gestureDuplicate</a></p>

---

## Description
**gestureDuplicate** est une extension NVDA de qualité professionnelle conçue pour maintenir l'intégrité et l'efficacité de la configuration de votre lecteur d'écran. Elle vous aide à identifier les conflits de gestes de commande (raccourcis en double), à gérer les mappages personnalisés et à effectuer un nettoyage en profondeur des données de configuration résiduelles des extensions désinstallées.

L'extension propose trois outils de maintenance essentiels :
* **Vérifier les gestes en double** — Détecte et liste tous les gestes en double dans tous les contextes (global, modules d'application, etc.).
* **Gestion de mes gestes** — Vous permet de visualiser et de supprimer en toute sécurité les gestes personnalisés assignés aux extensions qui ne sont plus installées.
* **Nettoyer la configuration (nvda.ini)** — Identifie et supprime les sections de configuration obsolètes appartenant à des extensions désinstallées qui résident encore dans votre fichier *nvda.ini* principal.

> **Important :** Au fil du temps, la désinstallation d'extensions laisse souvent des paramètres "fantômes" dans *nvda.ini* et *gestures.ini*. Cela peut entraîner une augmentation de l'utilisation de la mémoire, des conflits de configuration ou des comportements inattendus. Cet outil garantit que votre NVDA reste léger et stable.

<br>

## Touches de raccourci
> **Windows + Maj + G**
> <br>
> • **Appui simple :** Ouvrir la boîte de dialogue **Vérifier les gestes en double**
> <br>
> • **Appui double :** Ouvrir la boîte de dialogue **Gestion de mes gestes**
> <br>
> • **Appui triple :** Ouvrir la boîte de dialogue **Nettoyer la configuration**

<br>

**Accès au menu : Menu NVDA → Outils → gestureDuplicate →**
* Vérifier les gestes en double...
* Gérer les gestes personnalisés...
* Nettoyer la configuration...

<br>

## Caractéristiques
* **Détection des gestes en double :** Analyse tous les mappages chargés (Cœur + Extensions) pour trouver les conflits fonctionnels.
* **Navigation intelligente :** Accès direct en un clic à la boîte de dialogue standard "Gestes de commandes" de NVDA avec le script pertinent présélectionné pour une correction immédiate.
* **Nettoyage des gestes fantômes :** Cible spécifiquement le fichier *gestures.ini* pour trouver les entrées liées à des extensions manquantes, en les affichant en gris pour une identification facile.
* **Nettoyage avancé de la configuration :** Analyse le fichier *nvda.ini* principal à la recherche de sections résiduelles d'extensions désinstallées, vous permettant de "purger" les paramètres obsolètes en toute sécurité.
* **Actions groupées :** Prise en charge de la suppression d'éléments individuels, de tous les gestes pour une extension spécifique, ou de l'effacement de tous les mappages d'extensions personnalisés en une seule fois.
* **Flux de travail multi-appui :** Basculez rapidement entre les outils de détection, de gestion et de nettoyage à l'aide d'une seule touche de raccourci.
* **Axé sur l'accessibilité :** Toutes les boîtes de dialogue sont entièrement accessibles au clavier avec prise en charge de Entrée (exécuter), Espace (basculer), Suppr (supprimer) et Échap (fermer).

<br>

## Comment nettoyer votre configuration
Pour que NVDA conserve ses performances optimales, suivez ces étapes :
1. Ouvrez l'outil **Nettoyer la configuration** (Triple appui **Windows+Maj+G**).
2. Examinez la liste des sections trouvées dans votre *nvda.ini*.
3. Cochez les cases des extensions que vous avez déjà désinstallées.
4. Appuyez sur **Supprimer la sélection** pour effacer en toute sécurité ces sections de votre fichier de configuration.

> **Recommandation :** Exécutez "Gestion de mes gestes" et "Nettoyer la configuration" après chaque nettoyage majeur d'extensions pour éviter les conflits potentiels et garder vos paramètres organisés.

<br><br>

## Me soutenir
Si cet outil vous a facilité la vie, envisagez de soutenir la prochaine mise à jour par un petit don.

<br>

[![Soutenez-moi](https://img.shields.io/badge/Donate-Support%20Me-blue?style=for-the-badge&logo=stripe)](https://buy.stripe.com/dRm9AU1xQ3Ds22N6VK1VK01)

<br>

Votre soutien compte énormément. Construisons quelque chose de grand ensemble.

<br>

© 2026 Extension NVDA de Chai Chaimee publiée sous licence GNU