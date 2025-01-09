from corpus import Corpus

class SearchEngine:
    def __init__(self, corpus):
        self.corpus = corpus
        self.vocab = None
        self.mat_TF = None
        self.build_tf_matrix()

    def build_tf_matrix(self):
        textes = [Corpus.nettoyer_texte(doc.texte) for doc in self.corpus.id2doc.values()]
        textes = [texte for texte in textes if texte.strip()]

        if not textes:
            raise ValueError("Le corpus ne contient pas de texte utilisable.")

        self.vocab = set(word for texte in textes for word in texte.split())
        self.mat_TF = {word: [texte.split().count(word) for texte in textes] for word in self.vocab}