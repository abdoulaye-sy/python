# === Partie Utils ===
def creer_plateau():
    return [[" " for _ in range(3)] for _ in range(3)]

def afficher_plateau(plateau):
    for ligne in plateau:
        print(" | ".join(ligne))
        print("-" * 9)

def verifier_victoire(plateau, joueur):
    for ligne in plateau:
        if ligne.count(joueur) == 3:
            return True
    for col in range(3):
        if [plateau[0][col], plateau[1][col], plateau[2][col]].count(joueur) == 3:
            return True
    if [plateau[0][0], plateau[1][1], plateau[2][2]].count(joueur) == 3:
        return True
    if [plateau[0][2], plateau[1][1], plateau[2][0]].count(joueur) == 3:
        return True
    return False

def plateau_rempli(plateau):
    for ligne in plateau:
        if " " in ligne:
            return False
    return True

# === Partie Joueur Humain ===
def demander_choix(joueur, plateau):
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

# === Partie IA ===
import random
def choix_aleatoire(plateau):
    cases_libres = [
        (i, j)
        for i in range(3)
        for j in range(3)
        if plateau[i][j] == " "
    ]
    if cases_libres:
        return random.choice(cases_libres)
    return None

# === Partie Jeu Principal ===
def jouer():
    plateau = creer_plateau()
    joueur_humain = "X"
    joueur_ia = "O"

    print("Bienvenue dans le jeu du morpion !")
    afficher_plateau(plateau)

    while True:
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
