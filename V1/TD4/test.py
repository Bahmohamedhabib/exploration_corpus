import csv
import praw
import urllib, urllib.request
import xmltodict
import datetime
from Classes import Document

# Fonction pour sauvegarder les documents dans un fichier CSV
def save_to_csv(filename, documents):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Titre", "Auteur", "Date", "URL", "Texte"])  # En-têtes
        for doc in documents:
            writer.writerow([doc.titre, doc.auteur, doc.date, doc.url, doc.texte])

# Identification Reddit
reddit = praw.Reddit(
    client_id='q9__rfQs5kmGqjBSZYYc-w',
    client_secret='2j92UlcZsFrjY4vYjScVEQ4B5VTY1A',
    user_agent='test pyhtonBah'
)

# Requête Reddit (sous-reddit 'all' pour étendre la recherche)
limit = 100
hot_posts = reddit.subreddit('all').search("coronavirus", limit=limit)
docs_reddit = []

for i, post in enumerate(hot_posts):
    if i % 10 == 0:
        print("Reddit:", i, "/", limit)
    
    # Vérifiez que le texte est non vide ; sinon, remplacez par le titre ou une valeur par défaut
    texte = post.selftext.strip() if post.selftext.strip() else f"[Pas de contenu textuel disponible, voir le titre ou le lien.]"
    texte = texte.replace("\n", " ")  # Remplacez les retours à la ligne par des espaces

    titre = post.title.strip().replace("\n", '')  # Le titre est toujours requis
    auteur = str(post.author) if post.author else "Unknown"  # Gestion des auteurs inconnus
    date = datetime.datetime.fromtimestamp(post.created).strftime("%Y/%m/%d")  # Formatage de la date
    url = "https://www.reddit.com/" + post.permalink  # Génération de l'URL du post

    # Créez une instance de Document avec les données disponibles
    doc_classe = Document(titre, auteur, date, url, texte)
    docs_reddit.append(doc_classe)

# Requête ArXiv
query_terms = ["coronavirus"]  # Recherche sur coronavirus
max_results = 100
url = f'http://export.arxiv.org/api/query?search_query=all:{"+".join(query_terms)}&start=0&max_results={max_results}'
data = urllib.request.urlopen(url)
data = xmltodict.parse(data.read().decode('utf-8'))

docs_arxiv = []

for i, entry in enumerate(data["feed"]["entry"]):
    if i % 10 == 0:
        print("ArXiv:", i, "/", max_results)
    titre = entry["title"].replace('\n', '')
    try:
        authors = ", ".join([a["name"] for a in entry["author"]])
    except:
        authors = entry["author"]["name"]
    summary = entry["summary"].replace("\n", "")
    date = datetime.datetime.strptime(entry["published"], "%Y-%m-%dT%H:%M:%SZ").strftime("%Y/%m/%d")
    url = entry["id"]

    doc_classe = Document(titre, authors, date, url, summary)
    docs_arxiv.append(doc_classe)

# Sauvegarde dans des fichiers CSV
save_to_csv("corpus1.csv", docs_reddit)  # Données Reddit
save_to_csv("corpus2.csv", docs_arxiv)  # Données ArXiv

print("Les données concernant le coronavirus ont été sauvegardées dans corpus1.csv (Reddit) et corpus2.csv (ArXiv).")
