# Fichier : joueur_humain.py

def demander_choix(joueur, plateau):
    """
    Demande au joueur de choisir une case libre sur le plateau.
    """
    while True:
        try:
            choix = int(input(f"Joueur {joueur}, entrez un chiffre (1-9) : "))
            if choix < 1 or choix > 9:
                print("Choisissez un chiffre entre 1 et 9.")
                continue

            ligne = (choix - 1) // 3
            colonne = (choix - 1) % 3

            if plateau[ligne][colonne] == " ":
                return ligne, colonne
            else:
                print("Cette case est déjà prise.")
        except ValueError:
            print("Veuillez entrer un chiffre valide.")
