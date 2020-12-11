data = {}
with open("input.txt") as f:
    lines = [line.strip() for line in f]

for line in lines:
     space_split = line.split()
     comma_split = line.split(",")
     container = space_split[0] + " " + space_split[1]
     item = [j[-3] + " " + j[-2] for j in [i.split() for i in comma_split]]
     amount = [int(j[-4]) if j[-4] != "contain" else 0 for j in [i.split() for i in comma_split]]
     data[container] = dict(zip(item, amount))

def walk(container):
     global s
     for item in data[container]:
          if item == "shiny gold":
               s += 1
               raise Exception

          elif item != "no other":
               walk(item)

def walk_2(container, quantity):
     global s
     for item, amount in zip(data[container].keys(), data[container].values()):

          s += amount * quantity
          
          if item != "no other":
               walk_2(item, amount * quantity)          

def part_1():
     global s
     s = 0
     for container in data:
          try:
               walk(container)
          except:
               pass
     return s

          
def part_2():
     global s
     s = 0
     walk_2("shiny gold", 1)
     return s

print("day 1:", part_1())
print("day 2:", part_2())
