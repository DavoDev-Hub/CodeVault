from random import randint

class Die:
    def __init__(self, n, sides = 6):
        self.sides = sides
        self.n = n

    def roll_die(self):
        for x in range(1, self.n +1):
            print(f'{x}. ', randint(1, self.sides))

die = Die(10, 6)
die.roll_die()