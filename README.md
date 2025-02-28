# Reconnaissance Faciale avec Tkinter et OpenCV

Ce projet est une application de reconnaissance faciale utilisant `OpenCV`, `face_recognition` et `Tkinter` pour fournir une interface graphique simple et intuitive. L'application détecte les visages en temps réel via une webcam et compare les visages détectés à une image de référence.

## 📌 Fonctionnalités
- Détection de visage en temps réel à l'aide d'OpenCV.
- Chargement et encodage d'une image de référence pour la reconnaissance faciale.
- Comparaison des visages détectés avec l'image de référence.
- Interface utilisateur avec `Tkinter`.
- Affichage des visages reconnus avec un encadrement vert et des visages non reconnus avec un encadrement rouge.

## 🛠️ Installation et Prérequis
### Prérequis
Avant d'exécuter le projet, assurez-vous d'avoir installé les dépendances suivantes :
- Python 3.8+
- OpenCV
- numpy
- Pillow

### Installation
1. Clonez ce dépôt GitHub :
   ```bash
   git clone https://github.com/votre-utilisateur/votre-repo.git
   cd votre-repo
   ```
2. Installez les dépendances requises :
   ```bash
   pip install -r requirements.txt
   ```
3. Assurez-vous que CMake et Visual Studio Build Tools sont installés si vous utilisez Windows.

## 🚀 Utilisation
1. Placez l'image de référence sous le nom `img.png` dans le répertoire du projet.
2. Exécutez le script principal :
   ```bash
   python script.py
   ```
3. L'application s'ouvrira et affichera le flux de la webcam avec la reconnaissance faciale activée.

## 📝 Configuration
Si vous souhaitez utiliser une autre image de référence, remplacez `img.png` par votre propre image et assurez-vous qu'elle est bien chargée dans le script.

## 📌 Remarque
- La reconnaissance faciale fonctionne mieux avec des images bien éclairées et bien cadrées.
- Ajustez les paramètres de seuil si la reconnaissance n'est pas assez précise.

## 📜 Licence
Ce projet est sous licence MIT. Vous êtes libre de l'utiliser, de le modifier et de le distribuer sous les conditions de cette licence.

## 📧 Contact
Pour toute question ou suggestion, n'hésitez pas à ouvrir une issue ou à me contacter.

---
✨ Projet développé avec passion pour la reconnaissance faciale et l'IA. 🚀

