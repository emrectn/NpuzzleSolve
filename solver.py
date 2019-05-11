import matris
import copy
import math
import structures


class Solver:
    def __init__(self, input_list):
        """Solver objesini initialize ediyoruz. Çözüm var mı? Kontrol edilir"""
        if not self.solvable(input_list):
            raise ValueError('A solution is not possible')

        # List to grid -> 1,2,3,4 ---> [[1,2], [3,4]]
        self.initial_state = copy.deepcopy(self.list_to_grid(input_list))
        self.n = int(math.sqrt(len(input_list)))
        self.goal_state = self.set_goal_state(input_list)

        # Kuyruk yapıları için structures sınıfı kullanıldı.
        self.ast_frontier = structures.Priority_Frontier()
        self.explored = structures.Explored()
        self.path = self.a_star_algorithm()

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
        temp_matris = matris.Matris(self.list_to_grid(input_list))

        # Boşluğun lokasyonuna bağlı çözüm uygunluğu kontrolu
        space_location = temp_matris.locate_tile(0, temp_matris.state)
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
        """liste alır n^2, return nxn 2D list"""

        n = int(math.sqrt(len(tile_list)))

        # [['-','-'], ['-','-'], ['-','-']]
        input_grid = [['-' for x in range(n)] for y in range(n)]

        i = 0
        j = 0
        for tile in tile_list:
            input_grid[i][j] = tile
            j += 1
            if j == n:
                j = 0
                i += 1

        return input_grid

    def set_goal_state(self, input_list):
        """Hedef matris olusturulur"""

        cnt = 1
        goal_state = []
        for i in range(self.n):
            row = list()
            for j in range(self.n):
                row.append(cnt)
                cnt += 1
            goal_state.append(row)
        goal_state[self.n-1][self.n-1] = 0
        return goal_state

    def a_star_algorithm(self):

        # Baslangıç matrisi ve skoru
        initial_grid = matris.Matris(self.initial_state)
        initial_grid.score = initial_grid.manhattan_score(self.goal_state)

        # Kuyruga eklenir
        self.ast_frontier.queue.put(
            (initial_grid.score, self.ast_frontier.counter, initial_grid))

        self.ast_frontier.counter += 1

        # Kuyruk bitene kadar veya hedefe ulasana kadar dongu devam eder
        while not self.ast_frontier.queue.empty():
            lowest_scored = self.ast_frontier.queue.get()
            state = lowest_scored[2]

            self.explored.set.add(state)
            # Hedef ulaşılırsa gidilen path return edilir
            if self.check_goal_state(state):
                return state.path_history

            self.find_nodes(state)
        raise ValueError('Opps!! Buraya gelmemeliydin.')

    def find_nodes(self, starting_grid):
        """ Mevcut durumun yapabilecegi hareketlerin kuyruga eklenmesi """
        movement = ['UP', 'DOWN', 'LEFT', 'RIGHT']

        for move in movement:

            # Yeni bir matris olusturuyoruz, ana durumun kopyası
            new_grid = matris.Matris(starting_grid.state)
            new_grid.path_history = copy.copy(starting_grid.path_history)

            # Eger hareket etme imkanı varsa yeni hareketi kuyruga ekliyoruz
            if new_grid.move(move):
                new_grid.path_history.append(move)

                # Yeni durumun daha kontrol edilmemiş eklenmemiş
                # Sonraki adımlarda 
                if new_grid not in self.ast_frontier and new_grid not in self.explored:
                    new_grid.score = new_grid.manhattan_score(self.goal_state)
                    self.ast_frontier.queue.put(
                        (new_grid.score, self.ast_frontier.counter, new_grid))
                    self.ast_frontier.counter += 1

    def check_goal_state(self, state):
        """Hedef state olup olmadıgı kontrol edilir."""
        # print("Hedef : ", self.goal_state)
        # print("Mevcut : ", state.state)
        if state.state == self.goal_state:
            print("Goal Found : ", state.state)
            return True
        else:
            return False
