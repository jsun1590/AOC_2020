import math
with open("input.txt") as f:
    lines = [(i[:1], int(i[1:])) for i in [line.strip() for line in f]]

distance = [0,0]
directions = list("NESW")
prev = "E"
waypoint = [10, 1]


def rotate(origin, point, angle):
    ox, oy = origin
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return [qx, qy]


for line in lines:
    direction = line[0]

    if direction == "R":
        waypoint = rotate([0,0], waypoint, math.radians(-line[1]))
        continue
    elif direction == "L":
        waypoint = rotate([0,0], waypoint, math.radians(line[1]))
        continue
    elif direction == "F":
        for _ in range(line[1]):
            distance = list(map(sum, zip(*[waypoint, distance])))


    if line[0] == "N":
        waypoint[1] += line[1]
    elif line[0] == "E":
        waypoint[0] += line[1]
    elif line[0] == "S":
        waypoint[1] -= line[1]
    elif line[0] == "W":
        waypoint[0] -= line[1]
    print(distance, waypoint, direction, line)

    


print(abs(distance[0])+abs(distance[1]))
        
