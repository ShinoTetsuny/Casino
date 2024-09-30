import random
import math

def runGame(level, mise, name_user):
    while True:
        nb_python = random.randint(1, (level * 10))
        init_coup =  math.floor(math.log2(level*10))
        nb_coup = init_coup
        gain = 0
        print(f"level = {level} et mise = {mise}\n")
        print(f"nombre de coup = {init_coup}\n")
        for i in range(1, nb_coup + 1):  
            nb_user = input(f"Alors mon nombre est : ? (entre 0 et {level * 10})\n")
            
            while not nb_user.isdigit() or int(nb_user) < 1 or int(nb_user) > (level * 10):
                nb_user = input(f"Je ne comprends pas ! Entrer SVP un nombre entre 1 et {level * 10} :  ?\n")
            
            nb_user = int(nb_user)
            
            if nb_user == nb_python:
                gain = mise * (1 + level + ((init_coup - i)/10)) 
                print(f"Bingo {name_user}, vous avez gagné en {i} coup(s) et vous avez emporté {gain} € !\n")
                level += 1
                next_level = input(f"Voulez-vous continuer au niveau {level} ? (o/n) ")
                if next_level == "n":
                    #créer la stats de a game
                    return "n", gain
                if next_level == "o":
                    print(f"Super {name_user}, nous passons au niveau {level} !\n")
                    #créer la stats de a game
                    return "o", level, gain
                
            else:
                print(f"Perdu !")

                if nb_coup > 0:
                    nb_coup -= 1
                    print(f"Vous avez encore {nb_coup} chances !\n")
                    if nb_user < nb_python:
                        print(f"Votre nombre est trop petit !\n")
                    else:
                        print(f"Votre nombre est trop grand !\n")
                    
                    if nb_coup > 1:
                        print(f"Il vous reste {nb_coup} chances !\n")
                        print(f"le chiffre est {nb_python} !\n")
                    else:
                        print(f"Il vous reste une chance !\n")
                else:
                    print(f"Vous avez perdu ! Mon nombre était {nb_python} !\n")
                    
            
            if nb_coup == 0:
                print(f"Désolé {name_user}, vous avez utilisé toutes vos tentatives.\n")
                #créer la stats de a game
                return "perdu", level, gain
