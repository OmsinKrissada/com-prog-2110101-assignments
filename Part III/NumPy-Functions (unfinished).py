import numpy as np


def eq(A, B, p):
    total = 1
    for side in A.shape:
        total *= side
    for col in A:
        print(col)
    print(total)


def closest_point_indexes(points, p):
    pass


def number_of_inversions(A):
    pass


print(eq(np.array([[1, 2], [3, 4]]), np.array([1, 0]), 50))
