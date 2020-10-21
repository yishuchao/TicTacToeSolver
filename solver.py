from utils import *

class Solver():

    def __init__(self):
        self.memory = {}
    
    def solve(self,game):
        hashed = hash(game.position)
        if hashed in self.memory:
            return self.memory[hashed]
        else:
            if game.PrimitiveValue() != Value.UNDECIDED:
                self.memory[hashed] = (game.PrimitiveValue(), 0)
                return self.memory[hashed]
            else:
                sub_pos = []
                children =[]
                for move in game.GenerateMoves():
                    newGame = game.DoMove(move)
                    children.append(newGame)
                for child in children:
                    if hash(child.position) in self.memory:
                        sub_pos.append(self.memory[hash(child.position)])
                    else:
                        sub_pos.append(self.solve(child))
                values = [item[0] for item in sub_pos]
                if Value.LOSE in values:
                    remoteness  = 1 + min([item[1] for item in sub_pos if item[0] == Value.LOSE])
                    self.memory[hashed] = (Value.WIN, remoteness)
                elif Value.TIE in values:
                    remoteness = 1 + max([item[1] for item in sub_pos if item[0] == Value.TIE])
                    self.memory[hashed] = (Value.TIE, remoteness)
                else:
                    remoteness = 1 + max([item[1] for item in sub_pos])
                    self.memory[hashed] =  (Value.LOSE, remoteness)
                return self.memory[hashed]










