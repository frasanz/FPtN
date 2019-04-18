import random
class RandomWalker:
    def __init__(self):
        self.position = 0
    def walk(self, n):
        self.position = 0
        for i in range(n):
            yield self.position
            self.position +=2*random.randint(0,1)-1
