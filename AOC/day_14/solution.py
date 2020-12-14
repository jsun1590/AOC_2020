prog = {}
with open("input.txt") as f:
    for line in f:
        if line.startswith("mask"):
            current_mask = line.strip().split()[-1]
            prog[current_mask] = []
        else:
            prog[current_mask].append((int(line.split()[0].partition("[")[2][:-1]), int(line.split()[2])))
mem = {}

for ins in prog:
    for vals in prog[ins]:
        mem[vals[0]] = list(str(bin(vals[1]))[2:].zfill(36))
        for i, mask in enumerate(str(ins)):
            if mask != "X":
                mem[vals[0]][i] = mask

nums = [int("".join(mem[num]), 2) if mem[num] != 0 else 0 for num in mem]
print(sum(nums))
