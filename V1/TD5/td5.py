# Dans main.py
from corpus import SingletonCorpus
from DocumentFactory import DocumentFactory

# Création d'un corpus unique
corpus = SingletonCorpus.getInstance("Mon Corpus Hérité")
print(corpus)

# Ajout de documents via la Factory
doc1 = DocumentFactory.createDocument(
    "Reddit", 
    titre="Post Reddit", 
    auteur="User123", 
    date="2024/01/01", 
    url="http://reddit.com/post", 
    texte="Ceci est un post Reddit.", 
    nb_commentaires=42
)
corpus.add(doc1)


doc2 = DocumentFactory.createDocument(
    "Arxiv", 
    titre="Article Arxiv", 
    auteur="Auteur Principal", 
    date="2023/12/12", 
    url="https://arxiv.org/search/stat", 
    texte="Résumé de l'article Arxiv.", 
    co_auteurs=["Co-auteur1", "Co-auteur2"]
)
corpus.add(doc2)

# Affichage du corpus
corpus.show()
print(corpus)
