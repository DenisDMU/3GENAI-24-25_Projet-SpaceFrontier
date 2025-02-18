class Mission:
    def __init__(self, description, objectif, recompense):
        self.description = description  # Texte descriptif de la mission
        self.objectif = objectif  # Une fonction qui vérifie si la mission est accomplie
        self.recompense = recompense  # Nombre de crédits gagnés en cas de succès
        self.accomplie = False  # Statut de la mission

    def verifier_accomplissement(self, player):
        """ Vérifie si la mission est accomplie et donne la récompense. """
        if not self.accomplie and self.objectif(player):
            self.accomplie = True
            player.credits += self.recompense
            print(f"\n🎉 Bravo ! Vous avez accompli la mission : {self.description} 🎉")
            print(f"💰 Récompense : {self.recompense} crédits 💰\n")
