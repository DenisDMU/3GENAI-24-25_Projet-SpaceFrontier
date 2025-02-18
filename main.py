from Vaisseau import Vaisseau, upgrade_ship
from Planet import Planet
from Player import Player

# Initialisation des planètes
planets = [
    Planet("Terra Nova", "Grande", {"minerai": 50, "carburant": 30}),
    Planet("Zyphera", "Moyenne", {"gaz rare": 20}),
    Planet("Kronos", "Petite", {"cristaux": 10})
]

# Initialisation du joueur
player = Player("Explorateur")
vaisseau = Vaisseau()

def main():
    print("Bienvenue dans SpaceFrontier!")
    while True:
        print("\nMenu Principal:")
        print("1. Explorer une planète")
        print("2. Collecter des ressources")
        print("3. Coloniser une planète")
        print("4. Améliorer le vaisseau")
        print("5. Afficher statut")
        print("6. Quitter")

        choix = input("Que voulez-vous faire ? ")

        if choix == "1":
            print("Planètes disponibles pour l'exploration:")
            for i, planet in enumerate(planets):
                print(f"{i + 1}. {planet.name} ({'Colonisée' if planet.colonized else 'Libre'})")
            idx = int(input("Choisissez une planète à explorer : ")) - 1
            if 0 <= idx < len(planets):
                if player.explore(planets[idx]):
                    vaisseau.carburant -= 10

        elif choix == "2":
            print("Planètes disponibles pour la collecte:")
            for i, planet in enumerate(planets):
                print(f"{i + 1}. {planet.name}")
            idx = int(input("Choisissez une planète pour collecter : ")) - 1
            if 0 <= idx < len(planets):
                player.collect(planets[idx])

        elif choix == "3":
            print("Planètes disponibles pour la colonisation:")
            for i, planet in enumerate(planets):
                print(f"{i + 1}. {planet.name} ({'Colonisée' if planet.colonized else 'Libre'})")
            idx = int(input("Choisissez une planète à coloniser : ")) - 1
            if 0 <= idx < len(planets):
                player.colonize(planets[idx])

        elif choix == "4":
            upgrade_ship(vaisseau)

        elif choix == "5":
            print(f"Carburant : {vaisseau.carburant}")
            print(f"Ressources : {player.resources}")
            print(f"Colonies : {[p.name for p in player.colonies]}")
            vaisseau.afficher_statistiques()

        elif choix == "6":
            print("Merci d'avoir joué!")
            break

        else:
            print("Choix invalide, essayez encore.")

if __name__ == "__main__":
    main()
