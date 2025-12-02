# main.py

from csv_reader import charger_csv, FichierIntrouvableException, LigneInvalideException, PrixNegatifException

if __name__ == "__main__":
    chemin = "articles.csv"
    try:
        articles = charger_csv(chemin)
        for a in articles:
            print(a)
    except FichierIntrouvableException as e:
        print("Erreur:", e)
    except LigneInvalideException as e:
        print("Erreur:", e)
    except PrixNegatifException as e:
        print("Erreur:", e)
