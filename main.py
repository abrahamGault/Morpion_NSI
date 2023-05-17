import random
from profil import Profil
from tri import tri

plateau = [[".", ".", "."],[".", ".", "."],[".", ".", "."]]

f = open("score.csv", "r")
table = [ligne.rstrip().split(",") for ligne in f]

#converti les valeurs contenues en chaines de caractère en nombres flottants       
for i in table[1:]:
    for j in range(1, len(i)):
        i[j] = float(i[j])

f.close()

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


def aligner():
	Point = "."
	for i in range(3):
		if (plateau[0][i] == "X" and plateau[1][i] == "X" and plateau[2][i] == "X") or (plateau[0][i] == "O" and plateau[1][i] == "O" and plateau[2][i] == "O"):
			return True
	if ((plateau[0][0] == "X" and plateau[1][1] == "X" and plateau[2][2] == "X" ) or (plateau[0][0] == "O" and plateau[1][1] == "O" and plateau[2][2] == "O" )) or ((plateau[0][2] == "X" and plateau[1][1] == "X" and plateau[2][0] == "X" ) or (plateau[0][2] == "O" and plateau[1][1] == "O" and plateau[2][0] == "O" )):
		return True
	if Point in plateau[0] or Point in plateau[1] or Point in plateau[2] :
		return False
	print('égalité')
	exit()		

def main():
	joueur1 = Profil()
	table = joueur1.selecProfil()
	print(joueur1.nom,"est le joueur 1. Il/elle jouera avec X")
	
	joueur2 = Profil()
	table = joueur2.selecProfil()

	print(joueur2.nom, "est le joueur 2. Il/elle jouera avec O")
	affiche()
	
	joueur = random.randint(0,1)

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
		table = joueur2.victoire()
		table = joueur1.defaite()

	elif joueur == 1 :
		table = joueur1.victoire()
		table = joueur2.defaite()

if __name__ == "__main__":	
	main()
	