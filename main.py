import time
import threading
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
    Mission("Explorer toutes les planètes", lambda p: len(p.planetes_explorees) > 21, 50),
    Mission("Collecter au moins 200 ressources", lambda p: sum(p.resources.values()) >= 200, 100),
    Mission("Coloniser toutes les planètes", lambda p: len(p.colonies) >= 3, 150),
]

def auto_regeneration(planets):
    """ Régénère automatiquement les ressources des planètes toutes les 60 secondes. """
    while True:
        time.sleep(60)  # ⏳ Régénération toutes les 60 secondes
        for planet in planets:
            planet.regenerate_resources()

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
        print("2. Améliorer le vaisseau")
        print("3. Afficher statut")
        print("4. Voir les missions")
        print("5. Quitter")

        choix = input("Que voulez-vous faire ? ")

        threading.Thread(target=auto_regeneration, args=(planets,), daemon=True).start()

        if choix == "1":
            # 🔽 Nouveau système : Le joueur choisit une planète et peut ensuite agir dessus
            print("Planètes disponibles pour l'exploration:")
            for i, planet in enumerate(planets):
                print(f"{i + 1}. {planet.name} ({'Colonisée' if planet.colonized else 'Libre'})")
            idx = int(input("Choisissez une planète à explorer : ")) - 1
            if 0 <= idx < len(planets):
                if player.explore(planets[idx]):
                    vaisseau.carburant -= 10
                    verifier_toutes_les_missions(player)

                # 🎮 Nouveau sous-menu : Que faire après avoir exploré ?
                while True:
                    print(f"\nQue voulez-vous faire sur {planets[idx].name} ?")
                    print("1. Collecter des ressources")
                    print("2. Coloniser la planète")
                    print("3. Retour au menu principal")

                    action = input("Votre choix : ")
                    
                    if action == "1":
                        player.collect(planets[idx])
                        verifier_toutes_les_missions(player)
                    elif action == "2":
                        player.colonize(planets[idx])
                        verifier_toutes_les_missions(player)
                    elif action == "3":
                        break  # Retour au menu principal
                    else:
                        print("Choix invalide, essayez encore.")

        elif choix == "2":
            upgrade_ship(vaisseau)
            verifier_toutes_les_missions(player)  # ✅ Vérification après l'amélioration du vaisseau

        elif choix == "3":
            print(f"Carburant : {vaisseau.carburant}")
            print(f"Ressources : {player.resources}")
            print(f"Colonies : {[p.name for p in player.colonies]}")
            print(f"Crédits : {player.credits}")
            vaisseau.afficher_statistiques()
            verifier_toutes_les_missions(player)  # ✅ Vérification après l'affichage du statut

        elif choix == "4":
            afficher_missions(player)  # Juste un affichage, pas besoin de revalider ici

        elif choix == "5":
            print("Merci d'avoir joué!")
            break

        else:
            print("Choix invalide, essayez encore.")

if __name__ == "__main__":
    main()
