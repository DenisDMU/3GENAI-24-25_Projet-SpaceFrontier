from Vaisseau import Vaisseau, upgrade_ship
from Planet import Planet
from Player import Player
from Mission import Mission

# Initialisation des planètes
planets = [
    Planet("Terra Nova", "Grande", {"minerai": 50, "carburant": 30}),
    Planet("Zyphera", "Moyenne", {"gaz rare": 20}),
    Planet("Kronos", "Petite", {"cristaux": 10})
]

# Initialisation du joueur
player = Player("Explorateur")
vaisseau = Vaisseau()

# Initialisation des missions
missions = [
    Mission("Explorer une planète", lambda p: len(p.planetes_explorees) > 0, 50),
    Mission("Collecter au moins 30 ressources", lambda p: sum(p.resources.values()) >= 30, 100),
    Mission("Coloniser une planète", lambda p: len(p.colonies) >= 1, 150),
]

def afficher_missions(player):
    """ Affiche les missions et vérifie leur accomplissement """
    print("\n📜 Missions disponibles :")
    for i, mission in enumerate(missions):
        status = "✅ Accomplie" if mission.accomplie else "❌ Non accomplie"
        print(f"{i + 1}. {mission.description} - {status} - Récompense : {mission.recompense} crédits")

def verifier_toutes_les_missions(player):
    """ Vérifie et met à jour toutes les missions après chaque action. """
    for mission in missions:
        mission.verifier_accomplissement(player)


def main():
    print("Bienvenue dans SpaceFrontier!")
    while True:
        print("\nMenu Principal:")
        print("1. Explorer une planète")
        print("2. Collecter des ressources")
        print("3. Coloniser une planète")
        print("4. Améliorer le vaisseau")
        print("5. Afficher statut")
        print("6. Voir les missions")
        print("7. Quitter")

        choix = input("Que voulez-vous faire ? ")

        if choix == "1":
            print("Planètes disponibles pour l'exploration:")
            for i, planet in enumerate(planets):
                print(f"{i + 1}. {planet.name} ({'Colonisée' if planet.colonized else 'Libre'})")
            idx = int(input("Choisissez une planète à explorer : ")) - 1
            if 0 <= idx < len(planets):
                if player.explore(planets[idx]):
                    vaisseau.carburant -= 10
                    verifier_toutes_les_missions(player)  # ✅ Vérification après l'exploration


        elif choix == "2":
            print("Planètes disponibles pour la collecte:")
            for i, planet in enumerate(planets):
                print(f"{i + 1}. {planet.name}")
            idx = int(input("Choisissez une planète pour collecter : ")) - 1
            if 0 <= idx < len(planets):
                player.collect(planets[idx])
                verifier_toutes_les_missions(player)  # ✅ Vérification après l'exploration


        elif choix == "3":
            print("Planètes disponibles pour la colonisation:")
            for i, planet in enumerate(planets):
                print(f"{i + 1}. {planet.name} ({'Colonisée' if planet.colonized else 'Libre'})")
            idx = int(input("Choisissez une planète à coloniser : ")) - 1
            if 0 <= idx < len(planets):
                player.colonize(planets[idx])
                verifier_toutes_les_missions(player)  # ✅ Vérification après l'exploration


        elif choix == "4":
            upgrade_ship(vaisseau)
            verifier_toutes_les_missions(player)  # ✅ Vérification après l'amélioration du vaisseau


        elif choix == "5":
            print(f"Carburant : {vaisseau.carburant}")
            print(f"Ressources : {player.resources}")
            print(f"Colonies : {[p.name for p in player.colonies]}")
            print(f"Crédits : {player.credits}")
            vaisseau.afficher_statistiques()
            verifier_toutes_les_missions(player)  # ✅ Vérification après l'affichage du statut

        elif choix == "6":
            afficher_missions(player)

        elif choix == "76":
            print("Merci d'avoir joué!")
            break

        else:
            print("Choix invalide, essayez encore.")

if __name__ == "__main__":
    main()
