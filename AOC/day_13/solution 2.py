with open("input.txt") as f:
    lines = f.readlines()
    ids = []
    for i in [i.strip() for i in lines][0].split(","):
        if i == "x":
            ids.append(i)
        else:
            ids.append(int(i))
number = 0
for i in ids:
    if i =="x":
        number +=1
times = {}
iteration = 1
t= 0
def recurse():
    global t, iteration
    n = 1
    for i, j in enumerate(ids):
        if j == "x":
            continue
        elif i == 0:
            t = iteration*j
            iteration += 1
            
        else:
            #print(t, n,j, (t//j)*j+j)
            if t+n+number == (t//j)*j+j:
                #print(t+n)
                n+=1
            else:
                return True

    if n == len(ids)-number:
        print(t, "hello")
        return False

running = True
while running:
    running = recurse()
