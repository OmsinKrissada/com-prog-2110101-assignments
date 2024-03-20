left = "A23456789TJQK"
right = "CDHS"


def diff(c1, c2):
    result = left.index(c1[0]) - left.index(c2[0])
    if result == 0:
        result = right.index(c1[1]) - right.index(c2[1])
    return result


output = ""
deck = input().strip()
for i in range(0, len(deck) - 2, 2):
    val = diff(deck[i] + deck[i + 1], deck[i + 2] + deck[i + 3])
    output += f"+{val}" if val > 0 else str(val)
print(output)
