with open("input.txt") as file:
    lines = sorted([int(line.strip()) for line in file])

def part_1():
    prev = 0
    gaps = []
    for i in lines:
		gaps.append(i-prev)
        prev = i
    return(gaps.count(1) * (gaps.count(3)+1))

def part_2():
    array = [0]*(lines[-1]+1)
    array[0] = 1
    for i in lines:
        array[i] = array[i-3] + array[i-2] + array[i-1]
    return array[-1]

print("Part 1:", part_1())
print("Part 2:", part_2())
