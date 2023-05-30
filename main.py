import random
from profil import Profil

plateau = [[".", ".", "."],[".", ".", "."],[".", ".", "."]] #plateau contenant les cases du morpion

f = open("score.csv", "r")
table = [ligne.rstrip().split(",") for ligne in f]

#converti les valeurs contenues en chaines de caractère en nombres flottants       
for i in range(1, len(table)):
	for j in range(1, len(table[i])):
		table[i][j] = float(table[i][j])
		
f.close()

def tri(lst, ind):#la variable ind correspond à la variable selon laquelle trier la liste (ex: selon le nbr de victoires ou de victoires consécutives)

	for i in range(len(lst) - 1, 1, -1):
		for j in range(i - 1):
			if lst[j + 1][ind] > lst[j][ind]:
				lst[j+ 1], lst[j] = lst[j], lst[j + 1] 

	return lst


def affiche(): #affiche le plateau de jeu dans la console de manière lisible
	print("\033c") # "nettoie" la console
	print("Plateau :\n")
	print("\t \t","  0 1 2")
	
	for j in range(len(plateau)) :
		print("\t \t",j, end=" ")

		for i in range(len(plateau[0])-1):
			print(plateau[j][i], end=" ")
				 	
		print(plateau[j][-1]) 

def coupPossible(x,y): #vérifie si la case choisie par le joueur est disponible ou non
	return plateau[y][x] == "."

def choisir(joueur): #Permet aux joueurs de choisir leur case selon la disponibilité des cases restantes
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

def main(): #fonction principale pour jouer
	global table

	joueur1 = Profil()
	table = joueur1.selecProfil(table) #ajoute les modifications qui ont pu être faite
	print(joueur1.nom,"est le joueur 1. Il/elle jouera avec X")
	
	joueur2 = Profil()
	table = joueur2.selecProfil(table) #idem

	print(joueur2.nom, "est le joueur 2. Il/elle jouera avec O")
	affiche()
	
	#le jeu choisi aléatoirment le jouer qui débute
	joueur = random.randint(0,1)

	#tant que personne n'a gagné le jeu continue
	while aligner() == False :
		if joueur == 0 :
			print("C'est à", joueur1.nom,"de jouer")
			choisir(joueur)
			joueur = 1 #change le joueur qui placera son

		elif joueur == 1 :
			print("C'est à", joueur2.nom,"de jouer")
			choisir(joueur)
			joueur = 0 #idem

	if joueur == 0 :
		table = joueur2.victoire(table)
		table = joueur1.defaite(table)

	elif joueur == 1 :
		table = joueur1.victoire(table)
		table = joueur2.defaite(table)

	#réecriture du fichier csv avec les modifications de 'table'
	fichier = open("score.csv", "w")
	
	for i in range(len(table)):
		for j in range(len(table[i]) - 1):
			fichier.write(f"{str(table[i][j])}, ")
		fichier.write(f"{str(table[i][j + 1])}\n") #empêche de mettre une virgule à la fin d'une ligne

	fichier.close()

if __name__ == "__main__":	
	
	try:
		rep = input("Appuyez sur 'j' pour jouer et sur 's' pour voir les statistiques de joueurs: ")
		if rep.rstrip() == "j":
			main()

		if rep.rstrip() == "s":
			print("1. Victoires \n2. Défaites \n3. Le Ratio Victoires/Défaites \n4. La série de Victoires")
			ind = int(input("Choisissez selon quelle catégorie les statistiques seront triées: "))

			table = tri(table[1:], ind)
			for i in range(len(table)):
				print(i + 1, table[i][0], "avec", table[i][ind])

	except KeyboardInterrupt:
		print("\nLa partie ne sera pas enregistrée")