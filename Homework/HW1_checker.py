# student_id = "6632155721"

import random

has_id = input("Do you have a student id? [y/n] ")

if has_id == "y":
    student_id = input("Enter student id (663xxxxxxx): ")
    random.seed(31 + int(student_id))
    root = int(random.random() * 8) + 2
    a = int(random.random() * 1000) + 100
    x0 = int(random.random() * (a - 1)) + 1
    print(f"\nk = {root}\na = {a}\nx0 = {x0}\n")

elif has_id == "n":
    root, a, x0 = [int(x) for x in input("Enter k,a,x0 (ex. 5,108,34): ").split(",")]
    student_id = 6630000021
    while student_id <= 6639999999:
        random.seed(31 + student_id)
        c_root = int(random.random() * 8) + 2
        c_a = int(random.random() * 1000) + 100
        c_x0 = int(random.random() * (a - 1)) + 1
        # print(f"Checking {student_id}")
        if root == c_root and a == c_a and x0 == c_x0:
            print(f"\nFound at {student_id}")
            # exit()
            # break
        student_id += 100
    # if student_id == 6639999999:
    #     print("Cannot find a valid student ID")
    #     exit()
else:
    exit()


def calculate(x):
    return x - (x**root - a) / (root * x ** (root - 1))


def distance(x):
    return abs(x**root - a)


def isAcceptable(d):
    return d < 10**-6


def runFromNthX(n):
    if n == 0:
        return calculate(x0)
    return calculate(runFromNthX(n - 1))


def printCheck(n):
    print(
        runFromNthX(n), distance(runFromNthX(n)), isAcceptable(distance(runFromNthX(n)))
    )


n = 0
if isAcceptable(distance(x0)):
    print(
        f"x0 = {x0}, distance = {distance(runFromNthX(n))}",
    )
    exit()
while True:
    if isAcceptable(distance(runFromNthX(n))):
        print(
            f"x{n+1} = {runFromNthX(n)}, distance = {distance(runFromNthX(n))}",
        )
        exit()
    n += 1
