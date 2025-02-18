class Mission:
    def __init__(self, description, objectif, recompense):
        self.description = description
        self.objectif = objectif  # Doit prendre (player, vaisseau)
        self.recompense = recompense
        self.accomplie = False

    def verifier_accomplissement(self, player, vaisseau):
        if not self.accomplie and self.objectif(player, vaisseau):
            self.accomplie = True
            player.credits += self.recompense
            vaisseau.credits += self.recompense
            print(f"\n🎉 Bravo ! Vous avez accompli la mission : {self.description} 🎉")
            print(f"💰 Récompense : {self.recompense} crédits 💰\n")
