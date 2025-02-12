import math

total_par = 0
total_stroke = 0
total_stroke_fix = 0

for i in range(9):
    par, stroke, choose = [int(x) for x in input().split()]
    total_par += par
    total_stroke += stroke
    if choose == 1:
        total_stroke_fix += min(par + 2, stroke)

handicap = math.floor(0.8 * (1.5 * total_stroke_fix - total_par))

print(total_stroke)
print(handicap)
print(total_stroke - handicap)
