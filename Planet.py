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
