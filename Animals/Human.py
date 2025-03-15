from Animals.Animal import Animal

class Human(Animal):
    def __init__(self,x,y,w):
        super().__init__(x,y,w)
        self.path = "Images/human.png"
        self.dead = False

        self.id = 0
        self.power = 5
        self.iniciative = 4

        self.cooldown = 0
        self.duration = 0


    def reproduce(self):
        pass


    def to_add(self, x, y):
        return Human(x, y, self.world)

    def getThisName(self):
        return "Human"

    def action(self):
        self.newX = self.x
        self.newY = self.y
        if(self.world.abilityPressed == True):
            if(self.cooldown <= self.world.turn):
                self.cooldown = self.world.turn+10
                self.duration = self.world.turn+5
        self.updateVisuals()
        move = self.world.keyPressed # 1left 2right 3up 4down 0none
        if(move == 1):
            if(self.x - 1 >= 0):
                self.newX = self.x-1
        elif(move == 2):
            if(self.x+1 < self.world.x):
                self.newX = self.x+1
        elif(move == 3):
            if(self.y - 1 >= 0):
                self.newY = self.y-1
        elif(move == 4):
            if(self.y+1 < self.world.y):
                self.newY = self.y+1
        else:
            return

        if(self.newX != self.x or self.newY != self.y):
            if(self.world.animalArray[self.newX][self.newY] != None):
                self.collision(self.world.animalArray[self.newX][self.newY])
            else:
                self.changePosition()


    def invincibility(self):
        print("D: " + str(self.duration))
        if(self.duration > self.world.turn):
            return True
        else:
            return False

    def __getstate__(self,):
        return (self.x,self.y,self.dead,self.newX,self.newY,self.id,self.power,self.iniciative,self.range,self.cooldown,self.duration)

    def __setstate__(self, state):
        self.x, self.y, self.dead, self.newX, self.newY, self.id, self.power, self.iniciative, self.range, self.cooldown, self.duration = state
        self.actualise()

    def actualise(self):
        self.path = "Images/human.png"

    def updateVisuals(self):
        if (self.duration > self.world.turn):
            self.path = "Images/human2.png"
        else:
            self.path = "Images/human.png"