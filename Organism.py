from abc import ABC, abstractmethod


class Organism:
    def __init__(self, x, y, world):
        self.x = x
        self.y = y
        self.world = world
        self.path = "Images/empty.png"
        self.dead = False

    def kill(self):
        self.world.animalArray[self.x][self.y] = None
        self.world.logs.append(self.get_characteristics() + " died")
        self.dead = True

    def setXY(self,x,y):
        self.x = x
        self.y = y

    @abstractmethod
    def invincibility(self):
        pass

    @abstractmethod
    def action(self):
        pass

    @abstractmethod
    def collision(self):
        pass

    def get_characteristics(self):
        return str(self.getThisName()) + " [ "   + str(self.x) + "," + str(self.y) + " ] "

    @abstractmethod
    def to_add(self, x, y):
        pass

    @abstractmethod
    def getThisName(self):
        pass

    def burn(self, org):
        pass

    def updateVisuals(self):
        pass




