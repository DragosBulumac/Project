from itertools import product


def solve_sudoku(puzzle, trial=True):
    for (row, col) in product(range(0, 9), repeat=2):
        if puzzle[row][col] == 0:  # gaseste o celula neatribuita
            for num in range(1, 10):
                allowed = True  #  verificare daca num este permis in row/col/box
                for i in range(0, 9):
                    if (puzzle[i][col] == num) or (puzzle[row][i] == num):
                        allowed = False
                        break  # nu este permisa pe linie sau coloana
                for (i, j) in product(range(0, 3), repeat=2):
                    if puzzle[row - row % 3 + i][col - col % 3 + j] == num:
                        allowed = False
                        break  # not allowed in box
                if allowed:
                    puzzle[row][col] = num
                    if trial != solve_sudoku(puzzle):
                        return trial
                    else:
                        puzzle[row][col] = 0
            return False  # nu se poate adauga un numar in celula
    return puzzle


def print_sudoku(puzzle):
    # inlocuire 0 cu *
    puzzle = [['*' if num == 0 else num for num in row] for row in puzzle]
    print()
    for row in range(0, 9):
        if ((row % 3 == 0) and (row != 0)):
            print('-' * 33)  # trage linie orizontala
        for col in range(0, 9):
            if ((col % 3 == 0) and (col != 0)):
                print(' | ', end='')  # trage o linie verticala
            print('', puzzle[row][col], '', end='')
        print()
    print()


puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
          [6, 0, 0, 1, 9, 5, 0, 0, 0],
          [0, 9, 8, 0, 0, 0, 0, 6, 0],
          [8, 0, 0, 0, 6, 0, 0, 0, 3],
          [4, 0, 0, 8, 0, 3, 0, 0, 1],
          [7, 0, 0, 0, 2, 0, 0, 0, 6],
          [0, 6, 0, 0, 0, 0, 2, 8, 0],
          [0, 0, 0, 4, 1, 9, 0, 0, 5],
          [0, 0, 0, 0, 8, 0, 0, 7, 9]]
print_sudoku(puzzle)
solution = solve_sudoku(puzzle)
