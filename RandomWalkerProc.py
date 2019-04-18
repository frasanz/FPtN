import random
def RandomWalkerProc(n):
    position = 0
    walk = [position]
    for i in range(n):
        position += 2*random.randint(0,1)-1
        walk.append(position)
    return walk
