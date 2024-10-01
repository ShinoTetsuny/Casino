# Casino
import time
from SQL_request import *
from db_connect import mysqlconnect

from rungame import runGame

# Initialisation des variables
conn = mysqlconnect()
cur = conn.cursor()
level = 1
dotation = 10
name_user = input("Je suis Python. Quel est votre pseudo ? ")
user = getUser(name_user)
if user:
    print(f"user {user}")
    print(f"ReBonjour {name_user}, vous avez déjà un compte !\n")
    print(f"Voulez vous retourner au dernier niveau({user['last_level']}) ? (o/n) ")
    if input() == "o":
        level = user["last_level"]
else:
    insertNewUser(name_user)
    print(f"Bonjour {name_user}, vous avez un nouveau compte !\n")
    user = getUser(name_user)

regles = input(f"Voulez-vous voir les règles du jeu ? (o/n) ")
if regles == "o":
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
        print(f"Vous avez gagné {(dotation + result[2])} € ! A bientôt {name_user}!\n")
        #update du player stats
        insertNewStats(user['id'], result[1], result[3], mise, result[2])
        updateUser(name_user, result[3], result[2], result[1], user['total_gain'] + result[2], max(user['highest_gain'], result[2]), max(user['highest_putting'], mise), max(user['best_lvl'], result[1]))
        break
    elif result[0] == "o":
        level = result[1]
        dotation += result[2]
        print("user:", user, result[1], result[3], mise, result[2])
        insertNewStats(user['id'], result[1], result[3], mise, result[2])
        # print("user:", name_user, result[3], result[2], result[1], user['total_gain'] + result[2], max(user['highest_gain'], result[2]), max(user['highest_putting'], mise), max(user['best_lvl'], result[1]))
        updateUser(name_user, result[3], result[2], result[1], user['total_gain'] + result[2], max(user['highest_gain'], result[2]), max(user['highest_putting'], mise), max(user['best_lvl'], result[1]))
    elif result[0] == "perdu":
        level = result[1]
        dotation += result[2]
        insertNewStats(user['id'], result[1], result[3], mise, result[2])  
        updateUser(name_user, result[3], result[2], result[1], user['total_gain'] + result[2], max(user['highest_gain'], result[2]), max(user['highest_putting'], mise), max(user['best_lvl'], result[1]))
    if dotation == 0:
        print(f"Vous avez perdu ! Vous n'avez plus de dotation !\n")
        userStats = getUser(name_user)
        print(f"Votre meilleur niveau est {userStats['best_lvl']} avec un gain de {userStats['highest_gain']} € !\n")
        break
    