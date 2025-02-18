import random

class Planet:
    def __init__(self, name, size, resources):
        self.name = name
        self.size = size
        self.resources = resources
        self.colonized = False
    
    def collect_resources(self):
        if self.resources:
            collected = self.resources.copy()
            self.resources = {}  # Une fois collectées, les ressources sont épuisées
            return collected
        return {}
    
    def colonize(self):
        if not self.colonized:
            self.colonized = True
            return True
        return False

class Player:
    def __init__(self, name):
        self.name = name
        self.fuel = 100
        self.resources = {}
        self.colonies = []
    
    def explore(self, planet):
        if self.fuel >= 10:
            self.fuel -= 10
            print(f"Vous explorez la planète {planet.name}.")
            return True
        else:
            print("Carburant insuffisant pour explorer.")
            return False
    
    def collect(self, planet):
        if planet.resources:
            collected = planet.collect_resources()
            for key, value in collected.items():
                self.resources[key] = self.resources.get(key, 0) + value
            print(f"Vous avez collecté {collected} de {planet.name}.")
        else:
            print(f"Aucune ressource disponible sur {planet.name}.")
    
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

planets = [
    Planet("Terra Nova", "Grande", {"minerai": 50, "carburant": 30}),
    Planet("Zyphera", "Moyenne", {"gaz rare": 20}),
    Planet("Kronos", "Petite", {"cristaux": 10})
]

player = Player("Explorateur")

while True:
    print("\n1. Explorer une planète\n2. Collecter des ressources\n3. Coloniser une planète\n4. Afficher statut\n5. Quitter")
    choix = input("Que voulez-vous faire ? ")
    
    if choix == "1":
        for i, planet in enumerate(planets):
            print(f"{i + 1}. {planet.name} ({'Colonisée' if planet.colonized else 'Libre'})")
        idx = int(input("Choisissez une planète à explorer : ")) - 1
        if 0 <= idx < len(planets):
            player.explore(planets[idx])
    
    elif choix == "2":
        for i, planet in enumerate(planets):
            print(f"{i + 1}. {planet.name}")
        idx = int(input("Choisissez une planète pour collecter : ")) - 1
        if 0 <= idx < len(planets):
            player.collect(planets[idx])
    
    elif choix == "3":
        for i, planet in enumerate(planets):
            print(f"{i + 1}. {planet.name} ({'Colonisée' if planet.colonized else 'Libre'})")
        idx = int(input("Choisissez une planète à coloniser : ")) - 1
        if 0 <= idx < len(planets):
            player.colonize(planets[idx])
    
    elif choix == "4":
        print(f"Carburant : {player.fuel}\nRessources : {player.resources}\nColonies : {[p.name for p in player.colonies]}")
    
    elif choix == "5":
        break
    
    else:
        print("Choix invalide, essayez encore.")