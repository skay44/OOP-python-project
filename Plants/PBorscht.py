from Plants.Plant import Plant

class PBorscht(Plant):
    def __init__(self,x,y,w):
        super().__init__(x,y,w)
        self.path = "Images/pineBorscht.png"
        self.iniciative = 0
        self.id = 1
        self.power = 99
        self.reproductionChance = 5

    def to_add(self, x, y):
        return PBorscht(x, y, self.world)

    def getThisName(self):
        return "Pine Borscht"

    def action(self):
        for nx in range(-1,2,1):
            for ny in range(-1,2,1):
                if (self.x + nx < self.world.x-1 and self.x + nx > 0):
                    if (self.y + ny < self.world.y-1 and self.y + ny > 0):
                        if(self.world.animalArray[self.x+nx][self.y+ny] != None):
                            self.world.animalArray[self.x+nx][self.y+ny].burn(self)
        super().action()

    def attackedBy(self, org):
        self.kill()
        if(org.dead == False):
            org.attackedBy(self)

    def actualise(self):
        self.path = "Images/pineBorscht.png"
