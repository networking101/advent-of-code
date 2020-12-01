coords = []

with open("inputsmall.txt") as fp:
    line = fp.readline()
    while line:
        coord = line.rstrip().split(',')
        intcoord = [int(i) for i in coord]
        coords.append(intcoord)
        line = fp.readline()

graph = []
for i in coords:
    column = []
    for j in coords:
        temp = abs(i[0]-j[0]) + abs(i[1]-j[1]) + abs(i[2]-j[2]) + abs(i[3]-j[3])
        if temp > 3:
            column.append(0)
        else:
            column.append(temp)
    print column
    graph.append(column)

print "\n"

count = len(graph)
my_set = [0]*count
set_number = 0
visited_all = [0]*count
been_visited = [0]*count
for i in range(len(graph)):
    if been_visited[i] == 0:
        set_number += 1
        my_set[i] = set_number
    for j in range(len(graph[0])):
        if graph[i][j] != 0:
            if been_visited[j] == 0 or visited_all[j] != 0:
                been_visited[j] = 1
                my_set[j] = set_number
    visited_all[j] = 1
    print str(i) + ": " + str(my_set)

        #if graph[i][j] != 0 and been_visited[i] == 0 and been_visited[j] == 0 and i < j:
            #print("X: " + str(i) + "   Y: " + str(j))
            #count -= 1
            #in_set[j] == 1
    #print "Count: " + str(count)
print set_number
