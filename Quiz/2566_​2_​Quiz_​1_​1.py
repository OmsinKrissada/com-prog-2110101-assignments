count = int(input())

template_nums = ["K", "Q", "J", "X", "9", "8", "7", "6", "5", "4", "3", "2"]

for line in range(count):
    is_flush = True
    is_straight = True
    is_royal = True

    raw = input()
    cards = raw[1:-1].split("|")
    nums = template_nums[:]
    if cards[0][0] == "A":
        nums.insert(0, "A")
    else:
        nums.insert(len(nums), "A")

    for i, c in enumerate(cards):
        if cards[0][1] != c[1]:
            is_flush = False
        if i > 0 and nums.index(c[0]) - nums.index(cards[i - 1][0]) != 1:
            is_straight = False
        if nums[0] != "A" or nums[i] != c[0]:
            is_royal = False
    if is_straight and is_flush:
        if is_royal:
            print("Royal Straight Flush")
        else:
            print("Straight Flush")
    elif is_straight:
        print("Straight")
    elif is_flush:
        print("Flush")
    else:
        print("None")
