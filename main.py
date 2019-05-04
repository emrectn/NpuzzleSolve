import sys
import solver
import grid


def initialize():
    # validate command line input
    if len(sys.argv) != 2:
        sys.stderr.write("Error: must be  command line arguments of the " +
                         "form:\npython driver.py <board>\n")
        sys.exit()

    # convert input string to a list of ints
    input_list = sys.argv[1].split(',')
    input_list = list(map(int, input_list))

    ordered_list = sorted(input_list)
    for index, number in enumerate(ordered_list):
        if number != index:
            sys.stderr.write(
                "Error: input list must contain all numbers from 0 to n^2 - 1")
            sys.exit()

    try:
        solver_obj = solver.Solver(input_list)
        return solver_obj
    except ValueError:
        print('no solution exists')
        sys.exit()


def visualize(solver):
    solved_grid = grid.Grid(solver.initial_state)
    solved_grid.visualize()

    for move in solver.path:
        print("       ||\n"*2,  "      \\/")
        solved_grid.move(move)
        solved_grid.visualize()


if __name__ == "__main__":
    print("Bismillah")
    solver_obj = initialize()
    visualize(solver_obj)
