boys = []
girls = []

while True:
    name = input("Print boy name or end: ")
    if name != "end":
        boys.append(name)
    else:
        break
while True:
    name = input("Print girl name or end: ")
    if name != "end":
        girls.append(name)
    else:
        break

if len(boys) == len(girls):
    sorted_boys = sorted(boys)
    sorted_girls = sorted(girls)
    print("Результат\nИдеальные пары:")
    for i in range(len(boys)):
        print(sorted_boys[i], "и", sorted_girls[i])
else:
    print("Результат: Внимание, кто-то может остаться без пары.")