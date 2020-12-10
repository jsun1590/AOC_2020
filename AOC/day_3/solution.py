with open("input.txt") as file:
    lines = [line.strip() for line in file]

def tree_check(x,y):
    pos = [0,0]
    trees = 0
    for i, line in enumerate(lines):
        if i % y != 0:
            continue
        elif pos[1] == i and line[pos[0]%len(line)] == "#":
            trees += 1
            
        pos[0] += x
        pos[1] += y
        
    return trees

print("part 1:", tree_check(3,1))
print("part 2:", tree_check(1,1)*tree_check(3,1)*tree_check(5,1)*tree_check(7,1)*tree_check(1,2))
