from datetime import date
entry = input("Enter date here: ")
date_list = entry.split("-")
current = date.today()
difference = current.year - int(date_list[2])

if current.month < int(date_list[1]):
    difference -= 1

print(difference)
