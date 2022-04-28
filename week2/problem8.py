names = ["Peter", "John", "Luke", "Mike"]

for place, name in enumerate(names):
    if place + 1 == 1:
        print(f"{place + 1}st. {name}")
    elif place + 1 == 2:
        print(f"{place + 1}nd. {name}")
    elif place + 1 == 3:
        print(f"{place + 1}rd. {name}")
    else:
        print(f"{place + 1}th. {name}")
