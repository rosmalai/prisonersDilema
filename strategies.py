from player import Player
import random as rnd 

class Fridman(Player):
    
    def __init__(self):
        self.name = "Fridman"
        self.last_strategy = True
        self.op_moves = []

    def pick_strategy(self):
        return self.last_strategy
    
    def process_results(self, my_strategy, opponent_strategy, my_score, opponent_score):
        if False in self.op_moves:
            self.last_strategy = False
        
        self.op_moves.append(opponent_strategy)

    def __str__(self):
        return self.name

class TitForTat(Player):
    
    def __init__(self):
        self.name = "TitForTat"
        self.last_strategy = True

    def pick_strategy(self):
        return self.last_strategy
    
    def process_results(self, my_strategy, opponent_strategy, my_score, opponent_score):
        self.last_strategy = opponent_strategy

    def __str__(self):
        return self.name
    

class SneakyTitForTat(Player):

    def __init__(self):
        self.name = "SneakyTitFortat"
        self.last_strategy  = True
        self.count = 0

    def pick_strategy(self):
        return self.last_strategy
    
    def process_results(self, my_strategy, opponent_strategy, my_score, opponent_score):
        self.count+=1
        if self.count % 3 == 0:
            self.last_strategy = rnd.choice([True, False])
        else:
            self.last_strategy = opponent_strategy

    def __str__(self):
        return self.name
        

class Random(Player):

    def __init__(self):
        self.name = "Random"
        
    def pick_strategy(self):
        return rnd.choice([True, False])
    
    def process_results(self, my_strategy, opponent_strategy, my_score, opponent_score):
        pass

    def __str__(self):
        return self.name
    
class AlwaysDefect(Player):
    
    def __init__(self):
        self.name = "AlwaysDefect"
        self.last_strategy = False

    def pick_strategy(self):
        return self.last_strategy
    
    def process_results(self, my_strategy, opponent_strategy, my_score, opponent_score):
        pass

    def __str__(self):
        return self.name

class AlwaysCooperate(Player):

    def __init__(self):
        self.name = "AlwaysCooperate"
        self.last_strategy = True
    
    def pick_strategy(self):
        return self.last_strategy
    
    def process_results(self, my_strategy, opponent_strategy, my_score, opponent_score):
        pass

    def __str__(self):
        return self.name
    
class TitForTwoTats(Player):

    def __init__(self):
        self.name = "TitForTwoTats"
        self.last_strategy = True
        self.history = []

    def pick_strategy(self):
        if len(self.history) < 2:
            return self.last_strategy
        if not self.history[-1] and not self.history[-2]:
            return False
        return self.last_strategy

    def process_results(self, my_strategy, opponent_strategy, my_score, opponent_score):
        self.last_strategy = opponent_strategy
        self.history.append(opponent_strategy)

    def __str__(self):
        return self.name

class TitForTat_avg(Player):
    def __init__(self):
        self.name = "TitForTat_avg"
        self.history = []
        self.last_strategy = True

    def pick_strategy(self):
        return self.last_strategy
    
    def process_results(self, my_strategy, opponent_strategy, my_score, opponent_score):
        if opponent_strategy:
            self.history.append(1)
        else:
            self.history.append(-1)
        total = sum(self.history)
        if total >= 0:
            self.last_strategy = True
        else:
            self.last_strategy = False

    def __str__(self):
        return self.name
    

class Moody(Player):
    def __init__(self):
        self.name = "Moody"
        self.last_strategy = True

    def pick_strategy(self):
        return self.last_strategy 

    def process_results(self, my_strategy, opponent_strategy, my_score, opponent_score):
        if my_score >= opponent_score:
            self.last_strategy = True
        else:
            self.last_strategy = False
    
    def __str__(self):
        return self.name

class InverseMoody (Player):
    def __init__(self):
        self.name = "InverseMoody"
        self.last_strategy = True
    def pick_strategy(self):
        return self.last_strategy

    def process_results(self, my_strategy, opponent_strategy, my_score, opponent_score):
       if my_score >= opponent_score:
           self.last_strategy = False
       else:
           self.last_strategy = True
    def __str__(self):
        return self.name



strategies = [Fridman, TitForTat,SneakyTitForTat, Random, AlwaysDefect, AlwaysCooperate, TitForTwoTats,TitForTat_avg, Moody, InverseMoody]