import random
import numpy as np

niveau = np.random.randint(0, 2, (10, 10)).astype(object)
niveau[9, 9] = 'FIN'
joueur = 9
niveau[0, 0] = joueur
vie_joueur = 10
x, y = 0, 0

def deplacement(x, y, direction):
    if direction == "z" and x > 0: 
        x -= 1
    elif direction == "q" and y > 0: 
        y -= 1
    elif direction == "s" and x < 9:  
        x += 1
    elif direction == "d" and y < 9: 
        y += 1
    return x, y



while True :
    niveau[x, y] = joueur
    print(niveau)
    print("Le joueur à encore ", vie_joueur,"PV")
    zqsd = str(input("Déplacement avec ZQSD : ")) 
    niveau[x, y] = 0  
    x, y = deplacement(x, y, zqsd)
    if niveau[x, y] == 1:
        vie_joueur -= 1
    if niveau[x, y] == 'FIN':
        print("Félicitations, vous avez vaincu le dongeon !")
        break
    if vie_joueur < 0:
        print(("Vous avez perdu !!!!!"))
        break