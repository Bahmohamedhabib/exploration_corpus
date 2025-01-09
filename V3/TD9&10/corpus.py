import pandas as pd
import re
from document import Document

class Corpus:
    def __init__(self, nom):
        self.nom = nom
        self.id2doc = {}
        self.ndoc = 0

    def charger_depuis_csv(self, chemin_csv):
        try:
            df = pd.read_csv(chemin_csv, on_bad_lines='skip')
            if df.empty:
                raise ValueError("Le fichier CSV est vide.")
        except Exception as e:
            raise ValueError(f"Erreur lors de la lecture du fichier CSV : {e}")

        for _, row in df.iterrows():
            texte = row.get("Texte", "").strip()
            if not texte:
                continue
            doc = Document(
                titre=row.get("Titre", ""),
                auteur=row.get("Auteur", ""),
                date=row.get("Date", ""),
                texte=texte
            )
            self.add(doc)

    def add(self, doc):
        self.ndoc += 1
        self.id2doc[self.ndoc] = doc

    @staticmethod
    def nettoyer_texte(texte):
        texte = texte.lower()
        texte = texte.replace("\n", " ")
        texte = re.sub(r"[^\w\s]", "", texte)
        texte = re.sub(r"\d+", "", texte)
        return texte