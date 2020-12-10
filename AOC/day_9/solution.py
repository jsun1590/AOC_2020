from itertools import combinations
with open("input.txt") as file:
    lines = [int(i.strip()) for i in file]


def recurse(step):
    global invalid, cont, answer
    for i, j in enumerate(lines):

        cont.append(j)
        if len(cont) < step:
            continue
        elif len(cont) > step:

            cont.pop(0)
        if sum(cont) == invalid:
            answer = min(cont) + max(cont)
            raise Exception

    recurse(step+1)
    
def part_1():
    global invalid
    size = 24
    preamble = []
    for i, j in enumerate(lines):
        if i <= size:
            preamble.append(j)
            continue
        combos = [x[0] + x[1] for x in combinations(preamble, 2)]
        if j not in combos:
            invalid = j
            return invalid
        preamble.pop(0)
        preamble.append(j)
        
def part_2():
    global cont, answer
    cont = []
    try:
        recurse(2)
    except:
        return answer
            
print("day 1:", part_1())
print("day 2:", part_2())
