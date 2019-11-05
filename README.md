# token
- Dévellopement:
================
Mettre en place une application accessible par le réseau proposant les services suivants:
- Authentification et management par Token
- Ecritures des saisies utilisiteurs dans un fichier XML ou JSON


- Format du token:
le nom du groupe: exemple "groupe1"
le role: "admin" ou "user"
la signature: md5(role + secret)
le secret se compose de 4 charactère (min, maj, digit)

- Exemple de token:
groupe5.user.059a6fbd574bbac254b6e329cc852cf5

- Détail des fonctionnalités:
ouvrir un port TCP > 10000 et < 10100

lorsqu'un client se connecte fournir le token utilisateur

lorsqu'un client soumet un token utilisateur, vérifier sa validité
- s'il est valide on transmet à l'utilisateur la methode permettant d'écrire dans le fichier XML/JSON ainsi que l'ensemble du fichier XML / JSON
- s'il est valide, on permet l'ecriture des clés valeurs transmisent dans un fichier XML / JSON

lorsqu'un token admin est fourni on vérifie sa validité
la chaine "Admin ok" est renvoyé si le token est valide

Recette:
========

Une fois l'application fonctionnelle, connectez vous sur le même subnet et découvrez les éléments suivants sur les applications disponibles:

- le port sur lequelle l'application est disponible
- récuperation d'un token
- écriture dans le fichier
- injection / DOS sur le fichier
- le secret permettant de générer la signature des tokens
- validation d'un token admin


Choix et implémentation des préconisations
==========================================

une fois les vulnérabilités mises en lumière, choisir, implémenter et recetter les mesures de sécurité



Travail à rendre:
=================

1 CR contenant:

- le code source de l'application
- la preuve et le détail des vulnérabilités découvertes
- les préconisations


Critères d'évaluation:
======================

- Réalisation et sécurisation des fonctionnalités demandés : 10 pts
- Identification des vulnérabilités dans les applications : 8 pts
- Formalisme du rapport: 2 pts

