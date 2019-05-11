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
                if value != 0:
                    sum += self.manhattan_distance(value, (y, x), goal_state)
        return sum

    def manhattan_distance(self, value, coordinates, goal_state):
        goal_coordinates = self.locate_tile(value, goal_state)
        return (abs(goal_coordinates[0] - coordinates[0])
                + abs(goal_coordinates[1] - coordinates[1]))

    def move(self, direction):
        space = self.locate_tile(0, self.state)

        if direction == 'UP':
            y, x = -1, 0
        elif direction == 'DOWN':
            y, x = 1, 0
        elif direction == 'RIGHT':
            y, x = 0, 1
        elif direction == 'LEFT':
            y, x = 0, -1
        else:
            raise ValueError('Invalid direction: must be \'UP\', \'DOWN\', \
                \'LEFT\' or \'RIGHT\'')  # TODO: is this good design?

            # return false if move not possible
        if space[0] + y not in range(0, self.n):
            return False
        if space[1] + x not in range(0, self.n):
            return False

        # swap tiles
        tile_to_move = self.state[space[0] + y][space[1] + x]
        self.state[space[0]][space[1]] = tile_to_move
        self.state[space[0] + y][space[1] + x] = 0

        return True, (space[0], space[1], tile_to_move), (space[0]+y, space[1]+x, "")

    def visualize(self):
        print("\n", "-"*((self.n*2)**2//2))
        for y, row in enumerate(self.state):
            for x, value in enumerate(row):
                print(" {:3d} |".format(value), end="")
            print("\n", "-"*((self.n*2)**2//2))
