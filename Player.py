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
        - Le joueur choisit la ressource par un numéro (1, 2, 3...)
        - Il doit appuyer sur Entrée pour chaque extraction.
        - Le minage prend 5 secondes par cycle.
        - Il peut arrêter à tout moment.
        """
        if not planet.resources:
            print(f"{planet.name} n'a plus de ressources disponibles.")
            return

        while True:
            # 🔥 Affichage des ressources disponibles avec un numéro
            print(f"\n🌍 {planet.name} - Ressources disponibles :")
            resources_list = list(planet.resources.keys())  # Convertir en liste indexable
            for i, resource in enumerate(resources_list, 1):
                print(f"   {i}. {resource} ({planet.resources[resource]} unités)")

            # 🔄 Choix du joueur avec un numéro
            choice = input("\nSélectionnez une ressource à collecter (1, 2, 3...) ou 'q' pour quitter : ").strip()

            if choice.lower() == 'q':
                break  # Quitter la collecte

            # Vérifier que l'entrée est un numéro valide
            if not choice.isdigit() or int(choice) < 1 or int(choice) > len(resources_list):
                print("❌ Sélection invalide. Veuillez entrer un numéro valide.")
                continue

            chosen_resource = resources_list[int(choice) - 1]

            # 🔄 Lancer le minage
            print(f"\n⛏️ Extraction de {chosen_resource} en cours... Attendez 5 secondes.")
            for i in range(5, 0, -1):
                print(f"⏳ {i} secondes restantes...", end="\r", flush=True)
                time.sleep(1)
            print("✅ Extraction terminée !        ")  # Efface la ligne précédente

            # Ajouter les ressources collectées au joueur
            to_collect = min(amount, planet.resources[chosen_resource])
            planet.resources[chosen_resource] -= to_collect
            self.resources[chosen_resource] = self.resources.get(chosen_resource, 0) + to_collect

            print(f"✅ Vous avez collecté {to_collect} unités de {chosen_resource}.")

            # 🔥 Demander au joueur s'il veut continuer
            choice = input("Voulez-vous continuer à miner ? (o/n) [O par défaut] : ").strip().lower()
            if choice == 'n':
                break  # Quitter si le joueur dit "n"

        print(f"🏁 Fin de la collecte sur {planet.name}.")

    def colonize(self, planet):
        if planet.colonize():
            self.colonies.append(planet)
            print(f"Vous avez colonisé {planet.name} !")
        else:
            print(f"{planet.name} est déjà colonisée.")
    
    def produce_resources(self):
        for colony in self.colonies:
            for key, value in colony.resources.items():
                self.resources[key] = self.resources.get(key, 0) + (value // 2)
