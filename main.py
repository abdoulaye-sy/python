# Afficher le plateau
def afficher_plateau(plateau):
    for ligne in plateau:
        print(" | ".join(ligne))
        print("-" * 5)

# Initialiser un plateau vide
def initialiser_plateau():
    return [[" " for _ in range(3)] for _ in range(3)]

# Demander au joueur une position valide
def demander_position(joueur, plateau):
    while True:
        try:
            position = input(f"Joueur {joueur}, entrez votre position (ligne, colonne) : ")
            ligne, colonne = map(int, position.split(","))
            
            # Vérifier si la position est dans les limites du plateau
            if ligne < 0 or ligne > 2 or colonne < 0 or colonne > 2:
                print("Position hors du plateau. Essayez encore.")
                continue

            # Vérifier si la case est libre
            if plateau[ligne][colonne] != " ":
                print("Cette case est déjà prise. Choisissez une autre case.")
                continue

            return ligne, colonne
        except ValueError:
            print("Entrée invalide. Entrez deux nombres séparés par une virgule (exemple : 1,2).")

# Permettre à un joueur de jouer son tour
def jouer_tour(joueur, plateau):
    ligne, colonne = demander_position(joueur, plateau)
    plateau[ligne][colonne] = joueur

# Vérifier si un joueur a gagné
def verifier_victoire(plateau, joueur):
    # Vérifier les lignes
    for ligne in plateau:
        if all(case == joueur for case in ligne):
            return True

    # Vérifier les colonnes
    for col in range(3):
        if all(plateau[ligne][col] == joueur for ligne in range(3)):
            return True

    # Vérifier la diagonale principale
    if all(plateau[i][i] == joueur for i in range(3)):
        return True

    # Vérifier la diagonale secondaire
    if all(plateau[i][2 - i] == joueur for i in range(3)):
        return True

    return False

# Vérifier si la partie est un match nul
def verifier_match_nul(plateau):
    return all(case != " " for ligne in plateau for case in ligne)

# Boucle principale pour jouer au jeu
def jouer_tic_tac_toe():
    plateau = initialiser_plateau()
    joueur_actuel = "X"

    while True:
        afficher_plateau(plateau)
        print(f"Tour du joueur {joueur_actuel}")

        jouer_tour(joueur_actuel, plateau)

        # Vérifier si le joueur actuel gagne
        if verifier_victoire(plateau, joueur_actuel):
            afficher_plateau(plateau)
            print(f"Félicitations ! Le joueur {joueur_actuel} a gagné !")
            break

        # Vérifier si la partie est un match nul
        if verifier_match_nul(plateau):
            afficher_plateau(plateau)
            print("Match nul !")
            break

        # Passer au joueur suivant
        joueur_actuel = "O" if joueur_actuel == "X" else "X"

# Lancer le jeu
jouer_tic_tac_toe()
