import random

def generer_niveau():
    liste = [random.choice([0, 1]) for i in range(20)]
    return liste

def lance_de():
    return random.randint(1, 6)


#salle = generer_niveau()
#print(salle)

#for i in range(3): 
#    print(generer_niveau())

def dungeon(salle):
    vie = 1
    for o in salle:
        if o == 0: #Salle sans ennemi
            #print("La salle est vide")
            pass
        else: #Salle avec un ennemi 
            de = 0
            de = lance_de()
            #print(de)
            if de in [1, 2, 3]:
                vie -= 1
                #print("Votre vie a atteint ",vie)
            else:
                #print("Bravo (la traversée du niveau a été réussie)")
                pass
    if vie<=0:
        #print("Votre vie à atteints ",vie,", vous êtes mort dans le dungeon")
        return False
    else:
        #print("Bravo vous avez réussit la traverser du dungeon")
        return True
        
#print(dungeon(salle))

def main():
    nombre_de_dungeon = 0
    dungeon_passer = False
    while not dungeon_passer:
        nombre_de_dungeon = nombre_de_dungeon + 1
        salle = 0
        salle = generer_niveau()
        print(salle)
        dungeon_passer=dungeon(salle)
    print("Jeu terminé ! ",nombre_de_dungeon, " niveaux traversés avant de réussir")
    
main()


                






