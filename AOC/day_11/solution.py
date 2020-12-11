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

            n = []
            ne = []
            e = []
            se = []
            s = []
            sw = []
            w = []
            nw = []
            
            pos = i
            while pos >= 0:
                n.append(lines[pos][j])
                pos -= 1
            n.pop(0)

            pos = [i, j]
            while pos[0] >= 0 and pos[1] <= len(row)-1:
                ne.append(lines[pos[0]][pos[1]])
                pos[0] -= 1
                pos[1] += 1
            ne.pop(0)            

            pos = j
            while pos <= len(row)-1:
                e.append(lines[i][pos])
                pos += 1
            e.pop(0)

            pos = [i, j]
            while pos[0] <= len(lines)-1 and pos[1] <= len(row)-1:
                se.append(lines[pos[0]][pos[1]])
                pos[0] += 1
                pos[1] += 1
            se.pop(0)
            
            pos = i
            while pos <= len(lines)-1:
                s.append(lines[pos][j])
                pos += 1
            s.pop(0)

            pos = [i, j]
            
            while pos[0] <= len(lines)-1 and pos[1] >= 0:
                sw.append(lines[pos[0]][pos[1]])
                pos[0] += 1
                pos[1] -= 1
            sw.pop(0)
       

            pos = j
            while pos >= 0:
                w.append(lines[i][pos])
                pos -= 1
            w.pop(0)

            pos = [i, j]
            while pos[0] >= 0 and pos[1] >= 0:
                nw.append(lines[pos[0]][pos[1]])
                pos[0] -= 1
                pos[1] -= 1
            nw.pop(0)

            n = [i for i in n if i != "."]
            ne = [i for i in ne if i != "."]
            e = [i for i in e if i != "."]
            se = [i for i in se if i != "."]
            s = [i for i in s if i != "."]
            sw = [i for i in sw if i != "."]
            w = [i for i in w if i != "."]
            nw = [i for i in nw if i != "."]

            #print(se)
            try:
                around.append(n[0])
            except:
                pass
            try:
                around.append(ne[0])
            except:
                pass
            try:
                around.append(e[0])
            except:
                pass
            try:
                around.append(se[0])
            except:
                pass            
            try:
                around.append(s[0])
            except:
                pass
            try:
                around.append(sw[0])
            except:
                pass            
            try:
                around.append(w[0])
            except:
                pass
            try:
                around.append(nw[0])
            except:
                pass
            
            if col == "L" and "#" not in around:
                array[i][j] = "#"
                
            elif col == "#" and around.count("#") >= 5:
                array[i][j] = "L"

            #print(around)
            around = []
    
    for n in array:
        for k in n:
            if k == "#":
                occupied += 1
        #print(n)
    print(occupied, "\n")
    occupied = 0
    seats()
        
seats()

