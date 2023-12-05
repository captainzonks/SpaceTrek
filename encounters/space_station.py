from random import randint

from encounter import Encounter


class SpaceStation(Encounter):
    def __init__(self):
        super().__init__()
        self.occupied = randint(0, 1)
        self.friendly = randint(1, 1)
        self.description = 'Space Station'

    def action(self, stuff_for_action):
        if self.friendly:
            if stuff_for_action.ore > 0:
                print("Selling ore")
                if stuff_for_action.ore >= 150:
                    stuff_for_action.ore -= 150
                    stuff_for_action.money += 100
                elif stuff_for_action.ore > 0:
                    stuff_for_action.money += 100 / stuff_for_action.ore
                    stuff_for_action.ore = 0
            else:
                print("Ship has no ore to sell")

    def print(self):
        print("=====STATION=====")
