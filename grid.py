import math
import copy


class Grid:

    def __init__(self, input_state):
        self.state = copy.deepcopy(input_state)
        self.path_history = list()
        # Bir satırdaki eleman sayısı
        self.n = len(input_state[0])

        # manhattan distance hesaplanması
        self.score = 0

    def locate_tile(self, tile, grid_state):
        """İstenen karenin bulduğu kordinatları verir."""

        for (y, row) in enumerate(grid_state):
            for (x, value) in enumerate(row):
                if value == tile:
                    return (y, x)

    def manhattan_score(self, goal_state):
        sum = 0

        for y, row in enumerate(self.state):
            for x, value in enumerate(row):
                if value == 0:
                    continue
                sum += self.manhattan_distance(value, (y, x), goal_state)
        return sum

    def manhattan_distance(self, value, coordinates, goal_state):
        goal_coordinates = self.locate_tile(value, goal_state)
        return (abs(goal_coordinates[0] - coordinates[0]) 
                + abs(goal_coordinates[1] - coordinates[1]))