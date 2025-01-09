class Document:
    def __init__(self, titre="", auteur="", date="", texte=""):
        self.titre = titre
        self.auteur = auteur
        self.date = date
        self.texte = texte

    def __str__(self):
        return f"{self.titre}, par {self.auteur}"
