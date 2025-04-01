"""
Problem 96

Su Doku (Japanese meaning number place) is the name given to a popular puzzle concept. Its origin is unclear, but credit must be attributed to Leonhard Euler who invented a similar, and much more difficult, puzzle idea called Latin Squares. The objective of Su Doku puzzles, however, is to replace the blanks (or zeros) in a 9 by 9 grid in such that each row, column, and 3 by 3 box contains each of the digits 1 to 9. Below is an example of a typical starting puzzle grid and its solution grid.


003020600
900305001
001806400
008102900
700000008
006708200
002609500
800203009
005010300


483921657
967345821
251876493
548132976
729564138
136798245
372689514
814253769
695417382

A well constructed Su Doku puzzle has a unique solution and can be solved by logic, although it may be necessary to employ "guess and test" methods in order to eliminate options (there is much contested opinion over this). The complexity of the search determines the difficulty of the puzzle; the example above is considered easy because it can be solved by straight forward direct deduction.
The 6K text file, sudoku.txt (right click and 'Save Link/Target As...'), contains fifty different Su Doku puzzles ranging in difficulty, but all with unique solutions (the first puzzle in the file is the example above).
By solving all fifty puzzles find the sum of the 3-digit numbers found in the top left corner of each solution grid; for example, 483 is the 3-digit number found in the top left corner of the solution grid above.
"""
import time
from itertools import product
from copy import deepcopy

class sudoku(object):

    def __init__(self,board):
        self.solved = False
        self.board = [list(line) for line in board.split('\n')]
        self.checksum = 0

    def solve_by_deduction(self):
        board = self.board
        prev_unsolved = 0
        while not self.solved:
            unsolved = 0
            for row in range(len(board)):
                for col in range(len(board[0])):
                    if board[row][col] != '0': continue

                    possibilites = possible_nums(board,row,col)
                    if len(possibilites)==1:
                        num = possibilites.pop()
                        board[row][col] = num
                    else:
                        unsolved +=1

            if unsolved == 0:
                self.solved = True
                self.checksum = int(''.join(board[0][0:3]))
            if prev_unsolved == unsolved:
                # no new spots filled
                break
            prev_unsolved = unsolved

    def solve_by_DFS(self):

        start = deepcopy(self.board)
        stack = [start]
        while stack:
            curr_board = stack.pop()
            ## go to next empty spot / check if solved
            self.solved = True
            for row,col in product(range(9),repeat=2):
                if curr_board[row][col] == '0':
                    self.solved = False
                    break

            if self.solved:
                self.board = curr_board
                break

            # get children and add to stack
            nums = possible_nums(curr_board,row,col)
            next_boards = []
            for num in nums:
                new_board = deepcopy(curr_board)
                new_board[row][col] = num
                next_boards.append(new_board)
            stack += next_boards

            ## any board that is invalid will eventually have a spot that
            # has no possible nums in it, hence no children.
            # only need to check if board is solved and break while loop when
            # it is each board has only 1 soln




        s = ''.join(self.board[0][0:3])
        self.checksum = int(s)

    def solve(self):
        ## try and fill as many spots by deduction first
        s = time.time()
        self.solve_by_deduction()
        if not self.solved:
            self.solve_by_DFS()
        e = time.time()
        print(f'solved board in {(e-s)*1000:f} microseconds\n')

    def display(self):
        for _ in self.board:
            print(' '.join(_))

def possible_nums(board,row,col):
        # assume el == 0 for now
        # el = board[row][col]
        board_row = board[row]
        board_col = [a[col] for a in board]
        board_sq = get_square_els(board,row,col)

        out = set(str(a) for a in range(1,10))
        out.difference_update(board_row+board_col+list(board_sq))

        return sorted(out)

def get_square_els(board,row,col):
        els_in_box = set()
        start_row = (row//3)*3
        start_col = (col//3)*3
        for r in range(start_row,start_row+3):
            for c in range(start_col,start_col+3):
                els_in_box.add(board[r][c])
        return sorted(els_in_box)



input  = open('problem96/sudoku.txt','r').read()[0:].split('Grid ')
input = input[1:]

def solve(input):
    s = time.time()
    checksum = 0
    for unsolved_board in input:
        print(f'Solving Game {unsolved_board[0:2]}:')
        print(unsolved_board[3:-1])
        game = sudoku(unsolved_board[3:-1])
        game.solve()
        checksum+=game.checksum
    e = time.time()
    print(f"Final checksum is {checksum}.  {e-s:f} seconds elapsed")

solve(input)
# Final checksum is 24702.  13.859135 seconds elapsed
