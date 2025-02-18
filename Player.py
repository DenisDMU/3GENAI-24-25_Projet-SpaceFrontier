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
