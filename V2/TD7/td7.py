from corpus import Corpus
from document import Document
from searchEngine import SearchEngine

# Création d'un corpus
corpus = Corpus("Mon Corpus")
corpus.add(Document(titre="Doc1", auteur="Auteur1", date="2024/01/01", texte="Ceci est un exemple de document."))
corpus.add(Document(titre="Doc2", auteur="Auteur2", date="2024/01/02", texte="Un autre exemple de texte répétitif."))

# Initialisation du moteur de recherche
search_engine = SearchEngine(corpus)

# Requête utilisateur
query = "exemple document"
print("Résultats de recherche :")
print(search_engine.search(query, top_n=3))
