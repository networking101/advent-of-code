with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

# Silver
forward = 0
depth = 0

for line in lines:
    direction, magnitude = line.split(" ")
    magnitude = int(magnitude)
    if direction == "forward":
        forward += magnitude
    elif direction == "down":
        depth += magnitude
    elif direction == "up":
        depth -= magnitude

print(forward * depth)

# Gold
forward = 0
depth = 0
aim = 0

for line in lines:
    direction, magnitude = line.split(" ")
    magnitude = int(magnitude)
    if direction == "forward":
        forward += magnitude
        depth += aim * magnitude
    elif direction == "down":
        aim += magnitude
    elif direction == "up":
        aim -= magnitude

print(forward * depth)