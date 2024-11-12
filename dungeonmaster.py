import random


def generer_niveau():
    liste = [random.choice([0, 1]) for i in range(20)]
    return liste

def lance_de():
    return random.randint(1, 6)


for i in range(3): 
    print(generer_niveau())

def traverse_niveau(niveau):
    vie = 1
    for o in niveau:
        if niveau == 0: #Salle sans ennemi
            print("La salle est vide")
        else: #Salle avec un ennemi 
            if lance_de in [1, 2, 3]:
                vie -= 1
                print(vie)
                
            else:
                print("Bravo (la traversée du niveau a été réussie)") 

                






