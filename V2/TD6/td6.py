from corpus import Corpus
from document import Document

# Création du corpus
corpus = Corpus("Mon Corpus")
corpus.add(Document(titre="Doc1", auteur="Auteur1", date="2024/01/01", texte="Ceci est un exemple de texte car le texte est hyper complexe exemple."))
corpus.add(Document(titre="Doc2", auteur="Auteur2", date="2024/01/02", texte="Un autre exemple avec des mots répétitifs."))

# Recherche
print("Résultats de la recherche :")
print(corpus.search("exemple"))

# Concordancier
print("\nConcordancier :")
concordance = corpus.concorde("exemple")
print(concordance)

# Tableau des fréquences
print("\nTableau de fréquences :")
tableau_freq = corpus.construire_tableau_freq()
print(tableau_freq.head())
