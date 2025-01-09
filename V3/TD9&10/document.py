from datetime import datetime

class Document:
    def __init__(self, titre="", auteur="", date="", texte=""):
        self.titre = titre
        self.auteur = auteur
        self.date = self._validate_date(date)
        self.texte = texte

    def _validate_date(self, date):
        try:
            return datetime.strptime(date, "%Y-%m-%d").date()
        except ValueError:
            return None

    def __str__(self):
        return f"{self.titre}, par {self.auteur} ({self.date})"