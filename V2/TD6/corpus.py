import re
import pandas as pd
from collections import Counter

class Corpus:
    def __init__(self, nom):
        self.nom = nom
        self.id2doc = {}  # Dictionnaire contenant les documents
        self.ndoc = 0  # Nombre de documents
        self.concatenated_text = None  # Texte concaténé (calculé une seule fois)

    def add(self, doc):
        # Ajoute un document au corpus
        self.ndoc += 1
        self.id2doc[self.ndoc] = doc

    def concatenate_texts(self):
        # Concatène tous les textes dans une seule chaîne
        if self.concatenated_text is None:  # Calculé une seule fois
            self.concatenated_text = " ".join([doc.texte for doc in self.id2doc.values()])
        return self.concatenated_text

    def search(self, keyword):
        """
        Recherche toutes les occurrences d'un mot-clé dans le corpus.
        :param keyword: Mot-clé à chercher
        :return: Liste des passages contenant le mot-clé
        """
        concatenated_text = self.concatenate_texts()
        pattern = re.compile(rf"\b{keyword}\b", re.IGNORECASE)
        matches = pattern.findall(concatenated_text)
        return matches

    def concorde(self, keyword, context_size=20):
        """
        Construit un concordancier pour un mot-clé donné.
        :param keyword: Mot-clé à analyser
        :param context_size: Taille du contexte autour du mot-clé
        :return: DataFrame avec contexte gauche, motif trouvé, contexte droit
        """
        concatenated_text = self.concatenate_texts()
        pattern = re.compile(rf"(.{{0,{context_size}}})\b({keyword})\b(.{{0,{context_size}}})", re.IGNORECASE)
        matches = pattern.findall(concatenated_text)

        # Transformer les résultats en DataFrame
        data = {
            "Contexte Gauche": [match[0].strip() for match in matches],
            "Motif Trouvé": [match[1] for match in matches],
            "Contexte Droit": [match[2].strip() for match in matches],
        }
        return pd.DataFrame(data)

    @staticmethod
    def nettoyer_texte(texte):
        """
        Nettoie un texte en appliquant diverses transformations.
        :param texte: Chaîne de caractères à nettoyer
        :return: Texte nettoyé
        """
        # Mise en minuscules
        texte = texte.lower()
        # Suppression des sauts de ligne
        texte = texte.replace("\n", " ")
        # Suppression de la ponctuation et des chiffres
        texte = re.sub(r"[^\w\s]", "", texte)  # Supprime la ponctuation
        texte = re.sub(r"\d+", "", texte)  # Supprime les chiffres
        return texte

    def construire_vocabulaire(self):
        """
        Construit un vocabulaire unique à partir des documents du corpus.
        :return: Ensemble des mots uniques
        """
        vocabulaire = set()
        for doc in self.id2doc.values():
            texte_nettoye = self.nettoyer_texte(doc.texte)
            mots = texte_nettoye.split()
            vocabulaire.update(mots)  # Ajoute les mots uniques
        return vocabulaire

    def compter_occurrences(self):
        """
        Compte les occurrences des mots dans le corpus.
        :return: Dictionnaire avec les mots comme clés et leurs occurrences comme valeurs
        """
        compteur = Counter()
        for doc in self.id2doc.values():
            texte_nettoye = self.nettoyer_texte(doc.texte)
            mots = texte_nettoye.split()
            compteur.update(mots)
        return compteur

    def construire_tableau_freq(self):
        """
        Crée un tableau de fréquences des mots dans le corpus.
        :return: DataFrame avec colonnes 'Mot', 'Fréquence', 'Doc Frequency'
        """
        # Comptage des mots
        compteur = self.compter_occurrences()
        # Création du tableau
        data = {
            "Mot": list(compteur.keys()),
            "Fréquence": list(compteur.values()),
        }
        df = pd.DataFrame(data)
        # Tri des mots par fréquence décroissante
        df = df.sort_values(by="Fréquence", ascending=False)

        # Calcul de la fréquence des documents (Doc Frequency)
        df["Doc Frequency"] = df["Mot"].apply(
            lambda mot: sum(1 for doc in self.id2doc.values() if mot in self.nettoyer_texte(doc.texte))
        )
        return df
