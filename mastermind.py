from random import randint
class mastermind:
    def __init__(self):
        self.correct = [randint(1, 8) for _ in range(4)]
        self.max = 10

    def play(self):
        print("Playing Mastermind with 6 color and 4 positions")
        print(self.correct)
        for i in range(self.max):
            self.ans = []
            self.used = []
            self.inp = input("What is your guess?: ")
            print(f"you guess is {self.inp}")
            for j in range(4):
                if int(self.inp[j]) == self.correct[j]:
                    print('*',end='')
                    self.ans.append('*')
                    self.used.append(self.correct[j])
                elif int(self.inp[j]) in self.correct:
                    if int(self.inp[j]) not in self.used:
                        print('o', end='')
                        self.ans.append('o')
            print('\n')
            self.win = self.ans.count("*")
            if self.win == 4:
                print("You won")
                break





E = mastermind()
E.play()