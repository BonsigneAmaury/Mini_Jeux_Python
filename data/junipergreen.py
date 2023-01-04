def multiple(n, nMax):
    """
    Cette fonction retourne les multiples d'un chiffre n demandé en paramètre et qui sont inférieur à nMax
    :param n: chiffre sur lequel nous recherchons les multiples
    :type n: int
    :param nMax: limite des multiples
    :type nMax: int
    :return: multiples de n inférieur à nMax
    :rtype: list
    Exemple :
    >>> multiple(2, 20)
    [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    """
    multiple = 1
    listOfMultiples = []
    while n * multiple <= nMax:
        listOfMultiples.append(n * multiple)
        multiple += 1
    return listOfMultiples

def divider(n, nMax):
    """
    Cette fonction retourne les diviseurs d'un chiffre n demandé en paramètre et qui sont inférieur à nMax
    :param n: chiffre sur lequel nous recherchons les diviseurs
    :type n: int
    :param nMax: limite des diviseurs
    :type nMax: int
    :return: diviseurs de n inférieur à nMax
    :rtype: list
    Exemple :
    >>> divider(10, 20)
    [1, 2, 5, 10]
    """
    listOfDivider=[]
    for i in range(1, nMax + 1):
        if n % i == 0 and n // i <= nMax:
                listOfDivider.append(i)
    return listOfDivider

def union(listOne, listTwo):
    """
    Cette fonction l'union de deux listes triées
    :param listOne: première liste à unir
    :type listOne: list
    :param listTwo: deuxième liste à unir
    :type listTwo: list
    :return: l'union des deux listes triées
    :rtype: list
    Exemple :
    >>> union([1, 2, 3], [2, 5, 6])
    [1, 2, 2, 3, 5, 6]
    """
    return sorted(listOne + listTwo)

def firstFilter(listOne, listTwo):
    """
    Cette fonction renvoye une liste des nombres présant dans les deux listes données en paramètre
    :param listOne: première liste à filtrer
    :type listOne: list
    :param listTwo: deuxième liste à filtrer
    :type listTwo: list
    :return: liste contenant les nombres présent dans les deux listes
    :rtype: list
    Exemple :
    >>> firstFilter([1, 2, 5, 3], [2, 5, 4])
    [2, 5]
    """
    lisOfFilter = []
    for n in listOne:
        if n in listTwo:
            lisOfFilter.append(n)
    return lisOfFilter

def secondFilter(listOne, listTwo):
    """
    Cette fonction renvoye une liste de nombres présent dans la première mais qui ne sont pas dans la deuxième liste
    :patam listOne: première liste à filtrer
    :type listOne: list
    :param listTwo: deuxième liste à filtrer
    :type listTwo: list
    :return: liste contenant les nombres présent dans la première liste mais qui ne sont pas dans la deuxième liste
    :rtype: list
    Exemple :
    >>> secondFilter([1, 2, 5, 3], [2, 5, 4])
    [1, 3]
    """
    lisOfFilter = []
    for n in listOne:
        if n not in listTwo:
            lisOfFilter.append(n)
    return lisOfFilter

def game(n, nMax):
    """
    Cette fonction permet de jouer au je de juniper green
    :param n: nombre minimum qui peut être jouer par les joueurs 
    :type n: int
    :param nMax: nombre maximum qui peut être jouer pas les joueurs
    :type nMax: int
    Exemple :
    >>> #game(0, 20) // impossible de lancer un doctest car la librairie ne prend pas en compte les inputs
    Posible Numbers :  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    Joueur numéro 2 à vous de jouer        
    Donnez un chiffre pair entre 0 et 20 : 2
    Valide numbers :  [1, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    Numbers Played :  [2]
    Joueur numéro 1 à vous de jouer
    Donnez un chiffre entre 0 et 20 : 4
    Valide numbers :  [1, 8, 12, 16, 20]
    Numbers Played :  [2, 4]
    Joueur numéro 2 à vous de jouer     
    Donnez un chiffre entre 0 et 20 : 8 
    Valide numbers :  [1, 16]
    Numbers Played :  [2, 4, 8]
    Joueur numéro 1 à vous de jouer
    Donnez un chiffre entre 0 et 20 : 16
    Valide numbers :  [1]
    Numbers Played :  [2, 4, 8, 16]
    Joueur numéro 2 à vous de jouer
    Donnez un chiffre entre 0 et 20 : 1
    Valide numbers :  [3, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 17, 18, 19, 20]
    Numbers Played :  [2, 4, 8, 16, 1]
    Joueur numéro 1 à vous de jouer
    Donnez un chiffre entre 0 et 20 : 11
    Joueur 1 a gagné
    """
    whoIsPlaying = True # joueur 1 = true et joueur 2 = false
    possibleNumbers = list(range(n, nMax + 1)) # Créer un liste de n à nMax
    print("Possible Numbers : ", possibleNumbers) # Affiche les différents nombre possible
    valideNumbers = 0 # Initialisation de la variable valideNumbers qui vas nou permettre de récupérer les diviseurs et les multiples du nombre choisie par les joueurs
    getNumber = 0 # Initialisation de la variable getNumber qui vas nous permettre de récupérer la valeur donner par les joeurs
    numbersPlayed = [] # Initialisation de la variable numbersPlayed qui nous permettras de connaitre les nombres joués
    end = False # Initialisation de la variable end, elle nous perettras de savoir si le jeux et fini ou non
    first = 0 # Initialisation de la variable first qui nous permettras de savoir si nous somme au premier tour ou non

    while end != True: # Tant que endun différent de True alors nous jouons
        # Permet de savoir qui joue
        if whoIsPlaying:
            print("Joueur numéro 1 à vous de jouer")
        else:
            print("Joueur numéro 2 à vous de jouer")

        if first == 0: # Permet de sovoir si nous sommes au premier tour
            while True:
                try:
                    getNumber = int(input(f"Donnez un chiffre pair entre {n} et {nMax} : "))
                    while getNumber not in possibleNumbers or getNumber % 2 != 0: # Permet de récuperer un nombre pair qui soit jouable donc >= n et <= nMax
                        getNumber = int(input(f"Le chiffre choisie n'est pas un nombre pair ou n'est pas compris en {n} et {nMax}\nRéssayer : "))
                    break
                except ValueError:
                    print("Veulliez entrer un nombre entier")
            first += 1
        else:
            getNumber = int(input(f"Donnez un chiffre entre {n} et {nMax} : "))
            while getNumber in numbersPlayed or getNumber not in possibleNumbers: # Permet de savoir si le nombre est possible
                    getNumber = int(input(f"Le chiffre choisie n'est compris en {n} et {nMax} ou a déja été utilisé\nRéssayer : "))
        
        possibleNumbers.remove(getNumber)
        numbersPlayed.append(getNumber)
        sorted(numbersPlayed)

        valideNumbers = secondFilter(firstFilter(possibleNumbers, union(multiple(getNumber, nMax), divider(getNumber, nMax))), numbersPlayed)

        if valideNumbers == []:
            end = True
        else:
            print("Valide numbers : ", valideNumbers) # Permet de connaitre les chiffres jouables
            print("Numbers Played : ", numbersPlayed) # Permet de savoir les chiffres joués
            whoIsPlaying = not whoIsPlaying

    if whoIsPlaying:
        return print("Joueur 1 a gagné")
    return print("Joueur 2 a gagné")

if __name__ == "__main__":
    import doctest
    doctest.testmod()