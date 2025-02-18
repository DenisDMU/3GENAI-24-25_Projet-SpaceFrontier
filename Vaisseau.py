class Vaisseau:
    def __init__(self):
        self.nom = "Vaisseau"
        self.moteurs = 1
        self.armes = 1
        self.scanners = 1
        self.carburant = 100
        self.credits = 0
        self.modele = "Basique"  # Modèle par défaut

    def ameliorer_moteurs(self):
        if self.moteurs < 10 and self.credits >= 1:
            print("Amélioration des moteurs. Vous pouvez maintenant voyager plus vite.")
            self.moteurs += 1
            self.credits -= 1
        elif self.credits < 1:
            print("Crédits insuffisants pour améliorer les moteurs.")
        else:
            print("Vos moteurs sont déjà au maximum.")

    def ameliorer_armes(self):
        if self.armes < 10 and self.credits >= 1:
            print("Amélioration des armes. Vous êtes maintenant plus puissant contre les ennemis.")
            self.armes += 1
            self.credits -= 1
        elif self.credits < 1:
            print("Crédits insuffisants pour améliorer les armes.")
        else:
            print("Vos armes sont déjà au maximum.")

    def ameliorer_scanners(self):
        if self.scanners < 10 and self.credits >= 1:
            print("Amélioration des scanners. Vous pouvez maintenant détecter plus de ressources.")
            self.scanners += 1
            self.credits -= 1
        elif self.credits < 1:
            print("Crédits insuffisants pour améliorer les scanners.")
        else:
            print("Vos scanners sont déjà au maximum.")
    
    def ameliorer_vaisseau(self):
        if self.modele == "Basique" and self.credits >=5:
            self.model == "Mercenaire"
            self.credits -= 5
        elif self.modele == "Mercenaire" and self.credits >= 5:
            self.model == "Conqueror"
            self.credits -= 5
        elif self.modele == "Conqueror":
            print("Votre vaisseau est déjà au maximum.")

    def afficher_statistiques(self):
        print(f"Nom: {self.nom}")
        print(f"Modèle: {self.modele}")
        print(f"Moteurs: {self.moteurs}")
        print(f"Armes: {self.armes}")
        print(f"Scanners: {self.scanners}")
        print(f"Carburant: {self.carburant}")
        print(f"Crédits: {self.credits}")
        print(f"Modele: {self.modele}")

    def nommer_vaisseau(self, nom):
        self.nom = nom
        print(f"Votre vaisseau a été nommé : {self.nom}")

    def afficher_vaisseau(self):
        if self.modele == "Basique":
            print("""
            [  (    _____
                \__\,-'//   `--._
                [_/~||,-----.\@_\\___
                [_) |||()()()   ~[|||>
                [_\_||`-----'   //
                /  /`-.\\___,--'==(-
            [  (
        """)
        elif self.modele == "Mercenaire":
            print("""
                      		)__/... \_
                      00)__)  .___)
     ___              _0__)\_/ OOO/`':.
    0)_^'-._    __..-'`:  \ | / ::  \ o`:
    0)_\ \~_..-': \ \   :  \|/   ::  |   \
        \ /      : | |  :    :  ::  /  _./>-
         (__ ))): /_/____.))_____//.-'`
          7 7~~'           7 7
          L_L                 / /
         0) ^'-.__            |_|
         0)__.-'             0) ^'-.__
                             0)__.-'
        """)
        elif self.modele == "Conqueror":
            print("""
                          `. ___
                    __,' __`.                _..----....____
        __...--.'``;.   ,.   ;``--..__     .'    ,-._    _.-'
  _..-''-------'   `'   `'   `'     O ``-''._   (,;') _,'
,'________________                          \`-._`-','
 `._              ```````````------...___   '-.._'-:
    ```--.._      ,.                     ````--...__\-.
            `.--. `-`                       ____    |  |`
              `. `.                       ,'`````.  ;  ;`
                `._`.        __________   `.      \'__/`
                   `-:._____/______/___/____`.     \  `
                               |       `._    `.    \
                               `._________`-.   `.   `.___
                                               `------'`
        """)
        else:
            print("Modèle de vaisseau inconnu.")

def upgrade_ship(vaisseau):
    print("Choisissez ce que vous voulez faire:")
    print("1. Améliorer les moteurs")
    print("2. Améliorer les armes")
    print("3. Améliorer les scanners")
    print("4. Afficher les statistiques")
    print("5. Nommer le vaisseau")
    print("6. Choisir le modèle du vaisseau")
    print("7. Afficher votre vaisseau")
    print("8. Retour")

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
        nom = input("Entrez le nom de votre vaisseau: ")
        vaisseau.nommer_vaisseau(nom)
    elif choice == '6':
        modele = input("Upgrad: ")
        vaisseau.ameliorer_vaisseau(modele)
    elif choice == '7':
        vaisseau.afficher_vaisseau()
    elif choice == '8':
        return
    else:
        print("Option invalide.")
