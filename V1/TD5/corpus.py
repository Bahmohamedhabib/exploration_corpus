from document import Document, RedditDocument, ArxivDocument

class Corpus:
    def __init__(self, nom):
        self.nom = nom
        self.id2doc = {}  # Index des documents
        self.ndoc = 0  # Compteur de documents

    def add(self, doc):
        # Ajout d'un document au corpus
        self.ndoc += 1
        self.id2doc[self.ndoc] = doc

    def show(self, n_docs=-1, tri="abc"):
        # Affichage des documents triés par titre ou par date
        docs = list(self.id2doc.values())
        if tri == "abc":
            docs = sorted(docs, key=lambda x: x.titre.lower())[:n_docs]
        elif tri == "123":
            docs = sorted(docs, key=lambda x: x.date)[:n_docs]

        for doc in docs:
            print(f"[{doc.getType()}] {doc}")

    def __repr__(self):
        # Représentation textuelle du corpus
        return f"Corpus: {self.nom}, {self.ndoc} documents."
    


class SingletonCorpus:
    _instance = None

    @staticmethod
    def getInstance(nom="Corpus Unique"):
        # Méthode statique pour garantir une instance unique
        if SingletonCorpus._instance is None:
            SingletonCorpus._instance = Corpus(nom)
        return SingletonCorpus._instance

