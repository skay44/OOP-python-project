from Plants.Plant import Plant

class Grass(Plant):
    def __init__(self,x,y,w):
        super().__init__(x,y,w)
        self.path = "Images/grass.png"
        self.iniciative = 0
        self.id = 1
        self.power = 0
        self.reproductionChance = 15

    def to_add(self, x, y):
        return Grass(x, y, self.world)

    def getThisName(self):
        return "Grass"

    def actualise(self):
        self.path = "Images/grass.png"