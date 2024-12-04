# Fichier : ia.py

import random

def choix_aleatoire(plateau):
    """
    L'IA choisit une case libre au hasard.
    """
    cases_libres = [
        (i, j)
        for i in range(3)
        for j in range(3)
        if plateau[i][j] == " "
    ]
    if cases_libres:
        return random.choice(cases_libres)
    return None
