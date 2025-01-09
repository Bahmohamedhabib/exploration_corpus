# Documentation du Projet Python : Exploration et Analyse de Corpus

## Introduction
Ce projet implémente une application d’exploration et d’analyse de corpus à l’aide de Python. L'objectif est de permettre à l'utilisateur de charger deux corpus textuels, d'effectuer des comparaisons, d'analyser les mots-clés sur une frise temporelle, et d'exécuter des requêtes avancées. 

## Fonctionnalités Clés
1. **Chargement des corpus** :
   - Les utilisateurs peuvent charger deux fichiers CSV contenant les documents à analyser.
   - Le système vérifie si les fichiers sont valides et affiche des messages d'erreur en cas de problème.

2. **Comparaison des corpus** :
   - Affiche les mots communs entre les deux corpus.
   - Affiche les mots spécifiques à chaque corpus.

3. **Analyse temporelle** :
   - Permet à l’utilisateur d’entrer un mot ou un groupe de mots et d’analyser leur fréquence au fil du temps.
   - Génère des graphiques pour chaque mot dans les deux corpus.

4. **Requêtes avancées** :
   - Filtrage par auteur, date et mot-clé.
   - Recherche dans les deux corpus avec affichage des résultats contenant l’auteur, la date et un extrait du texte.

5. **Moteur de recherche interne** :
   - Recherche des fréquences de mots dans les deux corpus à l’aide d'une matrice de fréquences de termes (TF).

6. **Interface utilisateur conviviale** :
   - Une interface graphique construite avec Tkinter permet d'interagir facilement avec les différentes fonctionnalités.

## Structure des fichiers

### 1. **td9.py**
Fichier principal de l’application. Il contient :
- La classe `Interface` qui gère l’interface graphique.
- Les méthodes pour charger les corpus, analyser les données et générer des graphiques.

### 2. **corpus.py**
Ce fichier contient la classe `Corpus` qui :
- Charge les documents à partir de fichiers CSV.
- Nettoie les textes des documents pour les rendre exploitables.
- Structure les données avec des attributs comme `auteur`, `date` et `texte`.

### 3. **searchEngine.py**
Contient la classe `SearchEngine` qui :
- Crée une matrice de fréquences de termes (TF) pour les mots des documents.
- Permet une recherche efficace des mots dans les corpus.

### 4. **corpus2.csv**
Un exemple de fichier CSV contenant des documents avec les colonnes suivantes :
- `id`: Identifiant unique du document.
- `auteur`: Auteur du document.
- `date`: Date du document au format `YYYY/MM/DD`.
- `texte`: Contenu textuel du document.

## Dépendances
- **Python 3.10+**
- **pandas** : Pour la manipulation des données.
- **matplotlib** : Pour générer les graphiques.
- **Tkinter** : Pour l’interface graphique.
- **re** : Pour les expressions régulières utilisées dans la recherche de mots.

## Fonctionnement
### 1. Lancement de l’application
Exécutez le fichier principal avec la commande :
```bash
python td9.py
```

### 2. Interface utilisateur
- **Chargement des corpus** : Cliquez sur "Charger Corpus 1" et "Charger Corpus 2" pour importer des fichiers CSV.
- **Comparaison des corpus** : Utilisez les boutons pour afficher les mots communs ou spécifiques.
- **Analyse temporelle** : Entrez un mot ou une liste de mots séparés par des virgules pour générer des graphiques temporels.
- **Requêtes avancées** : Filtrez les documents par auteur, date et mots-clés.
- **Moteur de recherche** : Recherchez un mot dans les deux corpus et affichez les fréquences.

## Améliorations possibles
1. **Export des résultats** :
   - Ajouter une fonctionnalité pour exporter les résultats de l'analyse dans un fichier CSV.

2. **Prise en charge de formats supplémentaires** :
   - Supporter d’autres formats comme JSON ou XML.

3. **Optimisation des performances** :
   - Utiliser des structures de données avancées pour améliorer la vitesse de traitement des grands corpus.

4. **Intelligence artificielle** :
   - Intégrer un modèle NLP (Natural Language Processing) pour des analyses plus avancées.

## Conclusion
Ce projet fournit une base solide pour l’analyse textuelle de corpus. Les fonctionnalités implémentées permettent une exploration approfondie des données textuelles tout en étant facile d’utilisation grâce à une interface graphique intuitive.
