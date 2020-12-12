with open("input.txt") as f:
    lines = [(i[:1], int(i[1:])) for i in [line.strip() for line in f]]

prev = ""
distance = [0,0]
directions = list("NESW")
prev = "E"
for line in lines:
    direction = line[0]

    if direction == "R":
        prev = directions[(directions.index(prev)+line[1]//90)%4]
        continue
    elif direction == "L":
        prev = directions[(directions.index(prev)-line[1]//90)%4]
        continue
    elif direction == "F":
        if prev == "N":
            distance[1] += line[1]
        elif prev == "E":
            distance[0] += line[1]
        elif prev == "S":
            distance[1] -= line[1]
        elif prev == "W":
            distance[0] -= line[1]

    if line[0] == "N":
        distance[1] += line[1]
    elif line[0] == "E":
        distance[0] += line[1]
    elif line[0] == "S":
        distance[1] -= line[1]
    elif line[0] == "W":
        distance[0] -= line[1]

    


print(abs(distance[0])+abs(distance[1]))
        
