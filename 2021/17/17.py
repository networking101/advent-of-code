with open("input", "r") as fp:
    line = fp.readline().strip()

#Silver
print(sum(list(range(max(abs(min(range([int(t) for t in line.split(" ")[3][2:].split("..")][0], [int(t) for t in line.split(" ")[3][2:].split("..")][1] + 1))), abs(max(range([int(t) for t in line.split(" ")[3][2:].split("..")][0], [int(t) for t in line.split(" ")[3][2:].split("..")][1] + 1))))))))

_, _, x, y = [a[2:] for a in line.split(" ")]
x = [int(t) for t in x[:-1].split("..")]
y = [int(t) for t in y.split("..")]
xRange = range(x[0], x[1] + 1)
yRange = range(y[0], y[1] + 1)

# Gold
def stepx(vx, x):
    x += vx
    if vx > 0:
        vx -= 1
    if vx < 0:
        vx += 1
    return (vx, x)
	
def stepy(vy, y):
    y += vy
    vy -= 1
    return (vy, y)
	
x, y = 0, 0

# Get min and max vx
maxVX = max(xRange)
for i in range(1, 100):
    j = 0
    vj = i
    while vj > 0:
        vj, j = stepx(vj, j)
		
    if j >= min(xRange):
        minVX = i
        break
		
minVY = min(yRange)
maxVY = max(abs(min(yRange)), abs(max(yRange)))

hits = []
maxHeight = 0
for j in range(minVY, maxVY + 1):
    for i in range(minVX, maxVX + 1):
        tx = 0
        ty = 0
        tvy = j
        tvx = i
		
        currMaxHeight = 0
		
        while ty >= min(yRange):
            tvy, ty = stepy(tvy, ty)
            tvx, tx = stepx(tvx, tx)
            if ty > currMaxHeight:
                currMaxHeight = ty
            if tx in xRange and ty in yRange:
                if currMaxHeight > maxHeight:
                    maxHeight = currMaxHeight
                hits.append([i, j])
                break
print(len(hits))
