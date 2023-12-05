from position import Position


class Space:
    def __init__(self, size):
        self.size = size
        self.grid = self.initialize_space(size)

    @staticmethod
    def initialize_space(size) -> []:
        x = size[0]
        y = size[1]

        grid = [[Position(i, j) for i in range(x)] for j in range(y)]
        return grid

    def retrieve_position_via_coordinates(self, x, y):
        return self.grid[y][x]

    def print(self):
        for row in self.grid:
            for position in row:
                print(position.symbol, end=" "),
            print()
