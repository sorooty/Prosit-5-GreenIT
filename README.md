# Green IT Project

## Description
Ce projet vise à développer un logiciel de gestion énergétique pour un quartier connecté à un réseau urbain intelligent (Smart Grid). L'objectif principal est d'équilibrer dynamiquement l'offre et la demande d'énergie afin d'améliorer l'efficacité énergétique, de minimiser les coûts et d'optimiser l'utilisation des ressources renouvelables.

## Structure du projet
```
green_it_project/
│── main.py           # Code principal : algorithmes + analyse des datasets
│── utils.py          # Fonctions utiles (chargement Excel, génération tests, etc.)
│── analysis.ipynb    # Jupyter Notebook pour les graphiques et comparaisons
│── datasets/         # Dossier contenant tous les fichiers Excel
│    ├── data1.xlsx
│    ├── data2.xlsx
│    └── ...
```

## Objectifs d'apprentissage
- Décrire la complexité d'un algorithme en utilisant la notation Big O.
- Déterminer la complexité temporelle et spatiale d'un algorithme.
- Comparer des résultats théoriques et expérimentaux.
- Comprendre les principes du Green IT et les meilleures pratiques associées.
- Expliquer le fonctionnement des tables de hachage et leur implémentation en Python.

## Contexte
L'équipe doit développer un algorithme performant pour trouver deux valeurs dans une liste de surplus de production énergétique dont la somme correspond à une demande cible. Une approche initiale par force brute (O(n²)) a été testée, mais elle s'est avérée inefficace pour des volumes de données importants. Une solution utilisant des tables de hachage est proposée pour réduire la complexité temporelle à O(n).

## Ressources
- **Données** : `GreenIT_data.zip`
- **Complexité** : Exercices et problèmes d’algorithmique, chapitre 1.
- **Structures de données** : [A Guide to Python Hashmaps](https://example.com).
- **Smart Grid** : Articles sur les réseaux intelligents.
- **Green IT** : Approches de développement logiciel durable.

## Langage utilisé
Python est utilisé pour assurer la compatibilité avec l'environnement de développement.

## Conclusion
Ce projet met en pratique des concepts avancés d'algorithmique et de Green IT pour résoudre un problème réel d'optimisation énergétique dans un contexte de Smart Grid.
