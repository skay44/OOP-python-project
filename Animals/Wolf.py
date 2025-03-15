from Animals import Animal

class Wolf(Animal.Animal):
    def __init__(self,x,y, world):
        super().__init__(x,y, world)
        self.path = "Images/wolf.png"
        self.dead = False

        self.id = 1
        self.power = 9
        self.iniciative = 5

    def to_add(self, x, y):
        return Wolf(x,y,self.world)

    def getThisName(self):
        return "Wolf"

    def actualise(self):
        self.path = "Images/wolf.png"