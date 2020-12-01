import copy
import sys

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
    print ''

def check_path(g, k, y, x, s, key_dict, door_dict, door_list):

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
            

def path_find(g, k, coords, kd, dd, dl):

    queue = []
    step = 0

    queue.append([coords[0], coords[1], step])

    while queue:
    #for i in range(2):
        #print "QUEUE: " + str(queue)
        y, x, step = queue.pop(0)
        g[y][x] = '#'
        step += 1
        if check_path(g, k, y, x+1, step, kd, dd, dl):
            #print "DEBUG RIGHT"
            queue.append([y, x+1, step])
        if check_path(g, k, y, x-1, step, kd, dd, dl):
            #print "DEBUG LEFT"
            queue.append([y, x-1, step])
        if check_path(g, k, y+1, x, step, kd, dd, dl):
            #print "DEBUG DOWN"
            queue.append([y+1, x, step])
        if check_path(g, k, y-1, x, step, kd, dd, dl):
            #print "DEBUG UP"
            queue.append([y-1, x, step])

def main():

    my_map = []
    with open("smallinput.txt") as fp:
        line = fp.readline()
        while line:
            row = [i for i in line.rstrip()]
            my_map.append(row)
            line = fp.readline()

    print_graph(my_map, 0, 0, 1)

    x = 0
    y = 0

    key_dict = {}
    door_dict = {}
    door_list = []

    keys = {}
    for i in range(len(my_map)):
        for j in range(len(my_map[i])):
            if (ord(my_map[i][j]) >= 97 and ord(my_map[i][j]) <= 122) or ord(my_map[i][j]) == 64:
                keys[my_map[i][j]] = [i, j]
                key_dict[my_map[i][j]] = {}
                door_dict[my_map[i][j]] ={} 

    paths = []
    for i in keys:
        mm = copy.deepcopy(my_map)
        path_find(mm, i, keys[i], key_dict, door_dict, door_list)

    for i in key_dict:
        print i + ": " + str(key_dict[i])
        print i + ": " + str(door_dict[i])

    queue = []
    n_map = copy.deepcopy(my_map)

    queue.append([my_map, 0, key_dict, door_dict, door_list, keys['@']])

    #for k in range(5):
    while queue:
        n_map, tot_s, key_dict, door_dict, door_list, coords = queue.pop(0)
        y, x = coords
        print "\n\nNew queue"
        print "Key Dict: " + str(key_dict)
        print "Door Dict: " + str(door_dict)
        print "Door List: " + str(door_list)
        print "\n"
        for i in key_dict['@']:
            print "I: " + str(i)
            print "Steps: " + str(tot_s)
            nn_map = copy.deepcopy(n_map)
            n_key_dict = copy.deepcopy(key_dict)
            n_door_dict = copy.deepcopy(door_dict)
            n_door_list = copy.deepcopy(door_list)

            tot_s += key_dict['@'][i]

            #y, x = keys['@']
            nn_map[y][x] = '.'
            y, x = keys[i]
            nn_map[y][x] = '@'
            #kyes['@'] = [y, x]
            door_list.append(i.upper())

            del n_key_dict[i]
            del n_door_dict[i]
            key_dict['@'] = {}
            #n2_map = copy.deepcopy(nn_map)
            path_find(nn_map, '@', [y, x], n_key_dict, n_door_dict, n_door_list)
            if key_dict['@']:
                queue.append([nn_map, tot_s, n_key_dict, n_door_dict, n_door_list, [y, x]])
            else:
                print "Result: " + str(tot_s)

            #print "Key Dict: " + str(key_dict)
            #print "Door Dict: " + str(door_dict)
            #print "Door List: " + str(door_list)
            print_graph(nn_map, 0, 0, 0)
            #print tot_s
            #print "\n"

    """
    while keys:
        track, tot_s, n_map = queue.pop(0)
        print "\n\nWe are checking all keys reachable by " + track + "\n"
        for i in key_dict[track]:
            print "\n" + track + " -> " + i + "\n\n"
            mm2 = copy.deepcopy(n_map)

            tot_s += key_dict[track][i]
            print "tot_s: " + str(tot_s)
            door_list.append(i.upper())

            path_find(mm2, i, keys[i])

            queue.append([i, tot_s, my_map])

        del key_dict[track]
        my_map[keys[track][0]][keys[track][1]] = '.'
    """
    """
    for i in key_dict:
        print i + ": " + str(key_dict[i])
        print i + ": " + str(door_dict[i])
    print_graph(my_map, 0, 0, 0)
    """

main()




























