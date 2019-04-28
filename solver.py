import grid
import copy
import math


class Solver:
    def __init__(self, input_list):
        """Solver objesini initialize ediyoruz. Çözüm var mı? Kontrol edilir"""
        if not self.solvable(input_list):
            raise ValueError('A solution is not possible')

        # https://docs.python.org/2/library/copy.html
        self.initial_state = copy.deepcopy(self.list_to_grid(input_list))
        self.goal_state = self.set_goal_state(input_list)

        # # using custom structures so we can implement a custom __contains__()
        # self.frontier = custom_structures.Frontier() 
        # self.ast_frontier = custom_structures.Priority_Frontier()       
        # self.explored = custom_structures.Explored()

        # # TODO: fringe metrics not working for ast (because we're passing it wrong frontier here)
        # self.metrics = metric.Metric(self.frontier)
        return None

    def solvable(self, input_list):
        """
        Çözüm olup olmadığı kontrol edilir.
        http://math.stackexchange.com/questions/293527/how-to-check-if-a-8-puzzle-is-solvable/838818
        http://www.cs.bham.ac.uk/~mdr/teaching/modules04/java2/TilesSolvability.html

        Çözüm için gerekli kaynaklar yukarıdadır.
        """

        # Çözüm matris boyutuna bağlıdır
        size = int(math.sqrt(len(input_list)))

        # Boşluğun olduğu satır tek mi çift mi ?
        temp_grid = grid.Grid(self.list_to_grid(input_list))

        # Boşluğun lokasyonuna bağlı çözüm uygunluğu kontrolu
        space_location = temp_grid.locate_tile(0, temp_grid.state)
        if space_location[0] % 2 == 0:
            y_is_even = True
        else:
            y_is_even = False

        # inversions hesaplanır. Boşluk sayılmaz
        # Boşluk çıkarılır
        input_list = [number for number in input_list if number != 0]

        inversion_count = 0
        list_length = len(input_list)

        for index, value in enumerate(input_list):
            for value_to_compare in input_list[index + 1:list_length]:
                if value > value_to_compare:
                    inversion_count += 1                    

        if inversion_count % 2 == 0:
            inversions_even = True
        else:
            inversions_even = False

        if size % 2 == 0:
            size_even = True
        else:
            size_even = False

        # boşluk yukarıdan sayılır ama kurala göre aşağıdan sayılması gerekir
        if size_even:
            space_odd = not y_is_even

        # Çözüm kuralına göre çıkarılan formül
        return ((not size_even and inversions_even)
                or (size_even and (space_odd == inversions_even)))

    def list_to_grid(self, tile_list):
        """Take a list of length n^2, return a nxn 2D list"""

        # TODO: Shouldn't this be a method of grid instead?

        n = int(math.sqrt(len(tile_list)))

        # initialise empty grid
        input_grid = [['-' for x in range(n)] for y in range(n)]

        # populate grid with tiles
        i = 0
        j = 0
        for tile in tile_list:
            input_grid[i][j] = tile
            j += 1
            if j == n:
                j = 0
                i += 1

        return input_grid