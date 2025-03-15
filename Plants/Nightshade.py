from Plants.Plant import Plant

class Nightshade(Plant):
    def __init__(self,x,y,w):
        super().__init__(x,y,w)
        self.path = "Images/Nightshade.png"
        self.iniciative = 0
        self.id = 1
        self.power = 99
        self.reproductionChance = 5

    def to_add(self, x, y):
        return Nightshade(x, y, self.world)

    def getThisName(self):
        return "Nightshade"

    def attackedBy(self, org):
        self.kill()
        if(org.dead == False):
            org.attackedBy(self)

    def actualise(self):
        self.path = "Images/Nightshade.png"