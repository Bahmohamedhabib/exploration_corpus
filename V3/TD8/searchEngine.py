import numpy as np
import pandas as pd
from collections import Counter

class SearchEngine:
    def __init__(self, corpus):
        """
        Initialise le moteur de recherche avec un objet Corpus.
        """
        self.corpus = corpus
        self.vocab = self.corpus.construire_vocabulaire()
        self.mat_TF = None
        self.build_tf_matrix()

    def build_tf_matrix(self):
        """
        Construit la matrice TF manuellement.
        """
        rows, cols, data = [], [], []
        for doc_id, doc in self.corpus.id2doc.items():
            texte_nettoye = self.corpus.nettoyer_texte(doc.texte)
            mots = texte_nettoye.split()
            compteur = Counter(mots)

            for mot, freq in compteur.items():
                if mot in self.vocab:
                    rows.append(doc_id - 1)
                    cols.append(self.vocab[mot]["id"])
                    data.append(freq)

        self.mat_TF = np.zeros((self.corpus.ndoc, len(self.vocab)))
        for row, col, value in zip(rows, cols, data):
            self.mat_TF[row, col] = value

    def build_tfidf_matrix(self):
        """
        Construit la matrice TF-IDF manuellement.
        """
        if self.mat_TF is None:
            raise ValueError("La matrice TF n'a pas été construite.")

        N = self.corpus.ndoc
        df = np.sum(self.mat_TF > 0, axis=0)
        idf = np.log((N + 1) / (df + 1)) + 1

        tfidf = self.mat_TF * idf
        return tfidf

    def cosine_similarity(self, vector1, vector2):
        """
        Calcule la similarité cosinus entre deux vecteurs.
        """
        dot_product = np.dot(vector1, vector2)
        norm1 = np.linalg.norm(vector1)
        norm2 = np.linalg.norm(vector2)
        return dot_product / (norm1 * norm2) if norm1 > 0 and norm2 > 0 else 0

    def search(self, query, top_n=5):
        """
        Effectue une recherche sur le corpus.
        """
        mots_query = self.corpus.nettoyer_texte(query).split()
        query_vector = np.zeros(len(self.vocab))
        for mot in mots_query:
            if mot in self.vocab:
                query_vector[self.vocab[mot]["id"]] += 1

        tfidf = self.build_tfidf_matrix()
        results = []

        for doc_id in range(self.corpus.ndoc):
            doc_vector = tfidf[doc_id]
            similarity = self.cosine_similarity(query_vector, doc_vector)
            results.append((doc_id + 1, self.corpus.id2doc[doc_id + 1].titre, similarity))

        results = sorted(results, key=lambda x: x[2], reverse=True)[:top_n]

        return pd.DataFrame(results, columns=["Document ID", "Titre", "Score"])

# Exemple d'utilisation
if __name__ == "__main__":
    from corpus import Corpus
    from document import Document

    # Création d'un corpus
    corpus = Corpus("Discours US")
    corpus.add(Document(titre="Discours 1", auteur="Auteur A", date="2025-01-01", texte="Croissance économique et prospérité."))
    corpus.add(Document(titre="Discours 2", auteur="Auteur B", date="2025-01-02", texte="Développement durable et économie verte."))

    # Initialisation du moteur de recherche
    search_engine = SearchEngine(corpus)

    # Exemple de recherche
    query_test = "économie prospérité"
    results = search_engine.search(query_test, top_n=5)
    print("\nRésultats de la recherche :")
    print(results)
