import tkinter as tk
from tkinter import filedialog, messagebox
from corpus import Corpus
from searchEngine import SearchEngine
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
import time


class Interface:
    def __init__(self, root):
        self.root = root
        self.root.title("Exploration de Corpus - Projet Python")
        self.root.geometry("1000x800")
        self.root.configure(bg="#f7f7f7")
        self.corpus1 = None
        self.corpus2 = None
        self.create_ui()

    def create_ui(self):
        self.create_time_section()
        self.create_load_section()
        self.create_comparison_section()
        self.create_temporal_analysis_section()
        self.create_advanced_query_section()
        self.create_word_count_section()
        self.create_search_section()


    def create_time_section(self):
        frame = tk.LabelFrame(self.root, text="Heure Actuelle", bg="#e8e8e8", padx=10, pady=10)
        frame.pack(fill="x", padx=10, pady=5)

        self.time_label = tk.Label(frame, text="", font=("Helvetica", 14), fg="#333333", bg="#e8e8e8")
        self.time_label.pack()
        self.update_time()

    def update_time(self):
        now = time.strftime("%Y-%m-%d %H:%M:%S")
        self.time_label.config(text=f"Heure Actuelle : {now}")
        self.root.after(1000, self.update_time)

    def create_load_section(self):
        frame = tk.LabelFrame(self.root, text="Chargement des Fichiers", bg="#f0f0f0", padx=10, pady=10)
        frame.pack(fill="x", padx=10, pady=5)

        tk.Button(frame, text="Charger Corpus 1", command=self.load_corpus1, font=("Helvetica", 12),
                  bg="#007BFF", fg="white", bd=0, padx=10, pady=5).grid(row=0, column=0, padx=5, pady=5)
        tk.Button(frame, text="Charger Corpus 2", command=self.load_corpus2, font=("Helvetica", 12),
                  bg="#007BFF", fg="white", bd=0, padx=10, pady=5).grid(row=0, column=1, padx=5, pady=5)

    def create_comparison_section(self):
        self.comparison_frame = tk.LabelFrame(self.root, text="Comparaison des Corpus", bg="#e6f7ff", padx=10, pady=10)
        self.comparison_frame.pack(fill="x", padx=10, pady=5)

        tk.Button(self.comparison_frame, text="Afficher les Mots en Commun", command=self.show_common_words,
                  font=("Helvetica", 12), bg="#28A745", fg="white", bd=0, padx=10, pady=5).pack(pady=5)

        tk.Button(self.comparison_frame, text="Afficher Mots Spécifiques à Corpus 1",
                  command=self.show_specific_words_corpus1, font=("Helvetica", 12), bg="#17A2B8", fg="white",
                  bd=0, padx=10, pady=5).pack(pady=5)

        tk.Button(self.comparison_frame, text="Afficher Mots Spécifiques à Corpus 2",
                  command=self.show_specific_words_corpus2, font=("Helvetica", 12), bg="#17A2B8", fg="white",
                  bd=0, padx=10, pady=5).pack(pady=5)

    def create_temporal_analysis_section(self):
        frame = tk.LabelFrame(self.root, text="Analyse Temporelle", bg="#fff4e6", padx=10, pady=10)
        frame.pack(fill="x", padx=10, pady=5)

        self.keyword_entry = tk.Entry(frame, width=40)
        self.keyword_entry.pack(side="left", padx=5)
        self.keyword_entry.insert(0, "Entrez un ou plusieurs mots (séparés par des virgules)")

        tk.Button(frame, text="Analyser", command=self.analyze_temporal, font=("Helvetica", 12),
                  bg="#FF6347", fg="white", bd=0, padx=10, pady=5).pack(side="left", padx=5)

    def create_advanced_query_section(self):
        frame = tk.LabelFrame(self.root, text="Requêtes Avancées", bg="#e6ffe6", padx=10, pady=10)
        frame.pack(fill="x", padx=10, pady=5)

        tk.Label(frame, text="Auteur:").grid(row=0, column=0, padx=5, pady=5)
        self.author_entry = tk.Entry(frame, width=20)
        self.author_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame, text="Période (AAAA-MM-DD):").grid(row=1, column=0, padx=5, pady=5)
        self.start_date_entry = tk.Entry(frame, width=10)
        self.start_date_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame, text="Mot-clé:").grid(row=2, column=0, padx=5, pady=5)
        self.keyword_query_entry = tk.Entry(frame, width=20)
        self.keyword_query_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Button(frame, text="Filtrer", command=self.advanced_query, font=("Helvetica", 12),
                  bg="#6C757D", fg="white", bd=0, padx=10, pady=5).grid(row=3, column=0, columnspan=3, pady=10)
    


    def create_search_section(self):
        frame = tk.LabelFrame(self.root, text="Moteur de Recherche", bg="#e8e8e8", padx=10, pady=10)
        frame.pack(fill="x", padx=10, pady=5)

        tk.Label(frame, text="Entrez un mot à rechercher :").grid(row=0, column=0, padx=5, pady=5)
        self.search_entry = tk.Entry(frame, width=30)
        self.search_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Button(frame, text="Rechercher", command=self.search_word, font=("Helvetica", 12),
                bg="#007BFF", fg="white", bd=0, padx=10, pady=5).grid(row=0, column=2, padx=5, pady=5)


    def create_word_count_section(self):
        frame = tk.LabelFrame(self.root, text="Nombre de Mots", bg="#fff7e6", padx=10, pady=10)
        frame.pack(fill="x", padx=10, pady=5)

        tk.Button(frame, text="Calculer le Nombre de Mots", command=self.word_count, font=("Helvetica", 12),
                  bg="#FFC107", fg="black", bd=0, padx=10, pady=5).pack(pady=5)

    def load_corpus1(self):
        chemin_csv = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if chemin_csv:
            self.corpus1 = Corpus("Corpus1")
            self.corpus1.charger_depuis_csv(chemin_csv)
            messagebox.showinfo("Succès", "Corpus 1 chargé avec succès.")

    def load_corpus2(self):
        chemin_csv = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if chemin_csv:
            self.corpus2 = Corpus("Corpus2")
            self.corpus2.charger_depuis_csv(chemin_csv)
            messagebox.showinfo("Succès", "Corpus 2 chargé avec succès.")

    def show_common_words(self):
        if not self.corpus1 or not self.corpus2:
            messagebox.showerror("Erreur", "Veuillez charger les deux corpus.")
            return

        search_engine1 = SearchEngine(self.corpus1)
        search_engine2 = SearchEngine(self.corpus2)

        mots_commun = set(search_engine1.vocab).intersection(search_engine2.vocab)

        if mots_commun:
            messagebox.showinfo("Mots en Commun", ", ".join(mots_commun))
        else:
            messagebox.showinfo("Mots en Commun", "Aucun mot en commun trouvé.")

    def show_specific_words_corpus1(self):
        if not self.corpus1 or not self.corpus2:
            messagebox.showerror("Erreur", "Veuillez charger les deux corpus.")
            return

        search_engine1 = SearchEngine(self.corpus1)
        search_engine2 = SearchEngine(self.corpus2)
        mots_specifiques_corpus1 = set(search_engine1.vocab).difference(search_engine2.vocab)

        if mots_specifiques_corpus1:
            messagebox.showinfo("Mots Spécifiques à Corpus 1", ", ".join(mots_specifiques_corpus1))
        else:
            messagebox.showinfo("Mots Spécifiques à Corpus 1", "Aucun mot spécifique trouvé dans Corpus 1.")

    def show_specific_words_corpus2(self):
        if not self.corpus1 or not self.corpus2:
            messagebox.showerror("Erreur", "Veuillez charger les deux corpus.")
            return

        search_engine1 = SearchEngine(self.corpus1)
        search_engine2 = SearchEngine(self.corpus2)
        mots_specifiques_corpus2 = set(search_engine2.vocab).difference(search_engine1.vocab)

        if mots_specifiques_corpus2:
            messagebox.showinfo("Mots Spécifiques à Corpus 2", ", ".join(mots_specifiques_corpus2))
        else:
            messagebox.showinfo("Mots Spécifiques à Corpus 2", "Aucun mot spécifique trouvé dans Corpus 2.")

    def analyze_temporal(self):
        if not self.corpus1 or not self.corpus2:
            messagebox.showerror("Erreur", "Veuillez charger les deux corpus pour l'analyse temporelle.")
            return

        mots = self.keyword_entry.get().split(",")
        mots = [mot.strip().lower() for mot in mots if mot.strip()]
        if not mots:
            messagebox.showerror("Erreur", "Veuillez entrer au moins un mot pour l'analyse.")
            return

        print("Mots recherchés :", mots)  # Débogage

        def process_corpus(corpus, label):
            dates = []
            textes = []
            for doc in corpus.id2doc.values():
                if doc.date and doc.texte:
                    try:
                        # Convertir les dates en précisant le format
                        date = pd.to_datetime(doc.date, format="%Y/%m/%d", errors="coerce")
                        if pd.notnull(date):
                            dates.append(date)
                            textes.append(doc.texte.lower())
                    except Exception as e:
                        print(f"Erreur de conversion de date pour le document {doc}: {e}")

            evolution = {mot: [] for mot in mots}
            for date, texte in zip(dates, textes):
                print(f"Document analysé (date: {date}): {texte[:50]}...")  # Débogage
                for mot in mots:
                    frequency = texte.split().count(mot)  # Recherche par mots séparés
                    evolution[mot].append((date, frequency))
            return evolution

        # Traiter les deux corpus
        evolution_corpus1 = process_corpus(self.corpus1, "Corpus 1")
        evolution_corpus2 = process_corpus(self.corpus2, "Corpus 2")

        # Afficher les graphiques pour chaque mot et corpus
        for mot in mots:
            for corpus_label, evolution in [("Corpus 1", evolution_corpus1), ("Corpus 2", evolution_corpus2)]:
                freq = evolution[mot]
                df = pd.DataFrame(freq, columns=["Date", "Fréquence"])
                df = df.dropna()
                df["Date"] = pd.to_datetime(df["Date"], errors="coerce")  # Assurez-vous que la colonne est bien en datetime
                df = df.set_index("Date")  # Définir la colonne 'Date' comme index
                df = df.resample("M").sum()  # Regrouper par mois

                if df.empty or df["Fréquence"].sum() == 0:
                    print(f"Aucune donnée à tracer pour le mot '{mot}' dans {corpus_label}.")  # Débogage
                    messagebox.showinfo("Info", f"Aucune donnée à tracer pour le mot '{mot}' dans {corpus_label}.")
                    continue

                # Tracer le graphique
                plt.figure()
                df.plot(y="Fréquence", kind="line", legend=False)
                plt.title(f"Évolution temporelle de '{mot}' ({corpus_label})")
                plt.xlabel("Date")
                plt.ylabel("Fréquence")
                plt.grid(True)

        plt.show()



    def advanced_query(self):
        if not self.corpus1 or not self.corpus2:
            messagebox.showerror("Erreur", "Veuillez charger les deux corpus pour effectuer une requête avancée.")
            return

        auteur = self.author_entry.get().strip()
        start_date = self.start_date_entry.get().strip()
        mot_cle = self.keyword_query_entry.get().strip().lower()

        try:
            start_date = datetime.strptime(start_date, "%Y-%m-%d") if start_date else None
        except ValueError:
            messagebox.showerror("Erreur", "Format de date invalide. Utilisez AAAA-MM-DD.")
            return

        # Recherche dans Corpus 1
        resultats_corpus1 = []
        for doc in self.corpus1.id2doc.values():
            if auteur and auteur.lower() not in doc.auteur.lower():
                continue
            if start_date and doc.date and doc.date < start_date:
                continue
            if mot_cle and mot_cle not in doc.texte.lower():
                continue
            resultats_corpus1.append(f"Auteur: {doc.auteur}, Date: {doc.date}, Texte: {doc.texte[:50]}...")

        # Recherche dans Corpus 2
        resultats_corpus2 = []
        for doc in self.corpus2.id2doc.values():
            if auteur and auteur.lower() not in doc.auteur.lower():
                continue
            if start_date and doc.date and doc.date < start_date:
                continue
            if mot_cle and mot_cle not in doc.texte.lower():
                continue
            resultats_corpus2.append(f"Auteur: {doc.auteur}, Date: {doc.date}, Texte: {doc.texte[:50]}...")

        # Formater et afficher les résultats
        resultats = "Résultats dans Corpus 1:\n"
        resultats += "\n".join(resultats_corpus1) if resultats_corpus1 else "Aucun document trouvé dans Corpus 1.\n"
        resultats += "\n\nRésultats dans Corpus 2:\n"
        resultats += "\n".join(resultats_corpus2) if resultats_corpus2 else "Aucun document trouvé dans Corpus 2."

        messagebox.showinfo("Résultats des Requêtes Avancées", resultats)


    def word_count(self):
        if not self.corpus1 and not self.corpus2:
            messagebox.showerror("Erreur", "Veuillez charger au moins un corpus.")
            return

        result = ""
        if self.corpus1:
            mots_corpus1 = sum(len(doc.texte.split()) for doc in self.corpus1.id2doc.values())
            result += f"Nombre de mots dans Corpus 1 : {mots_corpus1}\n"

        if self.corpus2:
            mots_corpus2 = sum(len(doc.texte.split()) for doc in self.corpus2.id2doc.values())
            result += f"Nombre de mots dans Corpus 2 : {mots_corpus2}\n"

        messagebox.showinfo("Nombre de Mots", result)
    def search_word(self):
        mot = self.search_entry.get().strip().lower()
        if not mot:
            messagebox.showerror("Erreur", "Veuillez entrer un mot à rechercher.")
            return

        if not self.corpus1 or not self.corpus2:
            messagebox.showerror("Erreur", "Veuillez charger les deux corpus avant de rechercher un mot.")
            return

        # Recherche dans Corpus 1
        results_corpus1 = [doc for doc in self.corpus1.id2doc.values() if mot in doc.texte.lower()]
        score_corpus1 = sum(doc.texte.lower().split().count(mot) for doc in results_corpus1)

        # Recherche dans Corpus 2
        results_corpus2 = [doc for doc in self.corpus2.id2doc.values() if mot in doc.texte.lower()]
        score_corpus2 = sum(doc.texte.lower().split().count(mot) for doc in results_corpus2)

        # Formater les résultats
        resultats = (f"Score du mot '{mot}' :\n"
                    f"- Corpus 1 : {score_corpus1} occurrences dans {len(results_corpus1)} documents\n"
                    f"- Corpus 2 : {score_corpus2} occurrences dans {len(results_corpus2)} documents")

        # Afficher les résultats dans une boîte de dialogue
        messagebox.showinfo("Résultats de la Recherche", resultats)

        # Afficher les documents contenant le mot (facultatif)
        details = ""
        if results_corpus1:
            details += "Corpus 1:\n" + "\n".join([f"Document: {doc.auteur}, {doc.date}" for doc in results_corpus1]) + "\n\n"
        if results_corpus2:
            details += "Corpus 2:\n" + "\n".join([f"Document: {doc.auteur}, {doc.date}" for doc in results_corpus2])

        if details:
            messagebox.showinfo("Détails des Documents", details)



if __name__ == "__main__":
    root = tk.Tk()
    app = Interface(root)
    root.mainloop()
