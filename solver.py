from cube_class import Cube, face, axis
import pickle
import numpy as np
from time import time

def distance(puzzle):
    arr = puzzle.idx()
    if arr == [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5]:
        return 0
    data = np.array([arr])
    prediction = knn.predict(data)
    res = prediction[0]
    if res == 0:
        res = 1
    #print(res)
    return res

def search(puzzle, depth, dis):
    global path
    if depth == 0:
        if dis == 0:
            return True
    else:
        if dis == 0:
            return True
        if dis <= depth + 1:
            l_twist = path[-1] if len(path) >= 1 else -10
            ll_twist = path[-2] if len(path) >= 2 else -10
            for twist in range(18):
                if face(twist) == face(l_twist) or axis(twist) == axis(l_twist) == axis(ll_twist):
                    continue
                n_puzzle = puzzle.move(twist)
                n_dis = distance(n_puzzle)
                if n_dis > dis + 1:
                    continue
                path.append(twist)
                if search(n_puzzle, depth - 1, n_dis):
                    return True
                path.pop()
        return False

def solver(puzzle):
    global path
    print('depth', end=' ',flush=True)
    strt = time()
    dis = distance(puzzle)
    for depth in range(30):
        print(depth, end=' ', flush=True)
        path = []
        if search(puzzle, depth, dis):
            for twist in path:
                puzzle = puzzle.move(twist)
            print('')
            for i in path:
                print(move_candidate[i], end=' ')
            print('')
            print(time() - strt, 'sec')
            break


#                  0     1     2    3     4    5     6     7    8     9    10    11    12   13    14    15   16    17
move_candidate = ["R", "R2", "R'", "L", "L2", "L'", "U", "U2", "U'", "D", "D2", "D'", "F", "F2", "F'", "B", "B2", "B'"]

filename = 'model.sav'
knn = pickle.load(open(filename, 'rb'))

scramble = [move_candidate.index(i) for i in input().split()]
print('distance', len(scramble))
#print(scramble)

puzzle = Cube()
for i in scramble:
    puzzle = puzzle.move(i)
print('predicted', distance(puzzle))

path = []
solver(puzzle)