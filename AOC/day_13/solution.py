with open("input.txt") as f:
    lines = f.readlines()
    timestamp = int([i.strip() for i in lines][0])
    ids = []
    for i in [i.strip() for i in lines][1].split(","):
        if i == "x":
            ids.append(i)
        else:
            ids.append(int(i))

times = {}
for i in ids:
    if i == "x":
        pass
    else:
        times[(timestamp//i)*i+i] = i

print((min(times)-timestamp)*times[min(times)])
