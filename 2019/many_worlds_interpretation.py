import copy
import sys
import itertools
import time

"""
todo:
solve possible gate combinations. recursively travel through gates and append to global gate_combo
create object every time new combo is solved, check to make sure not appending new object
save list to file
"""

door_collection = []

class Routes:
    def __init__(self):
        self.distances = {}
        self.doors = []

    def getDoors(self):
        return self.doors

    def setDoors(self, dlist):
        self.doors = dlist

def print_graph(g, x, y, d):
    for i in range(len(g)):
        for j in range(len(g[i])):
            if i==y and j==x:
                if d == 1:
                    sys.stdout.write('>')
                elif d == 2:
                    sys.stdout.write('v')
                elif d == 3:
                    sys.stdout.write('<')
                elif d == 4:
                    sys.stdout.write('^')
                elif d == 0:
                    sys.stdout.write('0')
            else:
                sys.stdout.write(str(g[i][j]))
        print ''

def init_check_path(g, k, y, x, obj, s):
    print_graph(g, x, y, 0)
    t = g[y][x]
    if t != '#':
        if ord(t) >= 65 and ord(t) <= 90:
            if t not in obj.getDoors():
                return 0
            else:
                return 1
        elif ord(t) >= 97 and ord(t) <= 122 and t != k:
            """
            if k not in obj.distances:
                obj.distances[k] = {t:s}
            else:
                obj.distances[k][t] = s
            """
            if k not in obj.distances:
                obj.distances[k] = {t:s}
            elif t not in obj.distances[k]:
                obj.distances[k][t] = s
            else:
                if s < obj.distances[k][t]:
                    obj.distances[k][t] = s 
            return 1
        elif t == '.' or t == '@':
            return 1
    return 0

def check_path(g, k, y, x, s):

    #print_graph(g, x, y, 0)
    #print "DOOR_DICT: " + str(door_dict)
    #print "KEY_DICT: " + str(key_dict)
    #print "DOOR_LIST: " + str(door_list)

    t = g[y][x]
    #print "K: " + str(k)
    #print "T: " + str(t)
    if t != '#':
        if ord(t) >= 65 and ord(t) <= 90:

            if t not in door_list:
                if t not in door_dict[k]:
                    door_dict[k][t] = s
                return 0
            else:
                try:
                    del door_dict[k][t]
                except:
                    pass
                return 1
        elif ord(t) >= 97 and ord(t) <= 122:
            key_dict[k][t] = s
            return 1
        elif t == '.' or t == '@':
            return 1
    return 0
            

def path_find(grid, k, coords, obj):

    g = copy.deepcopy(grid)
    queue = []
    step = 0

    queue.append([coords[0], coords[1], step])

    while queue:
    #for i in range(2):
        #print "QUEUE: " + str(queue)
        y, x, step = queue.pop(0)
        g[y][x] = '#'
        step += 1
        if init_check_path(g, k, y, x+1, obj, step):
            #print "DEBUG RIGHT"
            queue.append([y, x+1, step])
        if init_check_path(g, k, y, x-1, obj, step):
            #print "DEBUG LEFT"
            queue.append([y, x-1, step])
        if init_check_path(g, k, y+1, x, obj, step):
            #print "DEBUG DOWN"
            queue.append([y+1, x, step])
        if init_check_path(g, k, y-1, x, obj, step):
            #print "DEBUG UP"
            queue.append([y-1, x, step])

def main():

    global door_collection

    my_map = []
    with open("input.txt") as fp:
        line = fp.readline()
        while line:
            row = [i for i in line.rstrip()]
            my_map.append(row)
            line = fp.readline()

    print_graph(my_map, 0, 0, 1)

    x = 0
    y = 0

    keys = {}
    doors = []
    for i in range(len(my_map)):
        for j in range(len(my_map[i])):
            if (ord(my_map[i][j]) >= 97 and ord(my_map[i][j]) <= 122) or my_map[i][j] == '@':
                keys[my_map[i][j]] = [i, j]
            if ord(my_map[i][j]) >= 65 and ord(my_map[i][j]) <= 90:
                doors.append(my_map[i][j])

    print "DEBUG 1"
    start = time.time()
    print start

    for i in range(len(doors)+1):
        for j in itertools.combinations(doors, i):
            temp = Routes()
            temp.setDoors(sorted(list(j)))
            door_collection.append(temp)
        print i
    
    end = time.time()
    print "DEBUG 2"
    print end
    f = open("time.txt", 'a')
    f.write("time: " + str(end-start))
    f.close()
    print end-start
    
    """
    for i in door_collection:
        print i.getDoors()
    print "\n"
    """
    """
    for i in door_collection:
        for j in keys:
            path_find(my_map, j, keys[j], i) 
        print str(i.getDoors()) + "     " + str(i.distances)
    """
    """
    last = door_collection[len(door_collection)-1]
    for j in keys:
        path_find(my_map, j, keys[j], last)
    print str(last.getDoors()) + "     " + str(last.distances)
    """
    for i in door_collection:
        for j in keys:
            path_find(my_map, j, keys[j], i)
        #print str(i.getDoors()) + "     " + str(i.distances)
    

main()




























