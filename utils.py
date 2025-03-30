import requests
from config import WIKIWIX_API_URL, LOG_FILE

def validate_url(url):
    """Vérifie si l'URL est valide."""
    return url.startswith("http://") or url.startswith("https://")

def get_archived_url(original_url):
    """Récupère l'URL archivée via Wikiwix."""
    return f'{WIKIWIX_API_URL}{original_url}'

def log_activity(message):
    """Enregistre les activités et erreurs dans un fichier de log."""
    with open(LOG_FILE, 'a') as log_file:
        log_file.write(f"{message}\n")

