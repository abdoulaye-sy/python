# Fichier : jeu_principal.py

from utils import creer_plateau, afficher_plateau, verifier_victoire, plateau_rempli
from joueur_humain import demander_choix
from ia import choix_aleatoire

def jouer():
    """
    Gère le déroulement du jeu entre le joueur humain et l'IA.
    """
    plateau = creer_plateau()
    joueur_humain = "X"
    joueur_ia = "O"

    print("Bienvenue dans le jeu du morpion !")
    afficher_plateau(plateau)

    while True:
        # Tour du joueur humain
        print("Votre tour !")
        ligne, colonne = demander_choix(joueur_humain, plateau)
        plateau[ligne][colonne] = joueur_humain

        afficher_plateau(plateau)

        if verifier_victoire(plateau, joueur_humain):
            print("Félicitations ! Vous avez gagné !")
            break

        if plateau_rempli(plateau):
            print("Match nul !")
            break

        # Tour de l'IA
        print("Tour de l'ordinateur...")
        ligne, colonne = choix_aleatoire(plateau)
        plateau[ligne][colonne] = joueur_ia

        afficher_plateau(plateau)

        if verifier_victoire(plateau, joueur_ia):
            print("L'ordinateur a gagné. Bonne chance la prochaine fois !")
            break

        if plateau_rempli(plateau):
            print("Match nul !")
            break

if __name__ == "__main__":
    jouer()
