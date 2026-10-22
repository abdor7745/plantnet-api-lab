 🌿 PlantNet API Lab - Client Python & Cloud Computing

Projet de laboratoire réalisé dans le cadre des cours de Cloud Computing et Services SaaS. Ce projet implémente un client Python pour interagir avec l'API de reconnaissance de plantes de **Pl@ntNet**, en mettant l'accent sur la robustesse, la gestion des erreurs réseau et l'analyse des prédictions.

 Fonctionnalités
- **Exploration interactive :** Liste automatiquement les images disponibles dans le dossier local.
- **Sécurité :** Gestion des clés d'API sensibles via un fichier d'environnement (`.env`) ignoré par Git.
- **Top 3 des prédictions :** Affichage des trois meilleures correspondances retournées par l'intelligence artificielle avec leurs scores de confiance.
- **Robustesse et Gestion des Erreurs :**
  - Gestion des erreurs d'authentification (`401`).
  - Gestion des images "hors domaine" ou non reconnues (`404 Species not found`).
  - Gestion des dépassements de délai réseau (`ConnectTimeout` et exceptions `RequestException`).
- **Ergonomie :** Ouverture automatique du dossier d'images ou de l'image sélectionnée à la demande.

 Technologies Utilisées
- **Langage :** Python 3.14+
- **Bibliothèques :** 
  - `requests` (Requêtes HTTP REST / API SaaS)
  - `python-dotenv` (Chargement sécurisé des variables d'environnement)
  - `Pillow` (Manipulation et affichage d'images)
- **Environnement :** VS Code / Terminal Windows (Git & GitHub)

 Installation et Configuration

1. Cloner le dépôt :
   ```bash
   git clone [https://github.com/abdor7745/plantnet-api-lab.git](https://github.com/abdor7745/plantnet-api-lab.git)
   cd plantnet-api-lab
