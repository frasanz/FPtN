import numpy as np
def RandomWalkerNP(n=1000):
    steps = np.random.choice([-1,+1],n)
    return np.cumsum(steps)
walk = RandomWalkerNP(1000)
print(walk)
