from utils import *
from solver import *

class TicTacToe():
    def __init__(self, position = '000000000', player='1'):
        self.position = position
        self.player = player
        if self.player == '1':
            self.opposite = '2'
        else:
            self.opposite = '1'


    def GenerateMoves(self):
        possible_moves = []
        for i in range(9):
            if self.position[i] =='0':
                possible_moves.append(i)
        return possible_moves

    def DoMove(self,move):
        board = list(self.position)
        board[move] = self.player
        position_new = "".join(board)
        return TicTacToe(position_new, self.opposite)

    def full_board(self):
        if "0" not in self.position:
            return True
        else:
            return False

    def check_triple(self, idx1, idx2, idx3):
        if self.position[idx1] == self.position[idx2] == self.position[idx3] != '0':
            return True
        else:
            return False

    def complete_triple(self):
        if self.check_triple(0,1,2):
            return True
        elif self.check_triple(3,4,5):
            return True
        elif self.check_triple(6,7,8):
            return True
        elif self.check_triple(0,3,6):
            return True
        elif self.check_triple(1,4,7):
            return True
        elif self.check_triple(2,5,8):
            return True
        elif self.check_triple(0,4,8):
            return True
        elif self.check_triple(2,4,6):
            return True
        else: 
            return False


    def PrimitiveValue(self):
        if self.complete_triple():
            return Value.LOSE
        elif self.full_board() and not self.complete_triple():
            return Value.TIE
        else:
            return Value.UNDECIDED



gameplay = Solver().solve((TicTacToe()))
