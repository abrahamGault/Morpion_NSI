class Profil:
    def __init__(self):
        self.coup = 0 #nombres de coups que le joueur a effectué

    def selecProfil(self):
        f = open("score.csv", "r")
        table = [ligne.rstrip().split(",") for ligne in f]
        
        rep = input("Si vous disposez déjà d'un profil tapez o, sinon tapez n pour créer un nouveau profil: ").strip(" ")
        
        if rep == "o":
            for i in table:
                print(table.index(i), i)

            pfofilNbr = input("Lequel êtes-vous ? (répondez par le nombre correspondant apparaissant devant): ")
            #afficher nom de profil et sélectionner avec nbr

        f.close()
        
        if rep == "n":
            #a refaire
            f = open("score.csv", "a")
            self.nom = input("Entrez votre nom: ")
            f.write(f"\n{self.nom}, 0, 0")
            f.close()

    def victoire(self):
        print(f"{self.nom} a gagné")

    def defaite(self):
        pass