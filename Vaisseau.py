# Définition des couleurs ANSI
RED = '\033[91m'
GREEN = '\033[92m'
BLUE = '\033[94m'
YELLOW = '\033[93m'
RESET = '\033[0m'

class Vaisseau:
    def __init__(self):
        self.nom = "Vaisseau"
        self.moteurs = 1
        self.armes = 1
        self.scanners = 1
        self.carburant = 100
        self.credits = 0
        self.modele = "Basique"
        self.modeles_debloques = ["Basique"]

    def ameliorer_moteurs(self):
        cout = self.moteurs * 10
        if self.moteurs < 100 and self.credits >= cout:
            print(f"{GREEN}Amélioration des moteurs pour {cout} crédits. Vous pouvez maintenant voyager plus vite.{RESET}")
            self.moteurs += 1
            self.credits -= cout
        elif self.credits < cout:
            print(f"{RED}Crédits insuffisants pour améliorer les moteurs. Coût : {cout} crédits.{RESET}")
        else:
            print(f"{YELLOW}Vos moteurs sont déjà au maximum.{RESET}")

    def ameliorer_carburant(self):
        cout = (self.carburant // 10) * 20
        if self.carburant < 1000 and self.credits >= cout:
            print(f"{GREEN}Amélioration du carburant pour {cout} crédits. Vous pouvez maintenant voyager plus loin.{RESET}")
            self.carburant += 10
            self.credits -= cout
        elif self.credits < cout:
            print(f"{RED}Crédits insuffisants pour améliorer le carburant. Coût : {cout} crédits.{RESET}")
        else:
            print(f"{YELLOW}Votre carburant est déjà au maximum.{RESET}")

    def ameliorer_armes(self):
        cout = self.armes * 10
        if self.armes < 100 and self.credits >= cout:
            print(f"{GREEN}Amélioration des armes pour {cout} crédits. Vous êtes maintenant plus puissant contre les ennemis.{RESET}")
            self.armes += 1
            self.credits -= cout
        elif self.credits < cout:
            print(f"{RED}Crédits insuffisants pour améliorer les armes. Coût : {cout} crédits.{RESET}")
        else:
            print(f"{YELLOW}Vos armes sont déjà au maximum.{RESET}")

    def ameliorer_scanners(self):
        cout = self.scanners * 10
        if self.scanners < 100 and self.credits >= cout:
            print(f"{GREEN}Amélioration des scanners pour {cout} crédits. Vous pouvez maintenant détecter plus de ressources.{RESET}")
            self.scanners += 1
            self.credits -= cout
        elif self.credits < cout:
            print(f"{RED}Crédits insuffisants pour améliorer les scanners. Coût : {cout} crédits.{RESET}")
        else:
            print(f"{YELLOW}Vos scanners sont déjà au maximum.{RESET}")

    def ameliorer_vaisseau(self):
        if self.modele == "Basique" and "Mercenaire" not in self.modeles_debloques and self.credits >= 50:
            confirmation = input(f"{BLUE}Payer 50 crédits pour débloquer le modèle Mercenaire ? (Oui/Non): {RESET}")
            if confirmation.lower() == "oui":
                self.modeles_debloques.append("Mercenaire")
                self.credits -= 50
                print(f"{GREEN}Modèle Mercenaire débloqué !{RESET}")
        elif self.modele == "Mercenaire" and "Conqueror" not in self.modeles_debloques and self.credits >= 50:
            confirmation = input(f"{BLUE}Payer 50 crédits pour débloquer le modèle Conqueror ? (Oui/Non): {RESET}")
            if confirmation.lower() == "oui":
                self.modeles_debloques.append("Conqueror")
                self.credits -= 50
                print(f"{GREEN}Modèle Conqueror débloqué !{RESET}")
        else:
            print(f"{YELLOW}Vous avez déjà débloqué tous les modèles disponibles.{RESET}")

    def choisir_modele(self):
        print(f"{BLUE}Modèles débloqués :{RESET}")
        for i, modele in enumerate(self.modeles_debloques, start=1):
            print(f"{BLUE}{i}. {modele}{RESET}")
        choix = int(input(f"{BLUE}Choisissez un modèle par son numéro : {RESET}")) - 1
        if 0 <= choix < len(self.modeles_debloques):
            self.modele = self.modeles_debloques[choix]
            print(f"{GREEN}Vous avez choisi le modèle : {self.modele}{RESET}")
        else:
            print(f"{RED}Choix invalide.{RESET}")

    def afficher_statistiques(self):
        print(f"{BLUE}Nom: {self.nom}")
        print(f"Modèle: {self.modele}")
        print(f"Moteurs: {self.moteurs}")
        print(f"Armes: {self.armes}")
        print(f"Scanners: {self.scanners}")
        print(f"Carburant: {self.carburant}")
        print(f"Crédits: {self.credits}{RESET}")

    def nommer_vaisseau(self, nom):
        self.nom = nom
        print(f"{GREEN}Votre vaisseau a été nommé : {self.nom}{RESET}")

    def afficher_vaisseau(self):
        print(f"{BLUE}")  # Début de la couleur bleue pour l'ASCII art
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
        print(f"{RESET}")  # Fin de la couleur bleue

def upgrade_ship(vaisseau):
    print(f"{RED}=== MENU D'AMÉLIORATION DU VAISSEAU ==={RESET}")
    print(f"{RED}1. Améliorer les moteurs")
    print("2. Améliorer les armes")
    print("3. Améliorer les scanners")
    print("4. Améliorer le carburant")
    print("5. Afficher les statistiques")
    print("6. Nommer le vaisseau")
    print("7. Améliorer le modèle du vaisseau")
    print("8. Choisir le modèle du vaisseau")
    print("9. Afficher votre vaisseau")
    print(f"10. Retour{RESET}")

    choice = input(f"{BLUE}Votre choix: {RESET}")

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
        nom = input(f"{BLUE}Entrez le nom de votre vaisseau: {RESET}")
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
        print(f"{RED}Option invalide.{RESET}")