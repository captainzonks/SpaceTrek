from random import randint

from encounter import Encounter


class Asteroid(Encounter):
    def __init__(self):
        super().__init__()
        self.type = randint(0, 3)
        self.quantity = randint(1500, 3500)
        self.description = 'Asteroid'

        match self.type:
            case 0:
                self.ore = 'Fe (Iron)'
            case 1:
                self.ore = 'Au (Gold)'
            case 2:
                self.ore = 'Cu (Copper)'

    def action(self):
        self.quantity -= self.quantity * 0.33 * self.tools[0]
        # debug print
        print("Ore quantity: ", self.quantity)
