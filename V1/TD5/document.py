class Document:
    # Classe mère représentant un document générique
    def __init__(self, titre="", auteur="", date="", url="", texte=""):
        self.titre = titre
        self.auteur = auteur
        self.date = date
        self.url = url
        self.texte = texte

    def __str__(self):
        return f"{self.titre}, par {self.auteur}"

    def getType(self):
        # Méthode générique, sera redéfinie par les classes filles
        return "Generic Document"

# ================== Classe RedditDocument ==================
class RedditDocument(Document):
    # Classe fille pour les documents Reddit
    def __init__(self, titre, auteur, date, url, texte, nb_commentaires=0):
        super().__init__(titre, auteur, date, url, texte)  # Appelle le constructeur de la classe mère
        self.nb_commentaires = nb_commentaires  # Attribut spécifique

    def __str__(self):
        # Affichage spécifique aux documents Reddit
        return super().__str__() + f" (Commentaires : {self.nb_commentaires})"

    def getType(self):
        return "Reddit Document"

# ================== Classe ArxivDocument ==================
class ArxivDocument(Document):
    # Classe fille pour les documents Arxiv
    def __init__(self, titre, auteur, date, url, texte, co_auteurs=None):
        super().__init__(titre, auteur, date, url, texte)  # Appelle le constructeur de la classe mère
        self.co_auteurs = co_auteurs or []  # Liste des co-auteurs, par défaut une liste vide

    def __str__(self):
        # Affichage spécifique aux documents Arxiv
        co_auteurs_str = ", ".join(self.co_auteurs)
        return super().__str__() + f" (Co-auteurs : {co_auteurs_str})"

    def getType(self):
        return "Arxiv Document"
