# Exceptions spécifiques
class ReservationException(Exception):
    def __init__(self, message):
        super().__init__(message)

class CapaciteDepasseeException(ReservationException): pass
class NombreInvalideException(ReservationException): pass
class NomClientInvalideException(ReservationException): pass
# Classe Evenement
class Evenement:
    def __init__(self, nom, capacite):
        self.nom = nom
        self.capacite = capacite
        self.places_reservees = 0

    def reserver(self, nom_client, nb_places):
        if not nom_client.strip():
            raise NomClientInvalideException("Nom du client requis.")
        if nb_places <= 0:
            raise NombreInvalideException("Nombre de places invalide.")
        if self.places_reservees + nb_places > self.capacite:
            raise CapaciteDepasseeException("Capacite depassee.")

        self.places_reservees += nb_places
        print(f"Reservation confirmée pour {nom_client} ({nb_places} places).")

    def afficher(self):
        print(f"Evenement: {self.nom} - {self.places_reservees}/{self.capacite} places reservees")

# Exemple d'utilisation
if __name__ == "__main__":
    try:
        event = Evenement("Concert", 5)
        event.reserver("", 2)
    except ReservationException as e:
        print("Erreur:", e)
