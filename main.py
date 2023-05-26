import random
from profil import Profil

plateau = [[".", ".", "."],[".", ".", "."],[".", ".", "."]]

f = open("score.csv", "r")
table = [ligne.rstrip().split(",") for ligne in f]

#converti les valeurs contenues en chaines de caractère en nombres flottants       
for i in table[1:]:
    for j in i[1:]:
	    j = float(j)

f.close()

def tri(lst, ind):#la variable ind correspond à la variable selon laquelle trier la liste (ex: selon le nbr de victoires ou de victoires consécutives)
    if len(lst) <= 1:
        return lst
    else:
        return fusion(tri([lst.pop(i) for i in range(round(len(lst) / 2))], ind), tri(lst, ind), ind)

def fusion(lstA, lstB, ind): #idem
    if lstA == []:
        return lstB
    
    if lstB == []:
        return lstA
    
    if lstA[0][ind] >= lstB[0][ind]:
        return [lstA[0]] + fusion(lstA[1:], lstB, ind)

    else : 
        return [lstB[0]] + fusion(lstA, lstB[1:], ind)

def stats(lst):
	print("1. Victoires \n2. Défaites \n3. Le Ratio Victoires/Défaites \n4. La série de Victoires")
	ind = int(input("Choisissez selon quelle catégorie les statistiques seront triées: "))

	lst = tri(lst, ind)
	for i in lst:
		print(i[0])

def affiche(): 
	#affiche le plateau de jeu dans la console de manière lisible
	print("\033c") # "nettoie" la console
	print("Plateau :\n")
	print("\t \t","  0 1 2")
	
	for j in range(len(plateau)) :
		print("\t \t",j, end=" ")

		for i in range(len(plateau[0])-1):
			print(plateau[j][i], end=" ")
				 	
		print(plateau[j][-1]) 

def coupPossible(x,y):
	return plateau[y][x] == "."

def choisir(joueur):
	choix = True 
	
	while choix :	
		v = input("Entrez les coordonnées(colonne, ligne) du point de votre choix (séparés par une virgule): ").strip().split(",")
		x, y = int(v[0]), int(v[1])
		
		if coupPossible(x, y) == True:			
			if joueur == 0:
				plateau[y][x] = "X"
				affiche()
				choix = False

			elif joueur == 1:
				plateau[y][x] = "O"
				affiche()
				choix = False
		else :
			print("Le coup est impossible veuillez recommencer")
			continue


def aligner(): #fonction vérifiant si l'un des joueurs a gagné
	Point = "."
	
	#verif lignes
	for i in range(3):
		if (plateau[0][i] == "X" and plateau[1][i] == "X" and plateau[2][i] == "X") or (plateau[0][i] == "O" and plateau[1][i] == "O" and plateau[2][i] == "O"):
			return True
	#verif lignes	
	for i in range(3):
		if(plateau[i][0] == "X" and plateau[i][1] == "X" and plateau[i][2] =="X" ) or (plateau[i][0] == "O" and plateau[i][1] == "O" and plateau[i][2] == "O"):
			return True
	#verif diagonale
	if ((plateau[0][0] == "X" and plateau[1][1] == "X" and plateau[2][2] == "X" ) or (plateau[0][0] == "O" and plateau[1][1] == "O" and plateau[2][2] == "O" )) or ((plateau[0][2] == "X" and plateau[1][1] == "X" and plateau[2][0] == "X" ) or (plateau[0][2] == "O" and plateau[1][1] == "O" and plateau[2][0] == "O" )):
		return True
	
	if Point in plateau[0] or Point in plateau[1] or Point in plateau[2] :
		return False
	
	print('égalité')
	exit()		

def main():
	global table

	joueur1 = Profil()
	table = joueur1.selecProfil(table)
	print(joueur1.nom,"est le joueur 1. Il/elle jouera avec X")
	
	joueur2 = Profil()
	table = joueur2.selecProfil(table)

	print(joueur2.nom, "est le joueur 2. Il/elle jouera avec O")
	affiche()
	
	#le jeu choisi aléatoirment le jouer qui débute
	joueur = random.randint(0,1)

	#tant que personne n'a gagné le jeu continue
	while aligner() == False :
		if joueur == 0 :
			print("C'est à", joueur1.nom,"de jouer")
			choisir(joueur)
			joueur = 1

		elif joueur == 1 :
			print("C'est à", joueur2.nom,"de jouer")
			choisir(joueur)
			joueur = 0

	if joueur == 0 :
		table = joueur2.victoire(table)
		table = joueur1.defaite(table)

	elif joueur == 1 :
		table = joueur1.victoire(table)
		table = joueur2.defaite(table)

	#réecriture du fichier csv avec
	fichier = open("score.csv", "w")
	
	for i in table:
		for j in i:
			fichier.write(f"{str(j)}, ")
		fichier.write("\n")

if __name__ == "__main__":	
	try:
		rep = input("Appuyez sur 'j' pour jouer et sur 's' pour voir les statistiques de joueurs: ")
		if rep.rstrip() == "j":
			main()

		if rep.rstrip() == "s":
			stats(table[1:])

	except KeyboardInterrupt:
		print("\n")
		print("La partie ne sera pas enregistrée")
