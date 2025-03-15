from Animals.Animal import Animal
import random

class Turtle(Animal):
    def __init__(self,x,y,w):
        super().__init__(x,y,w)
        self.path = "Images/turtle.png"
        self.dead = False

        self.id = 4
        self.power = 2
        self.iniciative = 1

    def to_add(self, x, y):
        return Turtle(x,y,self.world)

    def getThisName(self):
        return "Turtle"

    def action(self):
        rand = random.randint(0,3)
        if(rand == 0):
            super().action()

    def attackedBy(self, org):
        if(isinstance(org, Animal)):
            if(org.power <= 5):
                if(self.newX == self.x and self.newY == self.y):
                    self.world.logs.append(self.get_characteristics() + " defends from " + org.get_characteristics())
                    org.newX = org.x
                    org.newY = org.y
                    return
        self.kill()

    def actualise(self):
        self.path = "Images/turtle.png"