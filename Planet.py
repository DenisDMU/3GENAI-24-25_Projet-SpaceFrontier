class Planet:
    def __init__(self, name, size, resources):
        self.name = name
        self.size = size
        self.resources = resources  # Ressources disponibles
        self.initial_resources = resources.copy()  # Stockage des ressources de départ
        self.colonized = False
        self.regenerated = False

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

    def regenerate_resources(self):
        """
        Régénère progressivement les ressources jusqu'à leur niveau initial.
        Affiche un message UNE SEULE FOIS quand la planète est complètement restaurée.
        """
        was_depleted = any(self.resources[res] < self.initial_resources[res] for res in self.initial_resources)

        for resource, max_value in self.initial_resources.items():
            if self.resources[resource] < max_value:
                self.resources[resource] += 5  # Ex: +5 unités par cycle
                if self.resources[resource] > max_value:
                    self.resources[resource] = max_value  # Ne pas dépasser la valeur initiale

        # ✅ Vérifier si la planète a été exploitée avant d'annoncer sa régénération
        if was_depleted and self.resources == self.initial_resources and not self.regenerated:
            print(f"\n🌍✨ La planète {self.name} a retrouvé toutes ses ressources ! ✨\n")
            self.regenerated = True  # ✅ Marquer la planète comme régénérée

        # ✅ Réactiver la régénération si on mine à nouveau
        if was_depleted:
            self.regenerated = False  # Permet d'afficher à nouveau le message si la planète est minée
    
    def colonize(self):
        """ Colonise la planète et augmente durablement ses ressources """
        if not self.colonized:
            for resource in self.resources:
                self.resources[resource] += 10  # ✅ Augmente les ressources actuelles
                self.initial_resources[resource] += 10  # ✅ Augmente aussi la limite de régénération

            self.colonized = True
            print(f"🌍 {self.name} est colonisée ! Ressources augmentées et la planète pourra régénérer davantage.")
            return True

        return False