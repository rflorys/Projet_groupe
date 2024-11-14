import random

def generer_niveau():
    """Génère un niveau avec 20 salles"""
    niveau = [random.choice([0, 1]) for i in range(20)]
    return  niveau

def lance_de():
    """Retourne un lancer de dé à 6 faces."""
    return random.randint(1, 6)

def traverse_niveau(niveau):
    """Traverse le niveau et réduit la vie si un ennemi est rencontré."""
    vie = 1
    for salle in niveau:
        if salle == 1 and lance_de() in [1, 2, 3]:  # Perte de vie sur 1, 2 ou 3
            vie -= 1
            if vie <= 0:
                return False
    return True

def main():
    """Relance une tentative tant qu'un niveau n'a pas été réussi"""
    niveaux_tentatives = 0
    dungeon_reussi = False
    while not dungeon_reussi:
        niveaux_tentatives += 1
        niveau = generer_niveau()
        print(niveau)
        dungeon_reussi = traverse_niveau(niveau)
    print("Jeu terminé ! ",niveaux_tentatives, " niveaux traversés avant de réussir")
    
main()


                






