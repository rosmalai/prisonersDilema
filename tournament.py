from strategies import strategies
from match import Match
from random import randint
from itertools import combinations

class Tournament:
    def __init__(self, max_round, print_history):
        self.strategies = strategies
        self.max_round = max_round
        self.print_history = print_history
        self.database = {} #empty dict

    def sorted_score(self):
        # Sort the database entries by their scores (values) in descending order
        scores = sorted(self.database.items(), key = lambda x : x[1], reverse = True)

        print("Leaderboard")

        for i in scores:
            print(f"{i[0]} : {i[1]}")

    def give_pair(self):
        # Distinct pairs (tuples) + same-prisoner pairs (tuples)
        return list(combinations(self.strategies, 2)) + [(a, a)  for a in self.strategies] 
    
    def round(self):
        pairs = self.give_pair()
        rounds = randint(10000, 10001)
        for i in pairs:
            p1 = i[0]()
            p2 = i[1]()
            match = Match(rounds, p1, p2, self.print_history)
            scores = match.match()
            if p1.name not in self.database:
                self.database[p1.name] = 0
            if p2.name not in self.database:
                self.database[p2.name] = 0

            self.database[p1.name] += scores[0]
            self.database[p2.name] += scores[1]



    def repeat(self):

        for i in range (self.max_round):
            self.round()
        
            if self.print_history:
                print("After Tournament")

                for j in self.database:
                    print(f"{j} : {self.database[j]}")
                print()