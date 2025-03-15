from Animals.Animal import Animal

class Antelope(Animal):
    def __init__(self,x,y,w):
        super().__init__(x,y,w)
        self.path = "Images/antelope.png"
        self.dead = False

        self.range = 2
        self.id = 5
        self.power = 4
        self.iniciative = 4

    def to_add(self, x, y):
        return Antelope(x, y, self.world)

    def getThisName(self):
        return "Antelope"

    def ifEscapes(self):
        return True

    def actualise(self):
        self.path = "Images/antelope.png"