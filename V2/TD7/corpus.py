import re
from collections import Counter

class Corpus:
    def __init__(self, nom):
        self.nom = nom
        self.id2doc = {}
        self.ndoc = 0

    def add(self, doc):
        """
        Ajoute un document au corpus.
        """
        self.ndoc += 1
        self.id2doc[self.ndoc] = doc

    @staticmethod
    def nettoyer_texte(texte):
        """
        Nettoie un texte en appliquant diverses transformations.
        """
        texte = texte.lower()
        texte = texte.replace("\n", " ")
        texte = re.sub(r"[^\w\s]", "", texte)
        texte = re.sub(r"\d+", "", texte)
        return texte

    def construire_vocabulaire(self):
        """
        Construit le vocabulaire des mots du corpus.
        """
        vocab = {}
        index = 0
        for doc in self.id2doc.values():
            texte_nettoye = self.nettoyer_texte(doc.texte)
            mots = texte_nettoye.split()
            for mot in mots:
                if mot not in vocab:
                    vocab[mot] = {"id": index, "total_occurrences": 0, "doc_count": 0}
                    index += 1
                vocab[mot]["total_occurrences"] += 1

        # Mise à jour du nombre de documents contenant chaque mot
        for mot in vocab.keys():
            vocab[mot]["doc_count"] = sum(
                1 for doc in self.id2doc.values() if mot in self.nettoyer_texte(doc.texte).split()
            )
        return vocab
