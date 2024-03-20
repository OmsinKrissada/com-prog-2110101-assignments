words = [input() for _ in range(2)]

total_pairs = {}


def count(id, word):
    for c in word:
        if not c.isalpha():
            continue
        tc = c.lower()
        if tc in total_pairs:
            total_pairs[tc][id] += 1
        else:
            temp = [0, 0]
            temp[id] = 1
            total_pairs[tc] = temp


count(0, words[0])
count(1, words[1])

to_be_removed = ([], [])
for k, v in total_pairs.items():
    if v[0] > v[1]:
        to_be_removed[0].append((k, v[0] - v[1]))
    if v[0] < v[1]:
        to_be_removed[1].append((k, v[1] - v[0]))


for i, tbr_of_word in enumerate(to_be_removed):
    print(words[i])
    if len(tbr_of_word) == 0:
        print(" - None")
        continue
    for pair in sorted(tbr_of_word):
        print(f" - remove {pair[1]} {pair[0]}" + ("'s" if pair[1] > 1 else ""))
