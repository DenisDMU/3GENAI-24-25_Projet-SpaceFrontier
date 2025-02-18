class Vaisseau:
    def __init__(self):
        self.nom = "Vaisseau"
        self.moteurs = 1  
        self.armes = 1    
        self.scanners = 1 
        self.carburant = 100  # Capacité initiale
        self.credits = 100000000
        self.modele = "Basique"  # Modèle par défaut
        self.modeles_debloques = ["Basique"]  # Liste des modèles débloqués

    def ameliorer_moteurs(self):
        cout = self.moteurs * 10  # Coût augmente de 10 crédits par niveau
        if self.moteurs < 100 and self.credits >= cout:
            print(f"Amélioration des moteurs pour {cout} crédits. Vous pouvez maintenant voyager plus vite.")
            self.moteurs += 1
            self.credits -= cout
        elif self.credits < cout:
            print(f"Crédits insuffisants pour améliorer les moteurs. Coût : {cout} crédits.")
        else:
            print("Vos moteurs sont déjà au maximum.")

    def ameliorer_carburant(self):
        cout = self.carburant * 10
        if self.carburant < 1000 and self.credits >= cout:
            print(f"Amélioration du carburant pour {cout} crédits. Vous pouvez maintenant voyager plus loin.")
            self.carburant += 10
            self.credits -= cout
        elif self.credits < cout:
            print(f"Crédits insuffisants pour améliorer le carburant. Coût : {cout} crédits.")
        else:
            print("Votre carburant est déjà au maximum.")

    def ameliorer_armes(self):
        cout = self.armes * 10  # Coût augmente de 10 crédits par niveau
        if self.armes < 100 and self.credits >= cout:
            print(f"Amélioration des armes pour {cout} crédits. Vous êtes maintenant plus puissant contre les ennemis.")
            self.armes += 1
            self.credits -= cout
        elif self.credits < cout:
            print(f"Crédits insuffisants pour améliorer les armes. Coût : {cout} crédits.")
        else:
            print("Vos armes sont déjà au maximum.")

    def ameliorer_scanners(self):
        cout = self.scanners * 10  # Coût augmente de 10 crédits par niveau
        if self.scanners < 100 and self.credits >= cout:
            print(f"Amélioration des scanners pour {cout} crédits. Vous pouvez maintenant détecter plus de ressources.")
            self.scanners += 1
            self.credits -= cout
        elif self.credits < cout:
            print(f"Crédits insuffisants pour améliorer les scanners. Coût : {cout} crédits.")
        else:
            print("Vos scanners sont déjà au maximum.")

    def ameliorer_vaisseau(self):
        if self.modele == "Basique" and "Mercenaire" not in self.modeles_debloques and self.credits >= 5:
            confirmation = input("Payer 50 crédits pour débloquer le modèle Mercenaire ? (Oui/Non): ")
            if confirmation.lower() == "oui":
                self.modeles_debloques.append("Mercenaire")
                self.credits -= 50
                print("Modèle Mercenaire débloqué !")
        elif self.modele == "Mercenaire" and "Conqueror" not in self.modeles_debloques and self.credits >= 5:
            confirmation = input("Payer 5 crédits pour débloquer le modèle Conqueror ? (Oui/Non): ")
            if confirmation.lower() == "oui":
                self.modeles_debloques.append("Conqueror")
                self.credits -= 50
                print("Modèle Conqueror débloqué !")
        else:
            print("Vous avez déjà débloqué tous les modèles disponibles.")

    def choisir_modele(self):
        print("Modèles débloqués :")
        for i, modele in enumerate(self.modeles_debloques, start=1):
            print(f"{i}. {modele}")
        choix = int(input("Choisissez un modèle par son numéro : ")) - 1
        if 0 <= choix < len(self.modeles_debloques):
            self.modele = self.modeles_debloques[choix]
            print(f"Vous avez choisi le modèle : {self.modele}")
        else:
            print("Choix invalide.")

    def afficher_statistiques(self):
        print(f"Nom: {self.nom}")
        print(f"Modèle: {self.modele}")
        print(f"Moteurs: {self.moteurs}")
        print(f"Armes: {self.armes}")
        print(f"Scanners: {self.scanners}")
        print(f"Carburant: {self.carburant}")
        print(f"Crédits: {self.credits}")

    def nommer_vaisseau(self, nom):
        self.nom = nom
        print(f"Votre vaisseau a été nommé : {self.nom}")

    def afficher_vaisseau(self):
        if self.modele == "Basique":
            print("""

            Vaisseau Basique

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

            Mercenaire

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

            Conqueror

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
    print("4. Améliorer le carburant")
    print("5. Afficher les statistiques")
    print("6. Nommer le vaisseau")
    print("7. Améliorer le modèle du vaisseau")
    print("8. Choisir le modèle du vaisseau")
    print("9. Afficher votre vaisseau")
    print("10. Retour")

    choice = input("Votre choix: ")

    if choice == '1':
        vaisseau.ameliorer_moteurs()
    elif choice == '2':
        vaisseau.ameliorer_armes()
    elif choice == '3':
        vaisseau.ameliorer_scanners()
    elif choice == '4':
        vaisseau.ameliorer_carburant()
    elif choice == '5':
        vaisseau.afficher_statistiques()
    elif choice == '6':
        nom = input("Entrez le nom de votre vaisseau: ")
        vaisseau.nommer_vaisseau(nom)
    elif choice == '7':
        vaisseau.ameliorer_vaisseau()
    elif choice == '8':
        vaisseau.choisir_modele()
    elif choice == '9':
        vaisseau.afficher_vaisseau()
    elif choice == '10':
        return
    else:
        print("Option invalide.")