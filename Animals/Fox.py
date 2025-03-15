from Animals import Animal
import random

class Fox(Animal.Animal):
    def __init__(self,x,y, world):
        super().__init__(x,y, world)
        self.path = "Images/fox.png"
        self.dead = False

        self.id = 3
        self.power = 3
        self.iniciative = 7

    def to_add(self, x, y):
        return Fox(x,y,self.world)

    def getThisName(self):
        return "Fox"

    def checkSafe(self, nx, ny):
        if(self.world.animalArray[nx][ny] != None):
            if(self.world.animalArray[nx][ny].power > self.power):
                self.world.logs.append(self.get_characteristics() + " avoids danger from " + self.world.animalArray[nx][ny].get_characteristics())
                return False
        return True

    def action(self):
        direction = random.randint(0,3)
        moveX = 0
        moveY = 0
        success = False
        if(direction == 0):
            if(self.x > 0):
                if(self.checkSafe(self.x-1,self.y)):
                    moveX = -1
                    success = True
        elif(direction == 1):
            if(self.x < self.world.x-1):
                if(self.checkSafe(self.x+1,self.y)):
                    moveX = 1
                    success = True
        elif(direction == 2):
            if(self.y > 0):
                if(self.checkSafe(self.x,self.y-1)):
                    moveY = -1
                    success = True
        elif(direction == 3):
            if(self.y < self.world.y-1):
                if(self.checkSafe(self.x,self.y+1)):
                    moveY = 1
                    success = True

        if(success == True):
            self.newX = self.x + moveX
            self.newY = self.y + moveY
            if(self.world.animalArray[self.x + moveX][self.y + moveY] != None):
                self.collision(self.world.animalArray[self.x+moveX][self.y+moveY])
            else:
                self.changePosition()

    def actualise(self):
        self.path = "Images/fox.png"

