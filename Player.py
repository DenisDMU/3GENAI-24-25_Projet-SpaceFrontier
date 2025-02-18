import time
import sys

class Player:
    def __init__(self, name):
        self.name = name
        self.fuel = 100
        self.resources = {}
        self.colonies = []
        self.credits = 0  # Ajout des crédits
        self.planetes_explorees = []  # ✅ Liste des planètes explorées
    
    def explore(self, planet):
        if self.fuel >= 10:
            self.fuel -= 10
            print(f"Vous explorez la planète {planet.name}.")
            if planet not in self.planetes_explorees:
                self.planetes_explorees.append(planet)  # ✅ Ajouter la planète explorée
            return True
        else:
            print("Carburant insuffisant pour explorer.")
            return False

    def collect(self, planet, amount=5):
        """
        Système de minage interactif :
        - Le joueur choisit une ressource (1, 2, 3...).
        - Il doit appuyer sur Entrée pour chaque extraction.
        - Le minage prend 5 secondes par cycle.
        - Si la planète est colonisée, les ressources minées sont doublées.
        - Il peut arrêter à tout moment.
        """

        if not planet.resources:
            print(f"{planet.name} n'a plus de ressources disponibles.")
            return

        while True:
            print(f"\n🌍 {planet.name} - Ressources disponibles :")
            resources_list = list(planet.resources.keys())  

            for i, resource in enumerate(resources_list, 1):
                print(f"   {i}. {resource} ({planet.resources[resource]} unités)")

            choice = input("\nSélectionnez une ressource à collecter ou 'q' pour quitter : ").strip()

            if choice.lower() == 'q':
                break  

            if not choice.isdigit() or int(choice) < 1 or int(choice) > len(resources_list):
                print("❌ Sélection invalide. Veuillez entrer un numéro valide.")
                continue

            chosen_resource = resources_list[int(choice) - 1]

            # 🔥 Appliquer le boost x2 si la planète est colonisée
            boost_factor = 2 if planet.colonized else 1
            to_collect = min(amount * boost_factor, planet.resources[chosen_resource])

            print(f"\n⛏️ Extraction de {to_collect} unités de {chosen_resource} en cours... Attendez 5 secondes.")

            for i in range(5, 0, -1):
                print(f"⏳ {i} secondes restantes...", end="\r", flush=True)
                time.sleep(1)

            planet.resources[chosen_resource] -= to_collect
            self.resources[chosen_resource] = self.resources.get(chosen_resource, 0) + to_collect

            print(f"✅ Extraction terminée ! Vous avez collecté {to_collect} unités de {chosen_resource}.")

            choice = input("Voulez-vous continuer à miner ? (O/n) : ").strip().lower()
            if choice == 'n':
                break

        print(f"🏁 Fin de la collecte sur {planet.name}.")

    def colonize(self, planet):
        if planet.colonize():
            self.colonies.append(planet)
            print(f"Vous avez colonisé {planet.name} !")
            self.increase_production_on_colonization(planet)  # ✅ Ajout du boost de ressources
        else:
            print(f"{planet.name} est déjà colonisée.")
    
    def produce_resources(self):
        for colony in self.colonies:
            for key, value in colony.resources.items():
                self.resources[key] = self.resources.get(key, 0) + (value // 2)

    def increase_production_on_colonization(self, planet):
        """ Augmente les ressources d'une planète colonisée """
        for key, value in planet.resources.items():
            self.resources[key] = self.resources.get(key, 0) + (value // 2)  # 50% de boost
        print(f"\n🚀 Les ressources de {planet.name} sont boostées après colonisation !")