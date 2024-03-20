method_duration = {"E": 1, "Q": 3, "N": 7, "F": 14}


def get_arrive_date(method, day):
    y, m, d = day
    if y < 2558:
        return "Invalid year"
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ad = y - 543
    if ad % 400 == 0 or (ad % 4 == 0 and ad % 100 != 0):
        days_in_month[1] = 29
    if m < 1 or m > 12:
        return "Invalid month"
    if d <= 0 or d > days_in_month[m - 1]:
        return "Invalid date"

    if method not in method_duration:
        return "Invalid delivery type"

    new_d = d + method_duration[method]
    new_m = m
    new_y = y
    if new_d > days_in_month[m - 1]:
        new_d -= days_in_month[m - 1]
        new_m += 1
    if new_m > 12:
        new_m = 1
        new_y += 1
    return (new_y, new_m, new_d)


delivered = []
while True:
    raw = input()
    if raw == "END":
        break
    fields = raw.split()
    result = get_arrive_date(
        fields[1], (int(fields[4]), int(fields[3]), int(fields[2]))
    )
    if isinstance(result, str):
        print(f"Error: {raw} --> {result}")
    else:
        delivered.append((result, fields[0]))

delivered.sort()

for date, id in delivered:
    print(f"{id}: delivered on {date[2]}/{date[1]}/{date[0]}")
