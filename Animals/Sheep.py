from Animals import Animal

class Sheep(Animal.Animal):
    def __init__(self,x,y, world):
        super().__init__(x,y, world)
        self.path = "Images/sheep.png"
        self.dead = False

        self.id = 2
        self.power = 4
        self.iniciative = 4

    def to_add(self, x, y):
        return Sheep(x,y,self.world)

    def getThisName(self):
        return "Sheep"

    def actualise(self):
        self.path = "Images/sheep.png"