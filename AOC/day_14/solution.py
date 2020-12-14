prog = {}
with open("input.txt") as f:
    for line in f:
        if line.startswith("mask"):
            current_mask = line.strip().split()[-1]
            prog[current_mask] = []
        else:
            prog[current_mask].append((int(line.split()[0].partition("[")[2][:-1]), int(line.split()[2])))

max_val = 0
for mask in prog:
    for vals in prog[mask]:
        max_val = vals[0] if max_val < vals[0] else max_val
mem = [0]*(max_val+1)

for ins in prog:
    for vals in prog[ins]:
        mem[vals[0]] = list(str(bin(vals[1]))[2:].zfill(36))
        for i, mask in enumerate(str(ins)):
            if mask != "X":
                mem[vals[0]][i] = mask

nums = [int("".join(num), 2) if num != 0 else 0 for num in mem]
