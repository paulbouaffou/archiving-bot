# ArchivingBot

## Description
ArchivingBot est un outil automatique conçu pour détecter des URL sur Wikidata, les archiver via Wikiwix et ajouter les liens archivés aux éléments correspondants sur Wikidata. Il permet d'assurer la pérennité des références en ligne utilisées sur Wikidata.

## Fonctionnalités
- Détection automatique des nouvelles URL ajoutées sur Wikidata.
- Archivage des URL via Wikiwix.
- Ajout automatique des liens archivés dans les déclarations Wikidata.
- Gestion des erreurs et des tentatives de nouvelle soumission en cas d'échec.
- Journalisation des actions effectuées.

## Prérequis
Avant d'installer et d'exécuter le bot, assurez-vous d'avoir les éléments suivants :
- Python 3.6 ou une version plus récente.
- Un compte Wikimedia avec les permissions nécessaires pour modifier Wikidata.
- Pywikibot correctement configuré pour Wikidata.

## Installation
1. Clonez le dépôt :
   ```bash
   git clone https://github.com/votre-repo/archiving_bot.git
   cd archiving_bot
   ```
2. Installez les dépendances requises :
   ```bash
   pip install -r requirements.txt
   ```
3. Configurez Pywikibot en éditant `user-config.py` et en suivant les instructions de [Pywikibot](https://www.mediawiki.org/wiki/Manual:Pywikibot/Installation/fr).

## Configuration
Le fichier `config.py` permet de personnaliser les paramètres du bot. Voici les principales options configurables :
```python
# URL de l'API Wikiwix pour l'archivage
WIKIWIX_API_URL = 'http://archive.wikiwix.com/cache/'

# Nombre d'URL traitées par cycle
BATCH_SIZE = 50

# Nombre de tentatives en cas d'erreur réseau
RETRY_ATTEMPTS = 3

# Fichier de suivi des actions
LOG_FILE = 'archiving_bot.log'
```

## Utilisation
Exécutez le bot avec la commande suivante :
```bash
python bot.py
```

## Structure du projet
Le projet est organisé comme suit :
```
/archiving_bot
├── bot.py            # Logique principale du bot
├── config.py         # Configuration des paramètres
├── utils.py          # Fonctions utilitaires pour les requêtes et le traitement des URL
├── requirements.txt  # Dépendances du projet
├── README.md         # Documentation principale
├── CONTRIBUTING.md   # Guide de contribution pour les développeurs
├── .gitignore        # Fichiers à exclure du dépôt
├── LICENSE           # Licence open source du projet
└── user-config.py    # Configuration de Pywikibot pour Wikidata
```

## Déploiement
Le bot peut être exécuté sur un serveur distant pour fonctionner en continu. Vous pouvez utiliser Toolforge ou un autre environnement adapté aux bots Wikimedia.

## Contribuer
Les contributions sont les bienvenues ! Suivez ces étapes pour proposer des améliorations :
1. Forkez le dépôt.
2. Créez une branche pour votre modification :
   ```bash
   git checkout -b ma-modification
   ```
3. Faites vos modifications et validez-les :
   ```bash
   git commit -am "Ajout d'une nouvelle fonctionnalité"
   ```
4. Poussez vos modifications :
   ```bash
   git push origin ma-modification
   ```
5. Créez une pull request sur GitHub.

Voir [CONTRIBUTING.md](CONTRIBUTING.md) pour plus de détails.

## Licence
Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus d'informations.

## Contact
Pour toute question ou suggestion, ouvrez une issue sur GitHub ou contactez-nous via cette [page de discussion Wikimedia](https://www.wikidata.org/w/index.php?title=User_talk:ArchivingBot&action=edit&redlink=1).
