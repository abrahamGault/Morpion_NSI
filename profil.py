class Profil:
    def __init__(self):
        self.coup = 0 #nombres de coups que le joueur a effectué

    def selecProfil(self):
        f = open("score.csv", "r")
        champs = f.readline()
        lignes = f.readlines()
        table = []

        ligne1 = champs.rstrip().split(",")
        table.append(ligne1)
        indices = [ligne1.index("joueur"), ligne1.index("ratio_v/d"), ligne1.index("serie_victoire")]

        rep = input("Si vous disposez déjà d'un profil tapez o, sinon tapez n pour créer un nouveau profil: ").strip(" ")
        
        if rep == "o":
            pfofilNbr = input("Lequel êtes-vous ? (répondez par le nombre correspondant): ")
            #afficher nom de profil et sélectionner avec nbr   

        f.close()
        
        if rep == "n":
            f = open("score.csv", "a")
            self.nom = input("Entrez votre nom: ")
            f.write(f"\n{self.nom}, 0, 0")
            f.close()

    def victoire(self):
        print(f"{self.nom} a gagné")