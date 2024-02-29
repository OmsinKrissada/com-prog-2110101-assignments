pattern = input()
count = int(input())

for i in range(count):
    text = input()
    repeated = 0
    while pattern * repeated in text:
        repeated += 1
    print(repeated - 1 if repeated > 2 else 0)
