
# Modernisation d’un backend existant – Docker, Tests et CI/CD

## Description
Ce projet montre la modernisation d’un backend FastAPI initialement simple et non conteneurisé, en une version plus professionnelle incluant Docker, des tests automatisés et un pipeline CI/CD GitHub Actions.  
Le but est de démontrer la capacité à reprendre un backend existant, l’améliorer et le rendre plus facile à déployer et à maintenir.

## Structure du projet
```
backend-modernise-via-docker-ci-cd/
├── .gitignore
├── .github/
│   └── workflows/
│       └── ci.yml
├── legacy_api/
│   ├── main.py
│   └── requirements.txt
├── modern_api/
│   ├── Dockerfile
│   ├── __init__.py
│   ├── main.py
│   ├── requirements.txt
│   └── tests/
│       ├── __init__.py
│       └── test_health.py
└── README.md
```

## Version legacy (avant modernisation)
- API FastAPI minimale
- Aucun test
- Pas de Dockerfile
- Pas de pipeline CI/CD
- Démarrage uniquement en local via Uvicorn

## Version modernisée (après amélioration)
- Conteneurisation de l’application via Docker
- Tests automatisés avec Pytest
- Workflow CI/CD GitHub Actions (tests + build Docker)
- Structure de projet plus propre et exploitable
- Lancement possible en local ou via conteneur

## Prérequis
- Python 3
- Docker
- Git
- Pytest

## Exécution de la version legacy
cd legacy_api   
pip install -r requirements.txt  
uvicorn main:app --reload

## Exécution de la version modernisée (en local)
cd modern_api   
pip install -r requirements.txt  
pytest   
uvicorn main:app --reload

## Build Docker de la version modernisée
docker build -t modern-api ./modern_api   
docker run -p 8000:8000 modern-api

## Pipeline CI/CD
Le pipeline CI s’exécute automatiquement à chaque push ou pull request sur la branche `main`.  
Il effectue :
- Installation de Python
- Installation des dépendances
- Exécution des tests
- Construction de l’image Docker

## Objectif de la modernisation
- Démontrer la capacité à reprendre un backend existant
- Appliquer des bonnes pratiques DevOps
- Améliorer la maintenabilité
- Rendre le projet prêt pour la CI/CD
- Fournir une base simple mais professionnelle pour un déploiement futur

## Licence
Libre d’utilisation pour toute expérimentation ou amélioration personnelle.
