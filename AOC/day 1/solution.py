from itertools import combinations

with open("input.txt") as file:
    lines = [int(line.strip()) for line in file]

def part_1():
    for i in list(combinations(lines, 2)):
        if i[0] + i[1] == 2020:
            return i[0] * i[1]

def part_2():
    for i in list(combinations(lines, 3)):
        if i[0] + i[1] + i[2] == 2020:
            return i[0] * i[1] * i[2]

print("Part 1:", part_1())
print("Part 2:", part_2())
