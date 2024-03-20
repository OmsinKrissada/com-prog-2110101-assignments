scores = [0, 0]
point_map = "XRYGWBPK"

while True:
    player, *holes = input()
    scores[int(player) - 1] += point_map.index(holes[0])
    if len(holes) == 2:
        scores[int(player) - 1] += point_map.index(holes[1])
    if holes[0] == "K":
        break

print(f"{scores[0]} {scores[1]}")

if scores[0] > scores[1]:
    print("Player 1 wins")
elif scores[0] < scores[1]:
    print("Player 2 wins")
else:
    print("Tie")
