with open("input.txt") as file:
    lines = [i.split() for i in [line.strip() for line in file]]

def reader(ins):
    global acc
    if ins in dupes:
        raise Exception

    dupes.append(ins)
    if lines[ins][0] == "nop":
        reader(ins+1)
    elif lines[ins][0] == "acc":
        acc += int(lines[ins][1])
        reader(ins+1)
    elif lines[ins][0] == "jmp":
        reader(ins+int(lines[ins][1]))
        
    
def part_1():
    global acc, dupes
    acc = 0
    dupes = []
    try:
        reader(0)
    except:
        return acc
    
def part_2():
    global acc, dupes
    acc = 0
    dupes = []
    for i, j in enumerate(lines):
        if lines[i][0] == "jmp":
            lines[i][0] = "nop"
            
        elif lines[i][0] == "nop":
            lines[i][0] = "jmp"
        elif lines[i][0] == "acc":
            continue
        
        try:
            reader(0)
            print(acc)

        except IndexError:
            return acc
        
        except Exception:
            if lines[i][0] == "nop":
                lines[i][0] = "jmp"
            
            elif lines[i][0] == "jmp":
                lines[i][0] = "nop"
            dupes = []
            acc = 0
            
print("day 1:", part_1())
print("day 2:", part_2())
