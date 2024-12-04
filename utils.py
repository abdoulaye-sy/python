# Fichier : utils.py

def creer_plateau():
    """
    Crée un plateau vide de 3x3 pour le jeu.
    """
    return [[" " for _ in range(3)] for _ in range(3)]

def afficher_plateau(plateau):
    """
    Affiche le plateau du jeu.
    """
    for ligne in plateau:
        print(" | ".join(ligne))
        print("-" * 9)

def verifier_victoire(plateau, joueur):
    """
    Vérifie si le joueur a gagné (ligne, colonne ou diagonale).
    """
    for ligne in plateau:  # Vérifie les lignes
        if ligne.count(joueur) == 3:
            return True

    for col in range(3):  # Vérifie les colonnes
        if [plateau[0][col], plateau[1][col], plateau[2][col]].count(joueur) == 3:
            return True

    # Vérifie les diagonales
    if [plateau[0][0], plateau[1][1], plateau[2][2]].count(joueur) == 3:
        return True
    if [plateau[0][2], plateau[1][1], plateau[2][0]].count(joueur) == 3:
        return True

    return False

def plateau_rempli(plateau):
    """
    Vérifie si toutes les cases sont remplies.
    """
    for ligne in plateau:
        if " " in ligne:
            return False
    return True
