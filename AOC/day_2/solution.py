with open("input.txt") as file:
    lines = [line.strip() for line in file]

def part_1():      
    valid = 0
    for line in lines:
        elem = line.split()
        _min = int(elem[0].split("-")[0])
        _max = int(elem[0].split("-")[1])
        letter = elem[1][0]
        if _min <= elem[2].count(letter) <= _max:
            valid +=1
            
    return valid

def part_2():      
    valid = 0
    for line in lines:
        elem = line.split()
        _min = int(elem[0].split("-")[0])
        _max = int(elem[0].split("-")[1])
        letter = elem[1][0]
        
        if elem[2][_min-1] == letter or elem[2][_max-1] == letter:
            if elem[2][_min-1] == letter and elem[2][_max-1] == letter:
                pass
            else:
                valid +=1
                
    return(valid)

print("part 1:", part_1())
print("part 2:", part_2())
