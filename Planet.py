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
        self.collected_resources = {}

    def collect_resources(self, player):
        if self.resources:
            collected = self.resources.copy()
            for key, value in collected.items():
                player.resources[key] = player.resources.get(key, 0) + value
            self.resources = {}
            print(f"\033[1;32mVous avez collecté {collected} de {self.name}.\033[0m")
        else:
            print(f"\033[1;31mAucune ressource disponible sur {self.name}.\033[0m")

    def explore(self, vaisseau):
        if vaisseau.carburant >= 10:
            vaisseau.carburant -= 10
            print(f"\033[1;33mVous explorez la planète {self.name}.\033[0m")
            time.sleep(1)
            return True
        else:
            print("\033[1;31mCarburant insuffisant pour explorer.\033[0m")
            time.sleep(1)
            return False

    def colonize(self):
        if self.colonized_sectors >= self.max_sectors:
            print(f"\033[1;35m{self.name} est entièrement colonisée ({self.colonization_type}).\033[0m")
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
                return True

            self.colonization_type = colonization_type
            self.is_being_colonized = True

        print(f"\n\033[1;36mDémarrage de la colonisation d'un secteur de {self.name} ({self.colonization_type})...\033[0m")
        self.animate_colonization()
        self.colonized_sectors += 1
        print(f"\n\033[1;32mUn secteur de {self.name} a été colonisé ({self.colonized_sectors}/{self.max_sectors}).\033[0m")

        if self.colonized_sectors < self.max_sectors:
            choix = input("Voulez-vous coloniser un autre secteur ? (oui/non) : ")
            return choix.lower() == "oui"
        else:
            print(f"\n\033[1;35m{self.name} a été entièrement colonisée ({self.colonization_type}).\033[0m")
            return False

    def animate_colonization(self):
        for _ in range(5):
            for frame in ["|", "/", "-", "\\"]:
                sys.stdout.write(f"\rColonisation en cours {frame}")
                sys.stdout.flush()
                time.sleep(0.2)

    def get_status(self):
        return f"{self.name} ({self.colonized_sectors}/{self.max_sectors} secteurs" + (f", {self.colonization_type})" if self.colonization_type else ")")

    @staticmethod
    def planet_menu(planets, player, vaisseau):
        while True:
            print("\n\033[1;34m=== Liste des Planètes ===")
            for i, planet in enumerate(planets):
                status = "Non colonisée" if planet.colonized_sectors == 0 else f"Colonisée ({planet.colonized_sectors}/{planet.max_sectors})"
                print(f"{i + 1}. {planet.name} - {planet.size} - {status}")
            print(f"{len(planets) + 1}. Retour au menu principal\033[0m")

            choix = input("\nChoisissez une planète : ")

            try:
                choix_num = int(choix)
                if 1 <= choix_num <= len(planets):
                    planet = planets[choix_num - 1]
                    print("\n1. Explorer\n2. Coloniser\n3. Collecter les ressources\n4. Retour\n")
                    action = input("Que souhaitez-vous faire ? : ")

                    if action == "1":
                        planet.explore(vaisseau)
                    elif action == "2":
                        while planet.colonize():
                            continue
                    elif action == "3":
                        planet.collect_resources(player)
                    elif action == "4":
                        continue
                    else:
                        print("\033[1;31mChoix invalide.\033[0m")
                elif choix_num == len(planets) + 1:
                    break
                else:
                    print("\033[1;31mChoix invalide.\033[0m")
            except ValueError:
                print("\033[1;31mVeuillez entrer un nombre valide.\033[0m")
