from random import randint

from encounter import Encounter


class SpaceStation(Encounter):
    def __init__(self):
        super().__init__()
        self.occupied = randint(0, 1)
        self.description = 'Space Station'

    def action(self):
        # debug print
        print("Space Station Action")
