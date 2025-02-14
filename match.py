class Match:
    def __init__(self, maxround, prisoner1, prisoner2, printhistory):

        self.maxround = maxround
        self.printhistory = printhistory
        self.p1 = prisoner1
        self.p2 = prisoner2

    def score(self, strategy1, strategy2):
        if strategy1 and strategy2:
            return (3, 3)
        elif strategy1 and not strategy2:
            return (5, 0)
        elif not strategy1 and strategy2:
            return (0, 5)
        else:
            return (1, 1)

    def match(self):
        pr1 = self.p1
        pr2 = self.p2
        score1 = 0
        score2 = 0
        for _ in range(self.maxround):
            strategy1 = pr1.pick_strategy()
            strategy2 = pr2.pick_strategy()
            score = self.score(strategy1, strategy2)
            score1 += score[0]
            score2 += score[1]
            pr1.process_results(strategy1, strategy2, score1, score2)
            pr2.process_results(strategy2, strategy1, score2, score1)

        if self.printhistory:
            print(f"{pr1.name} vs {pr2.name}")
            print(f"{pr1} : {score1}")
            print(f"{pr2} : {score2}")
        
        return (score1, score2)