# Casino
import random
import time

from rungame import runGame

# Initialisation des variables
level = 1
dotation = 10
name_user = input("Je suis Python. Quel est votre pseudo ? ")
#rechercher si le jouer existe déjà
#si oui, récupérer les données et passer à les regles du jeu
#si non, créer un nouveau joueur et afficher les regles du jeu
print(f"Hello {name_user}, vous avez {dotation} €, Très bien ! Installez vous SVP à la table de pari.\n\t\t\t Je vous expliquerai le principe du jeu : \n")
print(f"Je viens de penser à un nombre entre 1 et {dotation} en fonction du niveau. Devinez lequel ?\n")
print(f"Att : vous avez le droit à trois essais !\n")
print(f"Si vous devinez mon nombre dès le premier coup, vous gagnez le double de votre mise !\n")
print(f"Si vous le devinez au 2è coup, vous gagnez exactement votre mise !\n")
print(f"Si vous le devinez au 3è coup, vous gagnez la moitiè votre mise !\n")

# Début du jeu
while True:
    mise = input(f"Le jeu commence, entrez votre mise : ? ({dotation})\n")
    while not mise.isdigit() or int(mise) > dotation:
        mise = input(f"Le montant saisi n'est pas valide. Entrer SVP un montant entre 1 et {dotation}€ :  ?\n")
    mise = int(mise)
    dotation -= mise
    result = runGame(level, mise, name_user)
    if result[0] == "n":
        print(f"Vous avez gagné {(dotation + result[1])} € ! A bientôt {name_user}!\n")
        #update du player stats
        break
    elif result[0] == "o":
        level = result[1]
        dotation += result[2]
    elif result[0] == "perdu":
        level = result[1]
        dotation += result[2]   
    if dotation == 0:
        print(f"Vous avez perdu ! Vous n'avez plus de dotation !\n")
        #afficher ses stats globale
        break
    