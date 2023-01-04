import random

def initGrid(numberOfLetter, nbLines, nbColumns):
    """Programme qui permet d'initialiser la grille de jeu 

    Args:
        numberOfLetter ([int]): Nombre de lettres
        nbLines ([int]): nombre de ligne
        nbColumns ([int]): nombre de colonnes

    Returns:
        [list]: renvoie la grille de jeu 
    """    
    if nbLines * nbColumns % 2 == 0 and 2 * numberOfLetter <= nbLines * nbColumns or (nbLines * nbColumns) / numberOfLetter % 2 == 0:
        letters = ["A", "B", "C", "D", "E", "F", "G"]
        grid = [[0 for x in range(nbColumns)] for y in range(nbLines)]
        number = int((nbLines * nbColumns) / numberOfLetter)
        maxLetter = letters[numberOfLetter]
        t = 0; lim = 0
        for x in range(nbLines):
            for y in range(nbColumns):
                if letters[t] != maxLetter:
                    if 0 in grid[x]:
                        grid[x][y] = letters[t]
                        lim += 1
                        if lim == number:
                            t +=1
                            lim = 0
        return grid
    return False

def shuffle(grid):
    """programme qui melanges les valeurs de la grille

    Args:
        grid ([list]): grille de jeu 

    Returns:
        [list]: Grille de jeu dont toutes les valeurs sont mélangées
    """    
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            n = [random.randint(0, len(grid) - 1), random.randint(0, len(grid) - 1)]
            m = [random.randint(0, len(grid) - 1), random.randint(0, len(grid) - 1)]
            grid[n[0]][n[1]], grid[m[0]][m[1]] = grid[m[0]][m[1]], grid[n[0]][n[1]]
    return grid

def initMarked(nbLines, nbColumns):
    """programme qui iniatilise une liste ou toutes les valeurs sont en false

    Args:
        nbLines ([int]): nombre de ligne
        nbColumns ([int]): nombre de colonne 

    Returns:
        [list]: liste ou toute les valeurs sont False
    """    
    return [[False for x in range(nbColumns)] for y in range(nbLines)]

def display(grid, marked):
    """gere l'affichage de la liste de jeu

    Args:
        grid ([list]): liste de jeu 
        marked ([list]): Liste ou toutes les valeurs sont falses
    """    
    line = ""
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if marked[x][y]:
                line += grid[x][y]
            else:
                line += "?"
            line += " "
        print(line)
        line = ""

def getInput(visible):
    """permet de recuperer le nombre de lignes et de colonnes

    Args:
        visible ([couple]): couple de coordonés 

    Returns:
        [int]: Couple de coordonnées
    """    
    line = -1; column = -1; available = False
    while available == False:
        try:
            line = int(input(f"Numéro de la lignes compris entre 1, {len(visible)}: ")) - 1
            if line >= 0 and line <= len(visible):
                available = True
            else:
                print("Numéro de ligne non valide")
        except ValueError:
            print("Veulliez entrer un nombre entier ")
    available = False
    while available == False:
        try:
            column = int(input(f"Numéro de la colonne compris entre 1, {len(visible[0])}: ")) - 1
            if column >= 0 and column <= len(visible[0]):
                available = True
            else:
                print("Numéro de colonne non valide")
        except ValueError:
            print("Veulliez entrer un nombre entier ")
    return (line, column)

def askPosition(visible):
    """[summary]

    Args:
        visible ([couple]): couple de coordonnés

    Returns:
        [int]: Couple de coordonnées
    """    
    line, column = getInput(visible)
    if visible[line][column]:
        return ()
    return (line, column)


def checkWin(marked):
    """
    Cette fonction permet de savoir si la partie est finie ou non
    :param marked: grid des cases visible est non visible
    :type marked: list
    :return: true si toute les cartes sont retournées et false sinon
    :rtype: bool
    """
    for x in range(len(marked)):
        for y in range(len(marked[0])):
            if marked[x][y] != True:
                return False
    return True

def main():
    """
    Cette fonction permet de jouer au jeu du memory
    >>> # main() // impossible de lancer un doctest car la librairie ne prend pas en compte les inputs
    Initialisation :
    ______________________
    Nombre de joueurs : 2 
    Nombre de lettres : 2
    Nombre de lignes : 4
    Nombre de column : 4
    Jeu
    _______________
    Score :  [0, 0]
    ? ? ? ?
    ? ? ? ?
    ? ? ? ?
    ? ? ? ?
    Joueur n°1
    Numéro de la lignes compris entre 1, 4: 1
    Numéro de la colonne compris entre 1, 4: 1
    B ? ? ?
    ? ? ? ?
    ? ? ? ?
    ? ? ? ?
    Numéro de la lignes compris entre 1, 4: 1
    Numéro de la colonne compris entre 1, 4: 2
    B A ? ?
    ? ? ? ?
    ? ? ? ?
    ? ? ? ?
    Joueur n°2
    Numéro de la lignes compris entre 1, 4: 2
    Numéro de la colonne compris entre 1, 4: 2
    ? ? ? ?
    ? B ? ?
    ? ? ? ?
    ? ? ? ?
    Numéro de la lignes compris entre 1, 4: 1
    Numéro de la colonne compris entre 1, 4: 1
    B ? ? ?
    ? B ? ?
    ? ? ? ?
    ? ? ? ?
    Joueur n°1
    Numéro de la lignes compris entre 1, 4: 2
    Numéro de la colonne compris entre 1, 4: 1
    B ? ? ?
    B B ? ?
    ? ? ? ?
    ? ? ? ?
    Numéro de la lignes compris entre 1, 4: 1
    Numéro de la colonne compris entre 1, 4: 3
    B ? A ?
    B B ? ?
    ? ? ? ?
    ? ? ? ?
    Joueur n°2
    Numéro de la lignes compris entre 1, 4: 1
    Numéro de la colonne compris entre 1, 4: 2
    B A ? ?
    ? B ? ?
    ? ? ? ?
    ? ? ? ?
    Numéro de la lignes compris entre 1, 4: 1
    Numéro de la colonne compris entre 1, 4: 3
    B A A ? 
    ? B ? ? 
    ? ? ? ? 
    ? ? ? ?
    Joueur n°1
    Numéro de la lignes compris entre 1, 4: 1
    Numéro de la colonne compris entre 1, 4: 4
    B A A A 
    ? B ? ?
    ? ? ? ?
    ? ? ? ?
    Numéro de la lignes compris entre 1, 4: 2
    Numéro de la colonne compris entre 1, 4: 3
    B A A A 
    ? B B ?
    ? ? ? ?
    ? ? ? ?
    Joueur n°2
    Numéro de la lignes compris entre 1, 4: 2
    Numéro de la colonne compris entre 1, 4: 1
    B A A ? 
    B B ? ?
    ? ? ? ?
    ? ? ? ?
    Numéro de la lignes compris entre 1, 4: 2
    Numéro de la colonne compris entre 1, 4: 3
    B A A ? 
    B B B ?
    ? ? ? ?
    ? ? ? ?
    Joueur n°1
    Numéro de la lignes compris entre 1, 4: 2
    Numéro de la colonne compris entre 1, 4: 4
    B A A ? 
    B B B B
    ? ? ? ?
    ? ? ? ?
    Numéro de la lignes compris entre 1, 4: 3
    Numéro de la colonne compris entre 1, 4: 1
    B A A ? 
    B B B B
    A ? ? ?
    ? ? ? ?
    Joueur n°2
    Numéro de la lignes compris entre 1, 4: 3
    Numéro de la colonne compris entre 1, 4: 1
    B A A ? 
    B B B ?
    A ? ? ?
    ? ? ? ?
    Numéro de la lignes compris entre 1, 4: 1
    Numéro de la colonne compris entre 1, 4: 4
    B A A A 
    B B B ?
    A ? ? ?
    ? ? ? ?
    Joueur n°1
    Numéro de la lignes compris entre 1, 4: 3
    Numéro de la colonne compris entre 1, 4: 2
    B A A A
    B B B ? 
    A B ? ?
    ? ? ? ?
    Numéro de la lignes compris entre 1, 4: 2
    Numéro de la colonne compris entre 1, 4: 4
    B A A A
    B B B B 
    A B ? ?
    ? ? ? ?
    Joueur n°2
    Numéro de la lignes compris entre 1, 4: 3
    Numéro de la colonne compris entre 1, 4: 3
    B A A A 
    B B B B
    A B A ?
    ? ? ? ?
    Numéro de la lignes compris entre 1, 4: 3
    Numéro de la colonne compris entre 1, 4: 4
    B A A A 
    B B B B
    A B A A
    ? ? ? ?
    Joueur n°1
    Numéro de la lignes compris entre 1, 4: 4
    Numéro de la colonne compris entre 1, 4: 1
    B A A A 
    B B B B
    A B A A
    A ? ? ?
    Numéro de la lignes compris entre 1, 4: 4
    Numéro de la colonne compris entre 1, 4: 3
    B A A A 
    B B B B
    A B A A
    A ? B ?
    Joueur n°2
    Numéro de la lignes compris entre 1, 4: 4
    Numéro de la colonne compris entre 1, 4: 2
    B A A A 
    B B B B
    A B A A
    ? B ? ?
    Numéro de la lignes compris entre 1, 4: 4
    Numéro de la colonne compris entre 1, 4: 3
    B A A A 
    B B B B
    A B A A
    ? B B ?
    Joueur n°1
    Numéro de la lignes compris entre 1, 4: 4
    Numéro de la colonne compris entre 1, 4: 1
    B A A A 
    B B B B
    A B A A
    A B B ?
    Numéro de la lignes compris entre 1, 4: 4
    Numéro de la colonne compris entre 1, 4: 4
    B A A A 
    B B B B
    A B A A
    A B B A
    Score :  [7, 6]
    Le joueur 1 fini premier
    """
    print("Initialisation :")
    print("______________________")
    # Local Variable --------------------------------------------- #
    separator = "_______________"
    variables = {
        "nbPlayers" : {"value" : 0, "stringInput" : "Nombre de joueurs : "},
        "nbLetters" : {"value" : 0, "stringInput" : "Nombre de lettres : "},
        "nbLines" : {"value" : 0, "stringInput" : "Nombre de lignes : "},
        "nbColumns" : {"value" : 0, "stringInput" : "Nombre de column : "}
    }
    score = []
    isWin = False
    variablesIsCheck = False
    while variablesIsCheck == False:
        for variable in variables:
            if variables[variable]["value"] == 0:
                while variables[variable]["value"] <= 0:
                    try:
                        variables[variable]["value"] = int(input(variables[variable]["stringInput"]))
                    except ValueError:
                        print("Veulliez entrer un nombre entier")
        # checkIfIsAvaible()
        nbLetters = variables["nbLetters"]["value"]
        nbLines = variables["nbLines"]["value"]
        nbColumns = variables["nbColumns"]["value"]
        nbPlayers = variables["nbPlayers"]["value"]
        score = [0 for x in range(variables["nbPlayers"]["value"])]
        grid = initGrid(nbLetters, nbLines, nbColumns)
        if grid == False:
            variables["nbLetters"]["value"] = 0
            variables["nbLines"]["value"] = 0
            variables["nbColumns"]["value"] = 0
            print("Impossible d'initialiser la grid les nombre de lettres, de lignes ou de colonnes ne sont pas correct")
        else:
            variablesIsCheck = True
            marked = initMarked(nbLines, nbColumns)
    print("Jeu")
    print(separator)
    shuffle(grid)
    print("Score : ", score)
    display(grid, marked)
    numberPlayer = 1
    while isWin != True:
        print(f"Joueur n°{numberPlayer}")
        tries = []
        for _ in range(2):
            line, column = getInput(marked)
            if marked[line][column] == False:
                marked[line][column] = True
            else:
                print("Case déjà montré")
            tries.append((line, column, grid[line][column]))
            display(grid, marked)
        if tries[0][2] != tries[1][2]:
            for tri in range(len(tries)):
                marked[tries[tri][0]][tries[tri][1]] = False
        score[numberPlayer - 1] += 1
        if numberPlayer == nbPlayers:
            numberPlayer = 1
        else:
            numberPlayer += 1
        isWin = checkWin(marked)
    print("Score : ", score)
    firsts = []
    for scorePlayer in range(len(score)):
        if score[scorePlayer] == max(score):
            firsts.append(scorePlayer + 1)
    for first in firsts:
        if len(firsts) > 1:
            print(f"Le joueur {first} fini en égalité avec {firsts[first]} point(s)")
        print(f"Le joueur {first} fini premier")

if __name__ == "__main__":
    import doctest
    doctest.testmod()