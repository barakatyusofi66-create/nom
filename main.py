count = 3
max_son = None

while True:
    son = int(input("Son kiriting (to'xtash uchun 0): "))

    if son == 0:
        break

    if max_son is None or son > max_son:
        max_son = son

    count += 1

print("Eng katta son:", max_son)