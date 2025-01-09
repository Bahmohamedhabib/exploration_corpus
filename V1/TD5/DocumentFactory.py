
from document import RedditDocument, ArxivDocument, Document

class DocumentFactory:
    @staticmethod
    def createDocument(doc_type, **kwargs):
        # Méthode pour créer un document basé sur son type
        if doc_type == "Reddit":
            return RedditDocument(**kwargs)
        elif doc_type == "Arxiv":
            return ArxivDocument(**kwargs)
        else:
            return Document(**kwargs)
