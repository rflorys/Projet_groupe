import random


def generer_niveau():
    liste = [random.choice([0, 1]) for i in range(20)]
    return liste

def lance_de():
    return random.randint(1, 6)


salle = generer_niveau()
print(salle)

#for i in range(3): 
#    print(generer_niveau())

def dungeon(salle):
    vie = 1
    for o in salle:
        if o == 0: #Salle sans ennemi
            print("La salle est vide")
        else: #Salle avec un ennemi 
            de = 0
            de = lance_de()
            print(de)
            if de in [1, 2, 3]:
                vie -= 1
                print("Votre vie a atteint ",vie)
                return False
            else:
                print("Bravo (la traversée du niveau a été réussie)")

dungeon(salle)


                






