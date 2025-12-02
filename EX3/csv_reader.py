import csv
import os
# Exceptions personnalisées
class CsvException(Exception):
    pass

class FichierIntrouvableException(CsvException):
    pass

class LigneInvalideException(CsvException):
    pass

class PrixNegatifException(CsvException):
    pass
# Fonction pour charger un CSV d'articles
def charger_csv(chemin):
    if not os.path.exists(chemin):
        raise FichierIntrouvableException(f"Fichier introuvable: {chemin}")

    articles = []
    with open(chemin, newline='', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        for i, ligne in enumerate(reader, start=1):
            if not ligne or all(not col.strip() for col in ligne):
                continue  # ignorer lignes vides
            if len(ligne) != 3:
                raise LigneInvalideException(f"Ligne {i} invalide: {ligne}")
            id_, nom, prix_str = ligne
            try:
                prix = float(prix_str)
            except ValueError:
                raise LigneInvalideException(f"Prix non numerique à la ligne {i}: {prix_str}")
            if prix <= 0:
                raise PrixNegatifException(f"Prix negatif ou nul à la ligne {i}: {prix}")
            articles.append({"id": id_, "nom": nom, "prix": prix})
    return articles
