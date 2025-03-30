import pywikibot
from utils import validate_url, get_archived_url, log_activity
from config import BATCH_SIZE

def main():
    site = pywikibot.Site("wikidata", "wikidata")
    repo = site.data_repository()
    
    for item in repo.recentchanges(namespaces=0, total=BATCH_SIZE):
        url = item.get('title')
        if validate_url(url):
            archived_url = get_archived_url(url)
            claim = pywikibot.Claim(repo, 'P1065')  # P1065 = Archive URL
            claim.setTarget(archived_url)
            item.addClaim(claim, summary='Adding an archived link via Wikiwix')
            log_activity(f"URL archivée : {url} -> {archived_url}")

if __name__ == "__main__":
    main()

