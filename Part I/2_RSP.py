pattern = "RSP"

scores = [0, 0]
won = [False, False]

m = int(input())
for i in range(3 * m):
    p1, p2 = input().split()
    if p1 == p2:
        continue
    elif pattern[(pattern.index(p1) + 1) % 3] == p2:
        scores[0] += 1
        if scores[0] == m:
            won[0] = True
            break
    else:
        scores[1] += 1
        if scores[1] == m:
            won[1] = True
            break

print(scores[0], scores[1])
if won[0]:
    print("Player 1 wins")
elif won[1]:
    print("Player 2 wins")
else:
    print("Tie")
