import math

with open("input.txt") as file:
    lines = [i.strip() for i in file]

ids = []
def part_1():
    global ids
    seat = [[0, 127],[0, 7]]
    
    for line in lines:
        for row in line[:7]:
            if row == "F":
                seat[0][1] = math.floor((seat[0][1]+seat[0][0])/2)
            else:
                seat[0][0] = math.ceil((seat[0][1]+seat[0][0])/2)
        for col in line[-3:]:
            if col == "R":
                seat[1][0] = math.ceil((seat[1][1]+seat[1][0])/2)
            else:
                seat[1][1] = math.floor((seat[1][1]+seat[1][0])/2)
        ids.append(seat[0][0] * 8 + seat[1][0])
        seat = [[0, 127],[0, 7]]
    return max(ids)


def part_2():
    global ids
    return next(iter(set(range(min(ids),max(ids)))-set(ids)))

print("part 1:", part_1())
print("part 2:", part_2())
