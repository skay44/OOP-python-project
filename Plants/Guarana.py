from Plants.Plant import Plant

class Guarana(Plant):
    def __init__(self,x,y,w):
        super().__init__(x,y,w)
        self.path = "Images/guarana.png"
        self.iniciative = 0
        self.id = 3
        self.power = 0
        self.reproductionChance = 5

    def to_add(self, x, y):
        return Guarana(x, y, self.world)

    def getThisName(self):
        return "Guarana"

    def attackedBy(self, org):
        org.power = org.power+3
        self.world.logs.append(org.get_characteristics() + " increased strength to <" + str(org.power) + ">")
        self.kill()

    def actualise(self):
        self.path = "Images/guarana.png"