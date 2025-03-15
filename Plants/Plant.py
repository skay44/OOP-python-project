from Organism import Organism
import random

class Plant(Organism):
    def __init__(self,x,y,w):
        super().__init__(x,y,w)
        self.path = "Images/placeholder.png"
        self.iniciative = 0
        self.reproductionChance = 10

    def collision(self, collided):
        if(isinstance(collided,Plant)):
            if(collided.id != self.id):
                if(collided.power <= self.power):
                    if(collided.invincibility() == False):
                        self.world.logs.append(self.get_characteristics() + " overgrows " + collided.get_characteristics())
                        collided.attackedBy(self)
                        reproduced = self.to_add(collided.x,collided.y)
                        self.world.addOrganism(reproduced)

    def action(self):
        reproduction = random.randint(0,100)
        if(self.reproductionChance > reproduction):
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
                if(self.world.animalArray[self.x+moveX][self.y+moveY] != None):
                    self.collision(self.world.animalArray[self.x+moveX][self.y+moveY])
                else:
                    reproduced = self.to_add(self.x+moveX,self.y+moveY)
                    self.world.addOrganism(reproduced)
                    self.world.logs.append(self.get_characteristics() + " reproduced -> " + reproduced.get_characteristics())


    def attackedBy(self, org):
        self.kill()

    def invincibility(self):
        return False

    def __getstate__(self,):
        return (self.x,self.y,self.dead,self.id,self.power,self.iniciative,self.reproductionChance)

    def actualise(self):
        pass

    def __setstate__(self, state):
        self.x, self.y, self.dead, self.id, self.power, self.iniciative,self.reproductionChance = state
        self.actualise()