from  Organism import Organism
from Plants import Plant
import random
import world

class Animal(Organism):
    def __init__(self, x, y, world):
        super().__init__(x, y, world)
        self.path = "Images/placeholder.png"
        self.range = 1
        self.newX = x
        self.newY = y


    def reproduce(self):
        direction = random.randint(0,3)
        moveX = 0
        moveY = 0
        success = False
        if(direction == 0):
            if(self.x > 0):
                moveX = -1
                success = True
        elif(direction == 1):
            if(self.x < self.world.x-1):
                moveX = 1
                success = True
        elif(direction == 2):
            if(self.y > 0):
                moveY = -1
                success = True
        elif(direction == 3):
            if(self.y < self.world.y-1):
                moveY = 1
                success = True
        if(success == True):
            breedingSuccess = True
            if(self.world.animalArray[self.x + moveX][self.y + moveY] != None):
                if(isinstance(self.world.animalArray[self.x + moveX][self.y + moveY], Animal)):
                    breedingSuccess = False
                else:
                    if(self.world.animalArray[self.x + moveX][self.y + moveY].power > self.power):
                        breedingSuccess = False
                    else:
                        self.world.animalArray[self.x + moveX][self.y + moveY].attackedBy(self)
            if(breedingSuccess == True):
                reproduced = self.to_add(self.x + moveX,self.y +moveY)
                self.world.addOrganism(reproduced)
                self.world.logs.append(self.get_characteristics() + "reproduces" + reproduced.get_characteristics())
            else:
                self.world.logs.append(self.get_characteristics() + "couldnt reproduce")
        else:
            self.world.logs.append(self.get_characteristics() + "couldnt reproduce")

    def escape(self):
        #return False #temporary
        if(self.newX-1 >= 0 and self.world.animalArray[self.newX-1][self.y] == None):
            self.newX = self.newX-1
            self.changePosition()
            return True
        elif(self.newX+1 < self.world.x and self.world.animalArray[self.newX+1][self.y] == None):
            self.newX = self.newX+1
            self.changePosition()
            return True
        elif(self.newY-1 >= 0 and self.world.animalArray[self.x][self.newY-1] == None):
            self.newY = self.newY-1
            self.changePosition()
            return True
        elif(self.newY+1 < self.y and self.world.animalArray[self.x][self.newY+1] == None):
            self.newY = self.newY + 1
            self.changePosition()
            return True
        return False


    def collision(self, collidingWith):
        ifEscaped = False
        self.world.logs.append(self.get_characteristics() + " encounters " + collidingWith.get_characteristics())
        if(isinstance(collidingWith,Animal)):
            if(collidingWith.id == self.id):
                self.newY = self.y
                self.newX = self.x
                self.reproduce()
            else:
                if(collidingWith.ifEscapes()):
                    ifEscaped = collidingWith.escape()
                if(ifEscaped == False):
                    if(collidingWith.power > self.power):
                        if(self.invincibility() == False):
                            self.attackedBy(collidingWith)
                        else:
                            self.world.logs.append(self.get_characteristics() + " avoids " + collidingWith.get_characteristics())
                            if(self.escape() == False):
                                self.attackedBy(collidingWith)
                    else:
                        if(collidingWith.invincibility() == False):
                            collidingWith.attackedBy(self)
                            self.changePosition()
                        else:
                            self.world.logs.append(collidingWith.get_characteristics() + " avoids " + self.get_characteristics())
                else:
                    self.world.logs.append(collidingWith.get_characteristics() + " escapes from " + self.get_characteristics()) #experimental
        elif(isinstance(collidingWith,Plant.Plant)):
            if(collidingWith.power > self.power):
                if(self.invincibility() == False):
                    self.world.logs.append(self.get_characteristics() + " eats " + collidingWith.get_characteristics())
                    self.attackedBy(collidingWith)
                    collidingWith.attackedBy(self)
                    if(self.dead == False):
                        self.changePosition()
                else:
                    self.world.logs.append(self.get_characteristics() + " avoids " + collidingWith.get_characteristics())
                    if(self.escape() == False):
                        self.attackedBy(collidingWith)
            else:
                self.world.logs.append(self.get_characteristics() + " eats " + collidingWith.get_characteristics())
                collidingWith.attackedBy(self)
                self.changePosition()


    def changePosition(self):
        self.world.animalArray[self.x][self.y] = None
        self.x = self.newX
        self.y = self.newY
        self.world.animalArray[self.x][self.y] = self

    def action(self):
        distance = random.randint(0,self.range-1)+1
        direction = random.randint(0,3)
        moveX = 0
        moveY = 0
        success = False
        if(direction == 0):
            if(self.x - distance >= 0):
                moveX = - distance
                success = True
        elif(direction == 1):
            if(self.x+distance < self.world.x):
                moveX = distance
                success = True
        elif(direction == 2):
            if(self.y-distance >= 0):
                moveY = -distance
                success = True
        elif(direction == 3):
            if(self.y+distance < self.world.y):
                moveY = distance
                success = True
        else:
            print("RESZTA")

        if(success == True):
            if(self.world.animalArray[self.x+moveX][self.y+moveY] != None):
                self.newX = self.x + moveX
                self.newY = self.y + moveY
                self.collision(self.world.animalArray[self.x+moveX][self.y+moveY])
            else:
                self.newX = self.x + moveX
                self.newY = self.y + moveY
                self.changePosition()


    def attackedBy(self, org):
        self.kill()

    def ifEscapes(self):
        return False

    def getThisName(self):
        return "Animal"

    def invincibility(self):
        return False

    def burn(self, org):
        if(self.dead == False):
            self.world.logs.append(self.get_characteristics() + " got burned by " + org.get_characteristics())
            self.kill()

    def __getstate__(self,):
        return (self.x,self.y,self.dead,self.newX,self.newY,self.id,self.power,self.iniciative,self.range)

    def actualise(self):
        pass

    def __setstate__(self, state):
        self.x, self.y, self.dead, self.newX, self.newY, self.id, self.power, self.iniciative, self.range = state
        self.actualise()