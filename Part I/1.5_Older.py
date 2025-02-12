months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

names = []
birthdate = []
for i in range(2):
    name, month, date, year = input().split()
    month = months.index(
        month
    )  # No need to be exact. January being 0 is okay since we are only using it for comparation.
    date = int(date[:-1])
    year = int(year)
    birthdate.append([year, month, date])
    names.append(name)

if birthdate[0] < birthdate[1]:
    print(names[0])
elif birthdate[1] < birthdate[0]:
    print(names[1])
else:
    print(names[0], names[1])
