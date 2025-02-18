class Planet:
    def __init__(self, name, size, resources):
        self.name = name
        self.size = size
        self.resources = resources  # Ressources disponibles
        self.initial_resources = resources.copy()  # Stockage des ressources de départ
        self.colonized = False

    def collect_resources(self, amount=None):
        """ Permet au joueur de collecter des ressources petit à petit. """
        if not self.resources:
            print(f"{self.name} n'a plus de ressources disponibles.")
            return {}

        collected = {}

        for resource, quantity in self.resources.items():
            if amount:
                to_collect = min(amount, quantity)
                collected[resource] = to_collect
                self.resources[resource] -= to_collect
            else:
                collected[resource] = quantity
                self.resources[resource] = 0
        
        return collected

    def regenerate_resources(self, percentage=20):
        """
        Régénère un pourcentage des ressources **uniquement si elles ne sont pas déjà au max**.
        Par défaut, restaure 20% des ressources initiales.
        """
        for resource, max_quantity in self.initial_resources.items():
            if self.resources.get(resource, 0) < max_quantity:
                regen_amount = int(max_quantity * (percentage / 100))
                self.resources[resource] = min(self.resources.get(resource, 0) + regen_amount, max_quantity)
    
    def colonize(self):
        if not self.colonized:
            self.colonized = True
            return True
        return False
