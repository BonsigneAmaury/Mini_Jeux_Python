from random import *

def allumette():
    """programme du jeu des allumettes

    Returns:
        [char]: retourne la chaine de caractère pour savoir quelle joueur a gagner
    """    
    liste=['I']*21#liste d'allumette afficher a l'ecran
    comp=0#compteur qui determine quel joueur joue (0 j1 joue 1j2 joue)
    chiffre =[1, 2, 3]#liste de reponse possible pour les allumette
    while len(liste)>0:
        if comp==0:#decision :j1 joue
            total = "".join(liste)
            print(total)#affichage de la liste sans les point les parenthese ect
            print('j1 joue')
            a=int(input("combien d'allumette retirer: "))#entrer le nb d'allumette
            comp+=1
            while a not in chiffre:
                print('erreur, nb entre 1 et 3')#boucle qui verifie que le nb choisi est bien dans les regle
                a=int(input("combien d'allumette retirer: "))
            while a>0 and len(liste)>0:#boucle qui delete des allumette dans la liste
                liste.pop()
                a-=1
        else:
            total = "".join(liste)#affichage comme plus haut
            print(total)
            print('j2 joue')
            a=int(input("combien d'allumette retirer: "))#demande du nb a retirer pour le j2
            comp-=1
            while a not in chiffre:
                print('erreur, nb entre 1 et 3')
                a=int(input("combien d'allumette retirer: "))
            while a>0 and len(liste) >0:
                liste.pop()
                a-=1

    if len(liste)==0 and comp==0:#verification de quel joueur a gagner 
        return print('victoire j1')
    elif len(liste)==0 and comp==1:
        return print('victoire j2')

def allumette_bot():
    """programme du jeu des allumettes contre l'ordinateur

    Returns:
        [char]: retourne la chaine de caractère pour savoir si l'on a gagner
    """    
    liste=['I']*21#creation liste d'allumette
    comp=0
    chiffre =[1, 2, 3]
    while len(liste)>0:
        if comp==0:
            total = "".join(liste)#affichage liste
            print(total)
            print('j1 joue')
            a=int(input("combien d'allumette retirer: "))#nb d'allumette a delete
            comp+=1
            while a not in chiffre:#boucle qui verifie que le nb d'allulette choisis est reglementaire
                print('erreur, nb entre 1 et 3')
                a=int(input("combien d'allumette retirer: "))
            while a>0 and len(liste)>0:#boucle qui delete les allumette
                liste.pop()
                a-=1
        else:
            total = "".join(liste)
            print(total)#affichage liste 
            print('ordi joue')
            if len(liste)>3:
                a= chiffre[randint(0,2)]#choix d'un nb d'aleatoire d'allumette a virer
            elif len(liste) == 3:#si il y en a 3 on en retire 2 afin de gagner, 2 on en retire 1 et 1 est la defaite
                a = 2
            elif len(liste)== 2:
                a = 1
            elif len(liste) == 1:
                a = 1
            comp-=1
            while a>0 and len(liste) >0:#boucle qui delete les allumette
                liste.pop()
                a-=1
        
    if len(liste)==0 and comp==0:#verification de qui a gagner 
        return print('victoire j1')
    elif len(liste)==0 and comp==1:
        return print('victoire ordi')
