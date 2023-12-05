from random import randint

from encounter import Encounter


class Asteroid(Encounter):
    def __init__(self):
        super().__init__()
        self.type = randint(0, 2)
        self.quantity = randint(1500, 3500)
        self.description = 'Asteroid'

        match self.type:
            case 0:
                self.ore = 'Fe (Iron)'
                print(self.ore)
            case 1:
                self.ore = 'Au (Gold)'
                print(self.ore)
            case 2:
                self.ore = 'Cu (Copper)'
                print(self.ore)

    def action(self, stuff_for_action) -> int:
        # debug print
        print("Ore type: ", self.ore)
        print("Ore quantity: ", self.quantity)

        if self.quantity >= 0:
            mined = self.quantity * 0.33 + self.tools[0]
            self.quantity -= mined
            if self.quantity <= 0:
                overdraft = self.quantity
                mined += overdraft
                self.quantity = 0
            return mined
        else:
            print("Asteroid contains no ore")
