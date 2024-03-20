sum = 0
count = 0

while True:
    received = input()
    if received == 'q':
        break
    count += 1
    sum += float(received)
if count == 0:
    print('No Data')
else:
    print(round(sum/count, 2))
