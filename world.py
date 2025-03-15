import screen
from pygamepopup import components
import pygamepopup
from pygamepopup.menu_manager import MenuManager
from tkinter import *
from Animals import Animal
import pygame
import Organism
from Animals.Antelope import Antelope
from Animals.CyberSheep import CyberSheep
from Animals.Fox import Fox
from Animals.Human import Human
from Animals.Sheep import Sheep
from Animals.Turtle import Turtle
from Animals.Wolf import Wolf
from Plants.Dandelion import Dandelion
from Plants.Grass import Grass
from Plants.Guarana import Guarana
from Plants.Nightshade import Nightshade
from Plants.PBorscht import PBorscht

import random
import pickle


class World:
    RANDOM = True
    grassAmount = 10
    dandelionAmount = 2
    guaranaAmount = 3
    nightshadeAmount = 5
    pineBorschAmount = 3

    wolfAmount = 3
    sheepAmount = 6
    foxAmount = 3
    turtleAmount = 4
    antelopeAmount = 3
    cyberSheepAmount = 2

    logs = []
    x = 20
    y = 20
    running = True
    animals = []
    animalArray = None
    keyPressed = 0
    abilityPressed = False

    def closed(self):
        exit(0)


    def game_loop(self):
        while self.running:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    self.running = False
                if (event.type == pygame.MOUSEBUTTONDOWN):
                    self.scr.checkClicked()
                if (event.type == pygame.KEYDOWN):
                    if(event.key == pygame.K_LEFT):
                        self.keyPressed = 1
                        #print("left")
                    if(event.key == pygame.K_RIGHT):
                        self.keyPressed = 2
                        #print("right")
                    if (event.key == pygame.K_UP):
                        self.keyPressed = 3
                        #print("up")
                    if (event.key == pygame.K_DOWN):
                        #print("down")
                        self.keyPressed = 4
                    if (event.key == pygame.K_q):
                        self.abilityPressed = True
            self.scr.updateVisuals()

    def generate_organisms(self):
        if self.RANDOM == False:
            self.addOrganism(Human(4,3,self))
            self.addOrganism(Fox(2,3,self))
            self.addOrganism(Fox(12,3,self))
            self.addOrganism(Grass(0,15,self))
            self.addOrganism(Sheep(3, 3, self))
            self.addOrganism(Turtle(16,16,self))
            self.addOrganism(Antelope(16,11,self))
            self.addOrganism(Grass(3,2,self))
            self.addOrganism(Wolf(11,2,self))
            self.addOrganism(CyberSheep(10,10,self))

            self.addOrganism(Dandelion(7,7,self))
            self.addOrganism(Guarana(7,8,self))
            self.addOrganism(Guarana(8,7,self))
            self.addOrganism(Nightshade(1,7,self))
            self.addOrganism(PBorscht(7,1,self))
            self.addOrganism(PBorscht(19,19,self))
        else:
            self.generateOrganism(Human(0,0,self))

            for i in range(self.grassAmount):
                self.generateOrganism(Grass(0,0,self))
            for i in range(self.dandelionAmount):
                self.generateOrganism(Dandelion(0,0,self))
            for i in range(self.guaranaAmount):
                self.generateOrganism(Guarana(0,0,self))
            for i in range(self.nightshadeAmount):
                self.generateOrganism(Nightshade(0,0,self))
            for i in range(self.pineBorschAmount):
                self.generateOrganism(PBorscht(0,0,self))
            for i in range(self.wolfAmount):
                self.generateOrganism(Wolf(0,0,self))
            for i in range(self.sheepAmount):
                self.generateOrganism(Sheep(0,0,self))
            for i in range(self.foxAmount):
                self.generateOrganism(Fox(0,0,self))
            for i in range(self.turtleAmount):
                self.generateOrganism(Turtle(0,0,self))
            for i in range(self.antelopeAmount):
                self.generateOrganism(Antelope(0,0,self))
            for i in range(self.cyberSheepAmount):
                self.generateOrganism(CyberSheep(0,0,self))

    def generateOrganism(self, organism):
        t = 0
        while True:
            randX = random.randint(0,self.x-1)
            randY = random.randint(0,self.y-1)
            if(self.animalArray[randX][randY] == None):
                organism.x = randX
                organism.y = randY
                self.addOrganism(organism)
                break
            else:
                t = t + 1
            if(t > 1000):
                break



    def __init__(self):
        def submit():
            try:
                if x_input.get() == "" and x_input.get() == "":
                    self.x = 20
                    self.y = 20
                else:
                    self.x = int(x_input.get())
                    self.y = int(y_input.get())
                    if self.x < 5:
                        self.x = 5
                    elif self.x > 30:
                        self.x = 30

                    if self.y < 5:
                        self.y = 5
                    elif self.y > 30:
                        self.y = 30
                root.quit()
                root.destroy()
            except:
                print("WRONG WALUE")


        self.turn = 1

        root = Tk()
        root.title('Enter the size of map')
        root.protocol("WM_DELETE_WINDOW", self.closed)
        root.geometry("400x200")

        x_label = Label(root, text="Width: ")
        x_label.pack(pady=10)

        x_input = Entry(root)
        x_input.pack(pady=5)

        y_label = Label(root, text="Height: ")
        y_label.pack(pady=10)

        y_input = Entry(root)
        y_input.pack(pady=5)

        confirm_button = Button(root, text="done", command=submit)
        confirm_button.pack(pady=5)

        # x =

        root.mainloop()

        # self.animalArray = [[Organism.Organism(0,0,self) for i in range(self.x)] for j in range(self.y)]

        print(str(self.x) + " " + str(self.y))

        self.animalArray = [[None for i in range(self.y)] for j in range(self.x)]

        #self.addOrganism(Sheep(3,4,self))
        #self.addOrganism(Fox(3,3,self))

        self.generate_organisms()

        self.scr = screen.Screen(self.x, self.y, self);

        self.scr.updateLogs()
        self.game_loop()

    def addOrganism(self, organism):
        if(organism.x < self.x and organism.x >= 0 and organism.y < self.y and organism.y > 0):
            self.animalArray[organism.x][organism.y] = organism
            self.animals.append(organism)

    def next_round(self):

        self.animals = [x for x in self.animals if not x.dead]

        for iniciative in range(8, -1, -1):
            for organism in self.animals:
                if(organism.iniciative == iniciative and organism.dead == False):
                    organism.action()


        self.scr.updateTiles(self.x,self.y)
        self.updateLogs()
        self.keyPressed = 0
        self.turn = self.turn + 1
        self.abilityPressed = False
        #print("next round")

    def updateLogs(self):
        self.scr.updateLogs()
        self.logs.clear()

    def new_board(self):
        def submit():
            try:
                if x_input.get() == "" and x_input.get() == "":
                    self.x = 20
                    self.y = 20
                else:
                    self.x = int(x_input.get())
                    self.y = int(y_input.get())
                    if self.x < 5:
                        self.x = 5
                    elif self.x > 30:
                        self.x = 30

                    if self.y < 5:
                        self.y = 5
                    elif self.y > 30:
                        self.y = 30
                root.quit()
                root.destroy()
            except:
                print("WRONG WALUE")

        self.animals.clear()
        self.animalArray = [[None for i in range(self.y)] for j in range(self.x)]

        self.turn = 1

        root = Tk()
        root.title('Enter the size of map')
        root.protocol("WM_DELETE_WINDOW", self.closed)
        root.geometry("400x200")

        x_label = Label(root, text="Width: ")
        x_label.pack(pady=10)

        x_input = Entry(root)
        x_input.pack(pady=5)

        y_label = Label(root, text="Height: ")
        y_label.pack(pady=10)

        y_input = Entry(root)
        y_input.pack(pady=5)

        confirm_button = Button(root, text="done", command=submit)
        confirm_button.pack(pady=5)

        # x =

        root.mainloop()

        #print(str(self.x) + " " + str(self.y))

        self.animalArray = [[None for i in range(self.y)] for j in range(self.x)]

        #self.addOrganism(Sheep(3,4,self))
        #self.addOrganism(Fox(3,3,self))

        self.generate_organisms()

        self.scr = screen.Screen(self.x, self.y, self);

        self.scr.updateLogs()
        self.game_loop()

    def save_game(self):
        with open('world.data', 'w') as file:
            file.write(str(self.turn) + "\n")
            file.write(str(self.x) + "\n")
            file.write(str(self.y) + "\n")

        with open('data.pickle', 'wb') as file:
            for entity in self.animals:
                pickle.dump(entity, file)
        print("save game")

    def load_game(self):
        with open('world.data', 'r') as file:
            self.turn = int(file.readline())
            self.x = int(file.readline())
            self.y = int(file.readline())

        self.animals.clear()
        self.animalArray = [[None for i in range(self.y)] for j in range(self.x)]
        with open('data.pickle', 'rb') as file:
            while True:
                try:
                    self.animals.append(pickle.load(file))
                except EOFError:
                    break

        for entity in self.animals:
            entity.world = self
            entity.updateVisuals()
            self.animalArray[entity.x][entity.y] = entity

        self.scr.updateTiles(self.x,self.y)
        self.keyPressed = 0

        print("load game")
        self.scr = screen.Screen(self.x, self.y, self);
        self.scr.updateLogs()
        self.game_loop()
