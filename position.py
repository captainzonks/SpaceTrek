from random import randint

from asteroid import Asteroid
from space_station import SpaceStation


class Position:
    def __init__(self, x_coord, y_coord):
        self.seed = randint(0, 2)
        self.coordinates = (x_coord, y_coord)
        self.encounter = None
        self.symbol = '-'

        match self.seed:
            case 0:
                print('Asteroid!')
                self.encounter = Asteroid()
                self.encounter.encounter_type = self.encounter
            case 1:
                print('SpaceStation!')
                self.encounter = SpaceStation()
                self.encounter.encounter_type = self.encounter
            case 2:
                print('None!')
                self.encounter = None
