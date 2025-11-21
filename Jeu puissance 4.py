# PROJET PUISSANCE 4
# Binôme : Paul
# - Fievet Thibaud 
# - linktevoet Paul

def creer_grille():
    """
    Crée la grille (6 lignes, 7 colonnes).
    
    :return: (list) la grille
    """
    grille = []
    
    for i in range(6):
        ligne = [0 for x in range(7)]
        grille.append(ligne)
        
    return grille

def afficher_grille(grille):
    """
    Affiche la grille.
    
    :param grille: (list) la grille
    """
    for ligne in grille:
        print("| ", end="")
        
        for case in ligne:
            print(case, end=" | ")
        print()
        
    print("-" * 29)

def verifie_colonne(grille, numero_colonne):
    """
    Vérifie s'il reste de la place dans la colonne,
    c'est-à-dire si la case du haut est vide.
    
    :param grille: (list) la grille
    :param numero_colonne: (int) la colonne à regarder
    """
    assert 0 <= numero_colonne <= 6
    
    if grille[0][numero_colonne]  != 0:
        resultat = False
    else:
        resultat = True
        
    return resultat

def place_jeton(grille, numero_colonne, jeton):
    """
    Place le jeton dans la colonne.
    
    :param grille: (list) la grille
    :param numero_colonne: (int) la colonne où placer le jeton
    :param jeton: (int) le jeton (1 ou 2)
    :return: (list) la grille modifiée
    """
    assert verifie_colonne(grille, numero_colonne) == True
    
    for i in range(5, 0-1, -1):
        if grille[i][numero_colonne] == 0:
            grille[i][numero_colonne] = jeton
            return grille

def ligne_gagnante(grille, jeton):
    """
    Indique si une des lignes est gagnante,
    c'est-à-dire s'il y a 4 jetons d'affilés.
    
    :param grille: (list) la grille
    :param jeton: (int) le jeton (1 ou 2)
    :return: (bool) True s'il y a une ligne gagnante, False sinon
    """
    for ligne in grille:
        nombre_daffile=0
        for case in ligne:
            if case == jeton:
                nombre_daffile=nombre_daffile+1
            else:
                nombre_daffile = 0
            if nombre_daffile==4:
                resultat= True
    return resultat

def colonne_gagnante(grille, jeton):
    """
    Indique si une des colonnes est gagnante,
    c'est-à-dire s'il y a 4 jetons d'affilée.
    
    :param grille: (list) la grille
    :param jeton: (int) le jeton (1 ou 2)
    :return: (bool) True s'il y a une colonne gagnante, False sinon
    """
    for colonne in range(7):
        nombre_daffile = 0
        for ligne in range(6):
            case=grille[ligne][colonne]
            if case == jeton:
                nombre_daffile=nombre_daffile+1
            else:
                nombre_daffile=0
            if nombre_daffile==4:
                resultat=True
    return resultat
def diagonale_gagnante(grille, jeton):
    """
    Indique si une des diagonales est gagnante,
    c'est-à-dire s'il y a 4 jetons d'affilée.
    
    :param grille: (list) la grille
    :param jeton: (int) le jeton (1 ou 2)
    :return: (bool) True s'il y a une diagonale gagnante, False sinon
    """
    return False
#     nombre_daffile=0
#     for diagonalle in range[(6,0-1,-1)][ligne]:
#         for ligne in range[(5,0-1,-1)][ligne]:
#             case=grille[ligne][colonne]
#             if case == jeton:
#                 nombre_daffile=nombre_daffile+1
#         if nombre_daffile==4:
#             resultat=True
#         else:
#             resultat=False
#         nombre_daffile=0
#     return resultat
def effectuer_coup(grille, joueur, jeton):
    """
    Effectue un coup pour le joueur en paramètre.
    
    :param grille: (list) la grille
    :param joueur: (str) le nom du joueur
    :param jeton: (int) le jeton du joueur (1 ou 2)
    :return: (list) la nouvelle grille
    """
    print("Tour de", joueur)
    valide = False
    while not valide:
        saisie = input("Entrez un numéro de colonne (0-6) : ")
        numero_colonne = int(saisie)

        if 0 <= numero_colonne <= 6:
            if verifie_colonne(grille, numero_colonne):
                valide = True
            else:
                print("Colonne pleine, essayez une autre.")
        else:
            print("Erreur : Le chiffre doit être entre 0 et 6.")
        
    grille = place_jeton(grille, numero_colonne, jeton)
    return grille
def jouer():
    """
    Lance une partie.
    
    :return: (str) le nom du vainqueur (ou égalité)
    """
    joueur1 = input("Nom joueur1 : ")
    joueur2 = input("Nom joueur2 : ")
    dico_jetons = {1 : joueur1, 2 : joueur2}
    
    grille = creer_grille()
    afficher_grille(grille)
    
    for tour in range(1,21+1):
        for jeton in dico_jetons.keys():
            joueur = dico_jetons[jeton]
            
            grille = effectuer_coup(grille, joueur, jeton)
            afficher_grille(grille)
            
            if ligne_gagnante(grille, jeton) or colonne_gagnante(grille, jeton) or diagonale_gagnante(grille,jeton):
                return "Victoire de " + joueur
                
    return "Egalité"

jouer()