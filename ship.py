from engine import Engine
from position import Position
from space import Space


class Ship:
    def __init__(self, space: Space):
        self.name = "Starship"
        self.space = space
        self.engine = Engine()
        self.position = Position(0, 0)
        self.previous_position = Position(0, 0)
        self.symbol = "o"

    def handle_ship_commands(self, player_input):
        match player_input:
            case 'w':
                self.move_up()
            case 's':
                self.move_down()
            case 'a':
                self.move_left()
            case 'd':
                self.move_right()
            case 'e':
                self.scan()
            case 'p':
                # probably just a debug print, no use for gameplay currently
                self.print_position()

    def move_up(self):
        if self.position.coordinates[0] is not 0:
            self.update_position(self.position.coordinates[0] - 1, self.position.coordinates[1])

    def move_down(self):
        if self.position.coordinates[0] is not 9:
            self.update_position(self.position.coordinates[0] + 1, self.position.coordinates[1])

    def move_left(self):
        if self.position.coordinates[1] is not 0:
            self.update_position(self.position.coordinates[0], self.position.coordinates[1] - 1)

    def move_right(self):
        if self.position.coordinates[1] is not 9:
            self.update_position(self.position.coordinates[0], self.position.coordinates[1] + 1)

    def update_position(self, x_coord, y_coord):
        self.previous_position = self.position
        self.position = self.space.retrieve_position_via_coordinates(x_coord, y_coord)
        self.update_grid()

    def update_grid(self):
        self.space.grid[self.previous_position.coordinates[0]][self.previous_position.coordinates[1]].symbol = '-'
        print(self.position.coordinates[0], self.position.coordinates[1])
        self.space.grid[self.position.coordinates[0]][self.position.coordinates[1]].symbol = self.symbol

    def scan(self):
        if self.position.encounter is not None:
            print('SCAN:', self.position.encounter.description, 'found!')
        else:
            print('SCAN: Found nothing')

    def print_position(self):
        print('POSITION: (', self.position.coordinates[0], ',', self.position.coordinates[1], ')')
