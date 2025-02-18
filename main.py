from Vaisseau import Vaisseau, upgrade_ship
from Planet import Planet
from Player import Player
from Mission import Mission
import time
import threading

# Définition des couleurs ANSI
RED = '\033[91m'
GREEN = '\033[92m'
BLUE = '\033[94m'
YELLOW = '\033[93m'
RESET = '\033[0m'

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
    Mission("Explorer une planète", lambda p, v: len(p.planetes_explorees) > 0, 20),
    Mission("Collecter au moins 10 ressources", lambda p, v: sum(p.resources.values()) >= 10, 20),
    Mission("Collecter au moins 30 ressources", lambda p, v: sum(p.resources.values()) >= 30, 40),
    Mission("Coloniser une planète", lambda p, v: len(p.colonies) >= 1, 40),
    Mission("Explorer toutes les planètes", lambda p, v: len(p.planetes_explorees) >= len(planets), 50),
    Mission("Collecter au moins 100 ressources", lambda p, v: sum(p.resources.values()) >= 100, 60),
    Mission("Collecter au moins 200 ressources", lambda p, v: sum(p.resources.values()) >= 200, 80),
    Mission("Coloniser toutes les planètes", lambda p, v: len(p.colonies) >= len(planets), 100),
    Mission("Débloquer le modèle Mercenaire", lambda p, v: "Mercenaire" in v.modeles_debloques, 50),
    Mission("Améliorer les moteurs du vaisseau au niveau 5", lambda p, v: v.moteurs >= 5, 80),
    Mission("Augmenter le carburant à 200", lambda p, v: v.carburant >= 200, 100),
    Mission("Explorer 2 planètes différentes", lambda p, v: len(p.planetes_explorees) >= 2, 25),
    Mission("Collecter 15 gaz rare", lambda p, v: p.resources.get("gaz rare", 0) >= 15, 40),
    Mission("Améliorer les scanners du vaisseau au niveau 5", lambda p, v: v.scanners >= 5, 80),
    Mission("Collecter 10 cristaux", lambda p, v: p.resources.get("cristaux", 0) >= 10, 40),
    Mission("Atteindre 300 de carburant", lambda p, v: v.carburant >= 300, 120),
    Mission("Améliorer les armes du vaisseau au niveau 5", lambda p, v: v.armes >= 5, 80),
    Mission("Donner un nom personnalisé au vaisseau", lambda p, v: v.nom != "Vaisseau", 20),
    Mission("Débloquer le modèle Conqueror", lambda p, v: "Conqueror" in v.modeles_debloques, 100),
    Mission("Collecter plus de 500 ressources au total", lambda p, v: sum(p.resources.values()) >= 500, 150),
]

def auto_regeneration(planets):
    """ Régénère automatiquement les ressources des planètes toutes les 60 secondes. """
    while True:
        time.sleep(60)  # ⏳ Régénération toutes les 60 secondes
        for planet in planets:
            planet.regenerate_resources()

def auto_production(player):
    """ Ajoute les ressources des colonies au joueur toutes les 3 minutes """
    while True:
        time.sleep(180)  # Attendre 180 secondes
        player.produce_resources()
        print("\n🏭 Production automatique des colonies ajoutée aux ressources du joueur !")

def afficher_missions(player):
    """ Affiche les missions et vérifie leur accomplissement """
    print("\n📜 Missions disponibles :")
    for i, mission in enumerate(missions):
        status = "✅ Accomplie" if mission.accomplie else "❌ Non accomplie"
        print(f"{i + 1}. {mission.description} - {status} - Récompense : {mission.recompense} crédits")

def verifier_toutes_les_missions(player, vaisseau):
    """ Vérifie et met à jour toutes les missions après chaque action. """
    for mission in missions:
        mission.verifier_accomplissement(player, vaisseau)

def afficher_caracteristiques_planete(planet):
    print(f"{BLUE}\n🌍 Planète sélectionnée : {planet.name} {RESET}")
    print(f"📏 Taille : {planet.size}")
    print("🛠️ Ressources disponibles :")
    for ressource, quantite in planet.resources.items():
        print(f"  - {ressource.capitalize()} : {quantite}")
    print(f"🏠 Colonisée : {'✅ Oui' if planet.colonized else '❌ Non'}")

def barre_de_chargement(duree):
    print("\n🚀 Voyage en cours...", end="", flush=True)
    for _ in range(duree):
        print("🚀", end="", flush=True)
        time.sleep(1)
    print(" ✅ Arrivée !\n")

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
        threading.Thread(target=auto_production, args=(player,), daemon=True).start()

        if choix == "1":
            while True:
                print("Planètes disponibles pour l'exploration:")
                for i, planet in enumerate(planets):
                    print(f"{i + 1}. {planet.name} ({'Colonisée' if planet.colonized else 'Libre'})")
        
                idx = int(input("Choisissez une planète à explorer : ")) - 1
                if 0 <= idx < len(planets):
                    planet = planets[idx]
                    afficher_caracteristiques_planete(planet)
                    confirmation = input("Êtes-vous sûr de vouloir explorer cette planète ? (O/N) : ").lower()
            
                    if confirmation == "o":
                        duree_voyage = min(10, max(1, len(planet.name)))  # Simulation d'une durée basée sur la planète
                        barre_de_chargement(duree_voyage)
                        if player.explore(planet):
                            vaisseau.carburant -= 10
                            verifier_toutes_les_missions(player, vaisseau)
                        break
                    else:
                        print("Retour au choix de la planète.")
                else:
                    print("Choix invalide, essayez encore.")

            while True:
                print(f"\nQue voulez-vous faire sur {planet.name} ?")
                print("1. Collecter des ressources")
                print("2. Coloniser la planète")
                print("3. Retour au menu principal")

                action = input("Votre choix : ")

                if action == "1":
                    player.collect(planet)
                    verifier_toutes_les_missions(player, vaisseau)
                elif action == "2":
                    player.colonize(planet)
                    verifier_toutes_les_missions(player, vaisseau)
                elif action == "3":
                    break
                else:
                    print("Choix invalide, essayez encore.")


        elif choix == "2":
            upgrade_ship(vaisseau)
            verifier_toutes_les_missions(player, vaisseau)

        elif choix == "3":
            print(f"Carburant : {vaisseau.carburant}")
            print(f"Ressources : {player.resources}")
            print(f"Colonies : {[p.name for p in player.colonies]}")
            print(f"Crédits : {player.credits}")
            vaisseau.afficher_statistiques()
            verifier_toutes_les_missions(player, vaisseau)

        elif choix == "4":
            afficher_missions(player)

        elif choix == "5":
            print("Merci d'avoir joué!")
            break

        else:
            print("Choix invalide, essayez encore.")

if __name__ == "__main__":
    main()
