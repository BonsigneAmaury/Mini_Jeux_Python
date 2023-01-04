import random

def getPosTresor():
    """
    Cette fonction permet de renvoyer un tuple de deux valeurs random entre 0 et 100 inclus
    """
    return (random.randint(0, 100), random.randint(0, 100))

def playerGame():
    # Nous récupérons les coordonnées du trésor
    posTresor = getPosTresor()
    counter = 0
    while True:
        while True:
            # Le joueur propose des coordonnées
            posSearch = tuple(int(x) for x in input("Donnez les coordonnées de recherche (x,y) : ").split(","))
            # Nous vérifions si les coordonnées sont bien dans l'intervale [0, 100]
            if posSearch[0] > 100 or posSearch[0] < 0 or posSearch[1] > 100 or posSearch[1] < 0:
                print("Le chiffre demandé doit être contenu entre 0 et 100 inclus")
            else:
                break

        counter += 1
        # Nous vérifions si le joueur a trouver les coordonnées du trésor ou non
        if posSearch[0] == posTresor[0] and posSearch[1] == posTresor[1]:
            return print("Vous avez gagné")

        # Nous vérifions si le nombre de coups n'est pas dépassé
        if counter >= 10:
            return print("Vous avez dépassé le nombre maximum d'éssais. Perdu !!!")

        # Sinon nous aidons les joueurs en lui indiquant si il doit aller à droite ou à gauche et en haut ou en bas en fonction des c'est réponse
        elif posSearch[0] > posTresor[0]:
            print("Plus à gauche")
        elif posSearch[0] < posTresor[0]:
            print("Plus à droite")
        if posSearch[1] > posTresor[1]:
            print("Plus en bas")
        elif posSearch[1] < posTresor[1]:
            print("Plus en haut")

def botGame(posSearchRangeX, posSearchRangeY, posTresor, counter = 0):
    """
    Cette fonction permet faire rechercher un chiffre entré en paramètre par l'utilisateur par un bot
    :param posSearchRangeX: liste de recherche sur l'axe de X
    :type posSearchRangeX: list
    :param posSearchRangeY: liste de recherche sur l'axe de Y
    :type posSearchRangeY: list
    :param posTresor: coordonnées du trésor
    :type posTresor: tuple
    :param counter: nombre de coups
    :type counter: int
    :return: la victoire ou la defaite de l'ordinateur
    :rtype: string
    """

    # Cette partie du programme permet de prendre la valeur qui se trouve au milieu des listes posSearchX et posSearchY
    if len(posSearchRangeX) % 2 == 0: # On regarde si la taille de la liste est pair ou inpair
        posSearchBot = (len(posSearchRangeX) // 2 + posSearchRangeX[0], 0) # Si pair allors nous allons prendre le chiffre de la division entière par 2
    else:
        posSearchBot = (len(posSearchRangeX) // 2 + posSearchRangeX[0] + 1, 0) # Sinon cela voudras dire que la taille de la liste est inpair donc nous allons récupérer le valeur de la division entière par 2 et nous allons lui rajouter 1 pour récupérer la valeur du milieu
    # Pareil que haut-dessus mais en utilisant la liste posSearchY
    if len(posSearchRangeY) % 2 == 0:
        posSearchBot = (posSearchBot[0], len(posSearchRangeY) // 2 + posSearchRangeY[0])
    else:
        posSearchBot = (posSearchBot[0], len(posSearchRangeY) // 2 + posSearchRangeY[0] + 1)

    print(posTresor)
    print(posSearchBot)

    # Nous devons vérifier si le nombre de coup ne dépasse pas 10 (le nombre d'essai max)
    if counter >= 10:
        return print("Le bot a perdu")
    # Nous vérifions ici si le tuple posSearchBot est égal au tuple posTrésor pour savoir savoir si le bot a trouvé la position du trésor 
    if posSearchBot == posTresor:
        return print("Le bot a gagner")
    
    ### Ces deux petite boucle for permette de récupérer les index des tuple contenu dans la variable posSearchBot, afin de renvoyer la partie gauche ou droite de la liste
    xIndex = 0; yIndex = 0
    for x in range(len(posSearchRangeX)):
        if posSearchRangeX[x] == posSearchBot[0]:
            xIndex = x
    for y in range(len(posSearchRangeY)):
        if posSearchRangeY[y] == posSearchBot[1]:
            yIndex = y
    ###

    # Permet de récupérer la réponse de l'utilisateur et la transformer en tuple
    answer = tuple(x for x in input("gauche ou droite ou trouve et haut ou bas ou touve  (gauche,bas) ou (trouve,haut) : ").split(","))

    # Vérifie les ajustements qu'il faut réalisé sur les différentes listes
    if answer[0] == "gauche": # Si gauche nous allons renvoyer la partie gauche de la liste
        posSearchRangeX = posSearchRangeX[:xIndex]
    elif answer[0] == "droite": # Si droite nous allons renvoyer la pertie droite de la liste
        posSearchRangeX = posSearchRangeX[xIndex:]
    if answer[1] == "haut": # Si haut nous allons renvoyer la pertie droite de la liste
        posSearchRangeY = posSearchRangeY[yIndex:]
    elif answer[1] == "bas": # Si bas nous allons renvoyer la pertie gauche de la liste
        posSearchRangeY = posSearchRangeY[:yIndex]
    elif answer[0] != "trouve" and answer[1] != "trouve": # Si non trouve allors il y a une erreur, donc nous ne faisons aucune modification sur les listes
        print("mauvaise commande")
    return botGame(posSearchRangeX, posSearchRangeY, posTresor, counter + 1)


