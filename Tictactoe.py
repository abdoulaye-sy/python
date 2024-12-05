# Création du plateau avec 9 cases
plateau = [' '] * 9

# Affichage du plateau
def affichage_plateau():
    print(f"| {plateau[0]} | {plateau[1]} | {plateau[2]} |")
    print("-------------")
    print(f"| {plateau[3]} | {plateau[4]} | {plateau[5]} |")
    print("----------")
    print(f"| {plateau[6]} | {plateau[7]} | {plateau[8]} |")

# Choix de case pour jouer
def jouer(joueur):
    affichage_plateau()  # Affiche le plateau au début du tour

    choix = input(f"Joueur {joueur}, Choisis un numéro de case entre 1 et 9 : ")

    if choix.isdigit():  # Vérifie que l'entrée est un nombre
        choix = int(choix) - 1  # Convertit en index (0 à 8)
        if 0 <= choix <= 8:  # Vérifie que l'index est dans les limites
            if plateau[choix] == ' ':  # Vérifie que la case est vide
                plateau[choix] = joueur  # Place 'X' sur la case choisie
                return  # Sort de la fonction après un choix valide
            else:
                print("Case déjà occupée ! Choisis une autre case.")
        else:
            print("Numéro invalide ! Choisis un numéro entre 1 et 9.")
    else:
        print("Entrée invalide ! Merci de rentrer un nombre.")

    jouer(joueur)  # Redemande un choix en cas d'erreur

# Vérification de victoire
def verifier_victoire():
    combinaisons_gagnantes = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Lignes
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colonnes
        [0, 4, 8], [2, 4, 6]              # Diagonales
    ]
    for combinaison in combinaisons_gagnantes:
        if plateau[combinaison[0]] == plateau[combinaison[1]] == plateau[combinaison[2]] != ' ':
            return True
    return False

# Jeu principal
if joueur_actuel == 'X':
    pass
else:
     joueur_actuel = 'O'
    

while True:
    jouer(joueur_actuel)
    if verifier_victoire():
        affichage_plateau()
        print(f"Victoire {joueur_actuel}, félicitations !")
        break
    elif ' ' not in plateau:  # Si le plateau est plein sans victoire
        affichage_plateau()
        print("Match nul !")
        break

#joueur_actuel = 'O' if joueur_actuel == 'X' else 'X'