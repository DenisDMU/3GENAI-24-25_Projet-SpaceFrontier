class Vaisseau:
    def __init__(self):
        self.moteurs = 1
        self.armes = 1
        self.scanners = 1
        self.carburant = 100

    def ameliorer_moteurs(self):
        if self.moteurs < 10:
            print("Amélioration des moteurs. Vous pouvez maintenant voyager plus vite.")
            self.moteurs += 1
        else:
            print("Vos moteurs sont déjà au maximum.")

    def ameliorer_armes(self):
        if self.armes < 10:
            print("Amélioration des armes. Vous êtes maintenant plus puissant contre les ennemis.")
            self.armes += 1
        else:
            print("Vos armes sont déjà au maximum.")

    def ameliorer_scanners(self):
        if self.scanners < 10:
            print("Amélioration des scanners. Vous pouvez maintenant détecter plus de ressources.")
            self.scanners += 1
        else:
            print("Vos scanners sont déjà au maximum.")

    def afficher_statistiques(self):
        print(f"Moteurs: {self.moteurs}")
        print(f"Armes: {self.armes}")
        print(f"Scanners: {self.scanners}")
        print(f"Carburant: {self.carburant}")

def upgrade_ship(vaisseau):
    print("Choisissez ce que vous voulez améliorer:")
    print("1. Moteurs")
    print("2. Armes")
    print("3. Scanners")
    print("4. Afficher les statistiques")
    print("5. Retour")

    choice = input("Votre choix: ")

    if choice == '1':
        vaisseau.ameliorer_moteurs()
    elif choice == '2':
        vaisseau.ameliorer_armes()
    elif choice == '3':
        vaisseau.ameliorer_scanners()
    elif choice == '4':
        vaisseau.afficher_statistiques()
    elif choice == '5':
        return
    else:
        print("Option invalide.")
