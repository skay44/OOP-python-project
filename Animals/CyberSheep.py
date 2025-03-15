from Animals import Animal
from Plants.PBorscht import PBorscht
import random


class vector2:
    def __init__(self, x1, y1):
        self.x = x1
        self.y = y1

class CyberSheep(Animal.Animal):
    def __init__(self,x,y, world):
        super().__init__(x,y, world)
        self.path = "Images/cyberSheep.png"
        self.dead = False

        self.id = 6
        self.power = 11
        self.iniciative = 4

    def to_add(self, x, y):
        return CyberSheep(x,y,self.world)

    def getThisName(self):
        return "Cyber Sheep"

    def action(self):

        distance = -1
        destination = vector2(-1,-1)
        moveX = 0
        moveY = 0

        for entity in self.world.animals:
            if(isinstance(entity,PBorscht)):
                if(distance == -1):
                    distance = abs(self.x - entity.x) + abs(self.y - entity.y)
                    destination.x = entity.x
                    destination.y = entity.y
                elif(distance > abs(self.x - entity.x) + abs(self.y - entity.y)):
                    distance = abs(self.x - entity.x) + abs(self.y - entity.y)
                    destination.x = entity.x
                    destination.y = entity.y

        if(destination.x != -1):
            if(abs(destination.x - self.x) > abs(destination.y - self.y)):
                if(destination.x > self.x):
                    moveX = moveX+1
                else:
                    moveX = moveX-1
            else:
                if(destination.y > self.y):
                    moveY = moveY+1
                else:
                    moveY = moveY-1

            if(self.world.animalArray[self.x+moveX][self.y+moveY] != None):
                self.newX = self.x + moveX
                self.newY = self.y + moveY
                self.collision(self.world.animalArray[self.x+moveX][self.y+moveY])
            else:
                self.newX = self.x + moveX
                self.newY = self.y + moveY
                self.changePosition()
        else:
            super().action()

    def burn(self, org):
        pass
    
    def attackedBy(self, org):
        if(isinstance(org,PBorscht)):
            pass
        else:
            super().attackedBy(org)

    def actualise(self):
        self.path = "Images/cyberSheep.png"





