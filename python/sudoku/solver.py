import random


def main():
    puzzle = enter_board()
    draw_board(puzzle)
    print(puzzle)


def enter_board():
    board_string = ''
    for i in range(9):
        line = input(f'Enter line {i + 1} : ')
        board_string += line
    puzzle = Puzzle(board_string)
    return puzzle


def draw_board(puzzle):
    char_list = []
    for i, cell in enumerate(puzzle.cells):
        if i % 3 == 0 and i > 0 and i % 9 != 0:
            char_list.append('|')
        if i % 9 == 0 and i > 0:
            char_list.append('\n')
        if i % 27 == 0 and i > 0:
            char_list.append('---------\n')
        char_list.append(str(cell.value or ' '))
    board_string = ''.join(char_list)
    print(board_string)


class Cell:
    def __init__(self, value=None):
        self.value = value

    def __str__(self):
        return str(self.value)


class Puzzle:
    def __init__(self, string=None):

        """ Create the 81 cells """
        self.cells = []
        if string:
            for char in string:
                try:
                    value = int(char)
                except ValueError:
                    value = None
                cell = Cell(value)
                self.cells.append(cell)
        else:
            for i in range(81):
                value = random.randrange(1, 10)
                self.cells.append(Cell(value))

        """ Create the 9 row lists """
        self.rows = [[] for i in range(9)]

        """ Create the 9 column lists """
        self.cols = [[] for i in range(9)]

        """ Create the 9 squares lists """
        self.squares = [[] for i in range(9)]

        """ Create the possible values lists """
        all_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.possible_values = [[] for i in range(81)]
        for i, cell in enumerate(self.cells):
            self.possible_values[i] = cell.value or all_values.copy()

    def __str__(self):
        string = [str(cell) for cell in self.cells]
        return ''.join(string)


if __name__ == '__main__':
    main()
