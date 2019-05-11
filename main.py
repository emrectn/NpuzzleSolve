import sys
import matris
import time
import solver
from tkinter import Tk, Frame, TOP, Button


def initialize():
    # Arguman kontrolu
    if len(sys.argv) != 2:
        sys.stderr.write("Error: Eksik Arguman" +
                         "form:\npython driver.py <board>\n")
        sys.exit()

    # Argumanların int'e çevrilmesi
    input_list = sys.argv[1].split(',')
    input_list = list(map(int, input_list))

    # Verilen dizinin sıralanan bitisin belirlenmesi
    ordered_list = sorted(input_list)

    # Dizinin dogru oldugunun kontrol edilmesi -> 0,1,2,7 : Hatalı
    for index, number in enumerate(ordered_list):
        if number != index:
            sys.stderr.write(
                "Error: Hatali liste, sayilar 0 to n^2 - 1 arasinda olmalidir")
            sys.exit()

    try:
        solution_obj = solver.Solver(input_list)
        return solution_obj
    except ValueError:
        print('Bu dizinin cözümü yoktur.')
        sys.exit()


def visualize(solver):
    solved_matris = matris.Matris(solver.initial_state)
    solved_matris.visualize()

    for move in solver.path:
        print("       ||\n"*2,  "      \\/")
        solved_matris.move(move)
        solved_matris.visualize()


def visualize_tkinter(solver):
    solver_grid = matris.Matris(solver.initial_state)
    size = solver_grid.n

    # Arayüz oluşturulması
    window = Tk()
    window.geometry("{}00x{}".format(size, int((size*100)*0.56)))  # size of the window width:- 500, height:- 375
    window.resizable(0, 0)  # this prevents from resizing the window
    window.title("Npuzzle")

    btn_frame = Frame(window, width=size*100, height=size*100, bg="gray")
    btn_frame.pack(side=TOP)

    # Başlangıçtaki sayıların yerleştirilmesi
    for i, row in enumerate(solver.initial_state):
        for j, value in enumerate(row):
            # Eger boşluk ise kırmızı renkli gösterilmesi
            if not value == 0:
                Button(btn_frame, text=value, fg="black", width=10, height=3,
                       bd=0).grid(row=i, column=j, padx=1, pady=1)
            else:
                Button(btn_frame, text="", fg="black", width=10, height=3,
                       highlightbackground='red', bd=0).grid(row=i, column=j, 
                                                             padx=1, pady=1)
    window.update()

    # a = input("Bekliyom : ")

    # Hareketlerin ekrana arayüzle gösterilmesi - time.sleep(0.4)
    for move in solver.path:
        window.update()
        time.sleep(0.1)

        unused, tile_xy, space_xy = solver_grid.move(move)
        Button(btn_frame, text=tile_xy[2], fg="black", width=10, height=3, bd=0,
               bg="red").grid(row=tile_xy[0], column=tile_xy[1], padx=1, pady=1)

        Button(btn_frame, text="", fg="black", highlightbackground='#F00',
               width=10, height=3, bd=0).grid(row=space_xy[0], 
                                              column=space_xy[1], padx=1, pady=1)

    window.mainloop()


if __name__ == "__main__":
    solution_obj = initialize()
    # visualize(solution_obj)
    print(len(solution_obj.path))
    visualize_tkinter(solution_obj)
