owords = input().split()
full = input()


def hide_vowel(w):
    h = ""
    for c in w:
        if c.lower() in "aeiou":
            c = "*"
        h += c
    return h


def less_offensive(t, oword):
    index = t.lower().find(oword.lower())
    original = t[index : index + len(oword)]
    return t[:index] + hide_vowel(original) + t[index + len(oword) :]


adjusted = full

for oword in owords:
    while oword.lower() in adjusted.lower():
        adjusted = less_offensive(adjusted, oword)

print(adjusted)
