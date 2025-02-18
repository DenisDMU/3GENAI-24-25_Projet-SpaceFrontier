import random
import time
import sys

class Planet:
    def __init__(self, name, size, resources):
        self.name = name
        self.size = size
        self.resources = resources
        self.colonized_sectors = 0
        self.max_sectors = 4
        self.colonization_type = None
        self.is_being_colonized = False

    def collect_resources(self):
        if self.resources:
            collected = self.resources.copy()
            self.resources = {}
            return collected
        return {}

    def colonize(self):
        if self.colonized_sectors >= self.max_sectors:
            print(f"\033[1;35m{self.name} est entièrement colonisée ({self.colonization_type}).\033[0m")
            time.sleep(2)
            return False

        if not self.is_being_colonized:
            print("\033[1;34mTypes de colonisation disponibles :\033[0m")
            colonization_types = {"1": "Minière", "2": "Militaire"}
            for key, value in colonization_types.items():
                print(f"{key}. {value}")

            choix = input("Choisissez un type de colonisation : ")
            colonization_type = colonization_types.get(choix)

            if not colonization_type:
                print("\033[1;31mChoix invalide.\033[0m")
                time.sleep(1)
                return True

            self.colonization_type = colonization_type
            self.is_being_colonized = True

        print(f"\n\033[1;36mDémarrage de la colonisation d'un secteur de {self.name} ({self.colonization_type})...\033[0m")
        self.animate_colonization()
        self.colonized_sectors += 1
        print(f"\n\033[1;32mUn secteur de {self.name} a été colonisé ({self.colonized_sectors}/{self.max_sectors}).\033[0m")

        if self.colonized_sectors < self.max_sectors:
            choix = input("Voulez-vous coloniser un autre secteur ? (oui/non) : ")
            if choix.lower() != "oui":
                print(f"\n\033[1;33mVous avez décidé d'arrêter la colonisation de {self.name}. Vous avez colonisé {self.colonized_sectors}/{self.max_sectors} secteurs.\033[0m")
                time.sleep(2)
                return False
            return True
        else:
            print(f"\n\033[1;35m{self.name} a été entièrement colonisée ({self.colonization_type}).\033[0m")
            time.sleep(2)
            return False

    def animate_colonization(self):
        for _ in range(5):
            for frame in ["|", "/", "-", "\\"]:
                sys.stdout.write(f"\rColonisation en cours {frame}")
                sys.stdout.flush()
                time.sleep(0.2)

class Player:
    def __init__(self, name):
        self.name = name
        self.fuel = 100
        self.resources = {}
        self.colonies = []

    def explore(self, planet):
        if self.fuel >= 10:
            self.fuel -= 10
            print(f"\033[1;33mVous explorez la planète {planet.name}.\033[0m")
            time.sleep(1)
            return True
        else:
            print("\033[1;31mCarburant insuffisant pour explorer.\033[0m")
            time.sleep(1)
            return False

    def collect(self, planet):
        if planet.resources:
            collected = planet.collect_resources()
            for key, value in collected.items():
                self.resources[key] = self.resources.get(key, 0) + value
            print(f"\033[1;32mVous avez collecté {collected} de {planet.name}.\033[0m")
        else:
            print(f"\033[1;31mAucune ressource disponible sur {planet.name}.\033[0m")

    def add_colony(self, planet):
        if planet not in self.colonies:
            self.colonies.append(planet)

def planet_menu(planet, player):
    while True:
        print(f"\n\033[1;34mPlanète : {planet.name}")
        print(f"Taille : {planet.size}")
        print(f"Secteurs colonisés : {planet.colonized_sectors}/{planet.max_sectors}")
        if planet.colonization_type:
            print(f"Type de colonisation : {planet.colonization_type}")
        print("\n1. Explorer")
        print("2. Coloniser")
        print("3. Retourner à la liste des planètes\033[0m")

        choix = input("Que souhaitez-vous faire ? ")

        if choix == "1":
            player.explore(planet)
        elif choix == "2":
            while planet.colonize():
                player.add_colony(planet)
                continue
        elif choix == "3":
            break
        else:
            print("\033[1;31mChoix invalide.\033[0m")
            time.sleep(1)

planets = [
    Planet("Terra Nova", "Grande", {"minerai": 50, "carburant": 30}),
    Planet("Zyphera", "Moyenne", {"gaz rare": 20}),
    Planet("Kronos", "Petite", {"cristaux": 10})
]

player = Player("Explorateur")

while True:
    print("\n\033[1;34m=== Liste des Planètes ===")
    for i, planet in enumerate(planets):
        status = "Non colonisée"
        if planet.colonized_sectors > 0:
            status = f"Colonisée ({planet.colonized_sectors}/{planet.max_sectors})"
        print(f"{i + 1}. {planet.name} - {planet.size} - {status}")
    print(f"{len(planets) + 1}. Afficher statut")
    print(f"{len(planets) + 2}. Quitter\033[0m")

    choix = input("\nChoisissez une planète ou une action : ")

    try:
        choix_num = int(choix)
        if 1 <= choix_num <= len(planets):
            planet_menu(planets[choix_num - 1], player)
        elif choix_num == len(planets) + 1:
            print(f"\033[1;34mCarburant : {player.fuel}")
            print(f"Ressources : {player.resources}")
            print(f"Colonies : {[p.name + ' (' + str(p.colonized_sectors) + '/' + str(p.max_sectors) + ' secteurs, ' + str(p.colonization_type) + ')' for p in player.colonies]}\033[0m")
            time.sleep(2)
        elif choix_num == len(planets) + 2:
            break
        else:
            print("\033[1;31mChoix invalide.\033[0m")
            time.sleep(1)
    except ValueError:
        print("\033[1;31mVeuillez entrer un nombre valide.\033[0m")
        time.sleep(1)