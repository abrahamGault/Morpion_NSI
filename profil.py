class Profil:
    def __init__(self):
        self.nom = ""
       
    def selecProfil(self, table):
        rep = input("Si vous disposez déjà d'un profil tapez 'o', sinon tapez 'n' pour créer un nouveau profil: ").strip(" ")
        
        if rep == "o":
            for i in table[1:]:
                print(f"{table.index(i)}, {i[0]}")

            pfofilNbr = float(input("Lequel êtes-vous ? (répondez par le nombre correspondant apparaissant devant): "))
            
            for j in table[1:] :
                if pfofilNbr == table.index(j):
                   self.nom = j[0]
            #afficher nom de profil et sélectionner avec nbr
        
        if rep == "n":
            self.nom = input("Entrez votre nom: ")
            table.append([self.nom, 0.0, 0.0, 0.0, 0.0])

        #change la table avec les informations ajoutées/modifiées
        return table

    def victoire(self, table):
        print(f"{self.nom} a gagné")
        
        for i in table[1:]:
            if i[0].rstrip() == self.nom :
                i[1] = float(i[1]); i[4] = float(i[4])
                i[1] += 1; i[3] = i[1]; i[4] += 1 #augmente le nombre de victoires, met à jour le ratio de victoire défaite et la série de victoires 

                if float(i[2]) != 0.0 : #traite le cas ou le joueur n'a jamais perdu car on ne peut pas diviser par zéro
                    i[3] = float(i[1])/float(i[2])

        #change la table avec les informations ajoutées/modifiées
        return table
    
    def defaite(self, table):
        
        for i in table[1:]:
            if i[0].rstrip() == self.nom:
                i[2] = float(i[2])
                i[2] += 1;i[3] = float(i[1])/float(i[2]);i[4] = 0 #augment le nombre de défaites, met à jour le ratio victoire défaite et la série de victoires (qui sera nulle)

        #ici nous ne risquons pas de diviser par zéro car le joueur a forcement deja perdu

        #change la table avec les informations ajoutées/modifiées
        return table
