import re

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
        Construit le vocabulaire des mots du corpus par lots.
        """
        batch_size = 5000  # Taille du lot pour le traitement
        vocab = {}

        # Traitement par lots
        for start in range(0, self.ndoc, batch_size):
            end = min(start + batch_size, self.ndoc)
            textes = [self.nettoyer_texte(doc.texte) for doc in list(self.id2doc.values())[start:end]]

            # Construction manuelle du vocabulaire
            for texte in textes:
                mots = texte.split()
                mots_uniques = set(mots)
                for mot in mots_uniques:
                    if mot not in vocab:
                        vocab[mot] = {"id": len(vocab), "total_occurrences": 0, "doc_count": 0}
                    vocab[mot]["total_occurrences"] += mots.count(mot)
                    vocab[mot]["doc_count"] += 1

        return vocab

# Exemple d'utilisation
if __name__ == "__main__":
    class Document:
        def __init__(self, titre="", auteur="", date="", texte=""):
            self.titre = titre
            self.auteur = auteur
            self.date = date
            self.texte = texte

    # Création d'un corpus
    corpus = Corpus("Exemple Corpus")
    corpus.add(Document(titre="Doc1", texte="Ceci est un exemple de document."))
    corpus.add(Document(titre="Doc2", texte="Un autre exemple de texte répétitif."))

    # Construction du vocabulaire
    vocabulaire = corpus.construire_vocabulaire()

    # Affichage du vocabulaire
    print("Vocabulaire construit :")
    for mot, infos in vocabulaire.items():
        print(f"Mot : {mot}, ID : {infos['id']}, Occurrences : {infos['total_occurrences']}, Docs : {infos['doc_count']}")
