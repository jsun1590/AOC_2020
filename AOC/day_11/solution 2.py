import copy
with open("input.txt") as f:
    lines = [list(line.strip()) for line in f]

occupied = 0
array = copy.deepcopy(lines)
def seats():
    global lines, occupied
    around = []
    lines = copy.deepcopy(array)
    
    for i, row in enumerate(lines):
        for j, col in enumerate(row):        
            if col == ".":
                continue
            
            elif i == 0:
                around.append(lines[i+1][j])
                if j == 0:
                        around.append(lines[i][j+1])
                        around.append(lines[i+1][j+1])
                        
                elif j == len(row)-1:
                        around.append(lines[i][j-1])
                        around.append(lines[i+1][j-1])
                else:
                    around.append(lines[i][j+1])
                    around.append(lines[i][j-1])
                    around.append(lines[i+1][j+1])
                    around.append(lines[i+1][j-1])
                    
            elif i == len(lines)-1:

                around.append(lines[i-1][j])
                if j == 0:
                    around.append(lines[i-1][j+1])
                    around.append(lines[i][j+1])
                    
                elif j == len(row)-1:
                    around.append(lines[i-1][j-1])
                    around.append(lines[i][j-1])
                else:
                    around.append(lines[i-1][j-1])
                    around.append(lines[i-1][j+1])
                    around.append(lines[i][j-1])
                    around.append(lines[i][j+1])
            else:

                around.append(lines[i-1][j])
                around.append(lines[i+1][j])
                if j == 0:
                    around.append(lines[i-1][j+1])
                    around.append(lines[i][j+1])
                    around.append(lines[i+1][j+1])
                    
                elif j == len(row)-1:
                    around.append(lines[i-1][j-1])
                    around.append(lines[i][j-1])
                    around.append(lines[i+1][j-1])
                    
                else:
                    around.append(lines[i-1][j-1])
                    around.append(lines[i-1][j+1])
                    around.append(lines[i][j-1])
                    around.append(lines[i][j+1])
                    around.append(lines[i+1][j-1])
                    around.append(lines[i+1][j+1])
                    
            if col == "L" and "#" not in around:
                array[i][j] = "#"
                
            elif col == "#" and around.count("#") >= 4:
                array[i][j] = "L"
                
            around = []
    
    for n in array:
        for k in n:
            if k == "#":
                occupied += 1
    print(occupied, "\n")
    occupied = 0
    seats()
        
seats()

