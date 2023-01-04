#from data.allumette import allumette_bot, allumette
from cgitb import text
from distutils import command
from data.juste_prix import juste_prix, juste_prix_pc
from data.chasse import botGame, playerGame
from tkinter import *
from data.allumette import allumette_bot, allumette
from data.junipergreen import game
from data.memory import main

window = Tk()
window.geometry("300x410")
window.resizable(width=0, height=0)
window.title('menu des jeux')
title = Label(window, text="Choisissez votre jeux : ")
title.pack()
window.eval('tk::PlaceWindow .')


# Allumette :
allumetteBtn = Button(window, text="Jeux de l'allumette avec 2 joueurs",command=allumette)
allumetteBtnBot = Button(window, text="Jeux de l'allumette contre un bot",command=allumette_bot)

allumetteBtn.pack(); allumetteBtnBot.pack()

# Chasse au trésor :
chasseBtn = Button(window, text = "Chasse au trésor joueur contre bot", command = playerGame)
chasseBtnBot = Button(window, text = "Chasse au trésor bot contre joueur", command = lambda : botGame([x for x in range(0, 101)], [y for y in range(0, 101)], tuple(int(x) for x in input("Donnez les coordonnées du trésor à rechercher (x,y) : ").split(","))))

chasseBtn.pack(); chasseBtnBot.pack()

# Juste prix :
justePrixBtn = Button(window, text = "Juste prix joueur contre bot", command = lambda : juste_prix_pc(liste_prix = [x for x in range(1, 1001)], prix_joueur = int(input("Veulliez entrer un chiffre entre 1 et 1000 inclus que le bot devras chercher : ")), nb_reponse = 0))
justePrixBtnBot = Button(window, text = "Juste prix bot contre joueur", command = lambda : juste_prix())

justePrixBtn.pack(); justePrixBtnBot.pack()

# Juniper Green :
juniperGreenBtn = Button(window, text = "Juniper Green", command = lambda : game(0,20))

juniperGreenBtn.pack()

# Memory

memoryBtn = Button(window, text = "Memory",  command=main)

memoryBtn.pack()

chasseBtn.place(relx=0.5, rely=0.2, anchor=CENTER)
chasseBtnBot.place(relx=0.5, rely=0.27, anchor=CENTER)
justePrixBtn.place(relx=0.5, rely=0.34, anchor=CENTER)
justePrixBtnBot.place(relx=0.5, rely=0.41, anchor=CENTER)
juniperGreenBtn.place(relx=0.5, rely=0.48, anchor=CENTER)
allumetteBtn.place(relx=0.5, rely=0.55, anchor=CENTER)
allumetteBtnBot.place(relx=0.5, rely=0.62, anchor=CENTER)
memoryBtn.place(relx=0.5 ,rely=0.69, anchor=CENTER)
window.mainloop()