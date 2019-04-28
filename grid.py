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
