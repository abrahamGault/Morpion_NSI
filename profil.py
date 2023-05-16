class Profil:
    def __init__(self):
        f = open("score.csv", "r")
        self.table = [ligne.rstrip().split(",") for ligne in f]

        #converti les valeurs contenues en chaines de caractère en nombres flottants       
        for i in self.table[1:]:
            for j in range(1, len(i)):
                i[j] = float(i[j])
        
        f.close()
       
    def selecProfil(self):
        rep = input("Si vous disposez déjà d'un profil tapez 'o', sinon tapez 'n' pour créer un nouveau profil: ").strip(" ")
        
        if rep == "o":
            for i in self.table[1:]:
                print(f"{self.table.index(i)}, {i[0]}")

            pfofilNbr = input("Lequel êtes-vous ? (répondez par le nombre correspondant apparaissant devant): ")
            
            for j in self.table[1:] :
                if pfofilNbr == self.table.index(j):
                   self.nom = j[0]
            #afficher nom de profil et sélectionner avec nbr
        
        if rep == "n":
            self.nom = input("Entrez votre nom: ")
            self.table.append([self.nom, 0, 0, 0, 0])

    def victoire(self):
        print(f"{self.nom} a gagné")

    def defaite(self):
        pass