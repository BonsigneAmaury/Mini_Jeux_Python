import random

def juste_prix():
    """Programme d'un jeu qui consiste a deviner un nombre compris entre 1 et 1000 en moins de 10 essais

    Returns:
        [char]: retourne la chaine de caractère pour savoir si l'on a gagner 
    """    
    prix = random.randint(1,1000)
    # chiffre aleatoire choisis par le pc
    choix_joueur = 0
    nb_reponse = 0
    while choix_joueur != prix:

        # Tant que le chiffre du joueur n'est pas egale a celui du pc, le pc lui donne des indication et le joueur rechoisis un prix
        choix_joueur = int(input('devinez le chiffre: '))
        if choix_joueur > prix:
            print("c'est moins")
        elif choix_joueur < prix:
            print("c'est plus") 
        nb_reponse +=1 # Compteur du nb de reponse
        print("vous avez répondu", nb_reponse, "fois")
        if nb_reponse >= 10 and choix_joueur != prix:
            print("c'est perdu")
            return "c'est perdu" # Defaite si nb de reponse depasser 



    if choix_joueur == prix:
        print("c'est gagner")
        return 'Gagner' # Condition de victoire

def juste_prix_pc(liste_prix, prix_joueur, nb_reponse):
    """Programme d'un jeu qui consiste a faire deviner un nombre compris entre 1 et 1000 
    a un ordinateur 

    Args:
        liste_prix ([list]): liste dans laquelle se trouve le prix
        prix_joueur ([int]): Nombre que l'ordinateur doit trouver 
        nb_reponse ([int]): Nombre d'essais

    Returns:
        [char]: retourne la chaine de caractère pour savoir si l'on a gagner 
    """    
    prix_ordi = liste_prix[len(liste_prix) // 2]
    print(prix_joueur)
    print(prix_ordi)
    index = 0
    if prix_ordi == prix_joueur: # condition victoire
        print('victoire du bot')
        return 'victoire ordinateur'
    elif nb_reponse == 10: # condition defaite
        print('défaite du bot')
        return 'defaite ordinateur'
    reponse = input("c'est plus ou c'est moins: ") # on demande au joueur si le prix de l'ordi est superieur ou inferieur au prix du joueur 
    nb_reponse +=1 # compteur nb de reponse max
    print("Nombre de réponse totale : ", nb_reponse)

    for x in range(len(liste_prix)): # recherche de l'index lieer au prix dans la liste
        if liste_prix[x] == prix_ordi:
            index = x

    if reponse == "c'est moins":
        return juste_prix_pc(liste_prix[:index], prix_joueur,nb_reponse) # on relance la fonction sans la partie de la liste superieur au prix deviner par le pc
    elif reponse == "c'est plus":
        return juste_prix_pc(liste_prix[index+1:], prix_joueur,nb_reponse) # relance la fonction sans la partie de la liste inferieur au prix
    else:
        print('mauvaise commande') # en cas d'erreur dans la reponse c'est plus ou c'est moins on relance sans rien changer 
        return juste_prix_pc(liste_prix, prix_joueur,nb_reponse)