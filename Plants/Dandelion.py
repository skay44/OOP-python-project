from Plants.Plant import Plant

class Dandelion(Plant):
    def __init__(self,x,y,w):
        super().__init__(x,y,w)
        self.path = "Images/dandelion.png"
        self.iniciative = 0
        self.id = 2
        self.power = 0
        self.reproductionChance = 10

    def to_add(self, x, y):
        return Dandelion(x, y, self.world)

    def getThisName(self):
        return "Dandelion"

    def action(self):
        for i in range(3):
            super().action()

    def actualise(self):
        self.path = "Images/dandelion.png"