import numpy as np
from scipy.sparse import csr_matrix
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
        Construit la matrice sparse des fréquences (TF).
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

        self.mat_TF = csr_matrix((data, (rows, cols)), shape=(self.corpus.ndoc, len(self.vocab)))

    def build_tfidf_matrix(self):
        """
        Construit la matrice sparse TF-IDF manuellement.
        """
        if self.mat_TF is None:
            raise ValueError("La matrice TF n'a pas été construite.")

        N = self.corpus.ndoc
        idf = np.log((N + 1) / (np.array(self.mat_TF.sum(axis=0)).flatten() + 1)) + 1
        tfidf = self.mat_TF.multiply(idf)
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
            doc_vector = tfidf.getrow(doc_id).toarray().flatten()
            similarity = self.cosine_similarity(query_vector, doc_vector)
            results.append((doc_id + 1, self.corpus.id2doc[doc_id + 1].titre, similarity))

        results = sorted(results, key=lambda x: x[2], reverse=True)[:top_n]

        return pd.DataFrame(results, columns=["Document ID", "Titre", "Score"])

# Exemple d'utilisation
if __name__ == "__main__":
    from corpus import Corpus
    from document import Document

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
