file = open("day1_input.txt", "r")
elfs = file.read().split("\n\n")

maximum = [0, 0, 0]
for elf in elfs:
    sum_food = 0
    foods = elf.split("\n")
    for food in foods:
        sum_food += int(food)

    if sum_food > min(maximum):
        maximum.remove(min(maximum))
        maximum.append(sum_food)


print(sum(maximum))
