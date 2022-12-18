from copy import deepcopy
import time

start_time = time.time()

with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

valves = {}
flow = {}
pos_flow = []
for line in lines:
    a, b = line.split("; ")
    _, v, _, _, rate = a.split()
    rate = int(rate.split("=")[1])
    tunnels = b.split()[4:]
    tunnels = [x.replace(",", "") for x in tunnels]
    valves[v] = tunnels
    flow[v] = rate
    if rate > 0:
        pos_flow.append(v)

# Generate graph of each valve with flow > 0 to each other valve > 0
graph = {}
for z in ["AA"]+pos_flow:
    graph[z] = {}
    found = [z]
    queue = [[z, 0]]
    seen = [z]
    while queue:
        curr_pos, dist = queue.pop(0)
        for t in valves[curr_pos]:
            if t not in seen:
                if flow[t] != 0:
                    found.append(t)
                    graph[z][t] = dist + 1
                seen.append(t)
                queue.append([t, dist + 1])

for a, b in graph.items():
    print(a, b)

# Calculate max flow
max_flow = 0
max_time = 30
# curr_pos, tot_flow, curr_time, open_valvs
next_op = [["AA", 0, 30, []]]
debug = 0
memoization = {}
while next_op:
    # get next value from queue
    curr_pos, tot_flow, curr_time, open_valvs = next_op.pop()

    # check if we have opened all valvs
    if len(open_valvs) == len(pos_flow):
        for v in open_valvs:
            tot_flow += (flow[v] * curr_time)
        if tot_flow > max_flow:
            max_flow = tot_flow
        continue

    # loop through each next node in graph
    for k, v in graph[curr_pos].items():
        if k in open_valvs:
            continue
        # if we have more time left than distance to next node
        if curr_time >= (v + 1):
            new_tot_flow = tot_flow
            # update total flow for the passed minutes
            for valv in open_valvs:
                new_tot_flow += (flow[valv] * (v + 1))
            new_open_valvs = deepcopy(open_valvs)
            new_open_valvs.append(k)
            new_time = curr_time - (v + 1)

            # memoization based on previously found valves
            key = new_open_valvs
            key.sort()
            key = ''.join(key)
            if key not in memoization:
                memoization[key] = (new_tot_flow, new_time)
                next_op.append([k, new_tot_flow, new_time, new_open_valvs])
            else:
                best_tot_flow, best_time = memoization[key]
                if new_tot_flow > best_tot_flow:
                    if new_time >= best_time:
                        memoization[key] = (new_tot_flow, new_time)
                    next_op.append([k, new_tot_flow, new_time, new_open_valvs])
                else:
                    if new_time > best_time:
                        next_op.append([k, new_tot_flow, new_time, new_open_valvs])
            # next_op.append([k, new_tot_flow, new_time, new_open_valvs])

        else:
            tf = tot_flow
            for t in range(curr_time):
                if curr_time - t == 0:
                    if tf > max_flow:
                        max_flow = tf
                    break
                for valv in open_valvs:
                    tf += flow[valv]
            if tf > max_flow:
                max_flow = tf

print(max_flow)
print(time.time() - start_time)

# Part 2
# Calculate max flow
max_flow = 0
max_time = 30
# curr_pos, tot_flow, curr_time, open_valvs
next_op = [["AA", 0, 26, [], "AA", 0, 26, [], []]]
debug = 0
memoization = {}
while next_op:
    # get next value from queue
    my_curr_pos, my_tot_flow, my_curr_time, my_vals, el_curr_pos, el_tot_flow, el_curr_time, el_vals, open_valvs = next_op.pop()

    # check if we have opened all valvs
    if len(open_valvs) == len(pos_flow):
        for v in my_vals:
            my_tot_flow += (flow[v] * my_curr_time)
        for v in el_vals:
            el_tot_flow += (flow[v] * el_curr_time)
        if (my_tot_flow + el_tot_flow) > max_flow:
            max_flow = my_tot_flow + el_tot_flow
            print(max_flow)
        continue

    # check if we both ran out of time
    if my_curr_time == 0 and el_curr_time == 0:
        for v in my_vals:
            my_tot_flow += (flow[v] * my_curr_time)
        for v in el_vals:
            el_tot_flow += (flow[v] * el_curr_time)
        if (my_tot_flow + el_tot_flow) > max_flow:
            max_flow = my_tot_flow + el_tot_flow
            print(max_flow)
        continue

    open_valvs_2 = deepcopy(open_valvs)

    # loop through each next node in graph
    if my_curr_time > 0 and len(my_vals) < len(pos_flow) - 2:
        my_sent = False
        for k, v in graph[my_curr_pos].items():
            if k in open_valvs:
                continue
            # if we have more time left than distance to next node
            if my_curr_time >= (v + 1):
                my_new_tot_flow = my_tot_flow
                # update total flow for the passed minutes
                for valv in my_vals:
                    my_new_tot_flow += (flow[valv] * (v + 1))
                new_open_valvs = deepcopy(open_valvs)
                new_my_vals = deepcopy(my_vals)
                new_open_valvs.append(k)
                new_my_vals.append(k)
                my_new_time = my_curr_time - (v + 1)

                # memoization based on previously found valves
                # key = new_open_valvs
                # key.sort()
                # key = ''.join(key)
                # if key not in memoization:
                #     memoization[key] = (my_new_tot_flow, my_new_time)
                #     next_op.append([k, my_new_tot_flow, my_new_time, new_my_vals, el_curr_pos, el_tot_flow, el_curr_time, el_vals, new_open_valvs])
                # else:
                #     best_tot_flow, best_time = memoization[key]
                #     if my_new_tot_flow > best_tot_flow:
                #         if my_new_time >= best_time:
                #             memoization[key] = (my_new_tot_flow, my_new_time)
                #         next_op.append([k, my_new_tot_flow, my_new_time, new_my_vals, el_curr_pos, el_tot_flow, el_curr_time, el_vals, new_open_valvs])
                #     else:
                #         if my_new_time > best_time:
                #             next_op.append([k, my_new_tot_flow, my_new_time, new_my_vals, el_curr_pos, el_tot_flow, el_curr_time, el_vals, new_open_valvs])
                next_op.append([k, my_new_tot_flow, my_new_time, new_my_vals, el_curr_pos, el_tot_flow, el_curr_time, el_vals, new_open_valvs])
            elif not my_sent:
                tf = my_tot_flow
                for t in range(my_curr_time):
                    for valv in my_vals:
                        tf += flow[valv]
                my_sent = True
                next_op.append([k, my_new_tot_flow, 0, new_my_vals, el_curr_pos, el_tot_flow, el_curr_time, el_vals, new_open_valvs])

    open_valvs = open_valvs_2

    # elephant loops through each next node in graph
    if el_curr_time > 0 and len(el_vals) < len(pos_flow) - 2:
        el_sent = False
        for k, v in graph[el_curr_pos].items():
            if k in open_valvs:
                continue
            # if we have more time left than distance to next node
            if el_curr_time >= (v + 1):
                el_new_tot_flow = el_tot_flow
                # update total flow for the passed minutes
                for valv in el_vals:
                    el_new_tot_flow += (flow[valv] * (v + 1))
                new_open_valvs = deepcopy(open_valvs)
                new_open_valvs.append(k)
                new_el_vals = deepcopy(el_vals)
                new_el_vals.append(k)
                el_new_time = el_curr_time - (v + 1)

                # memoization based on previously found valves
                # key = new_open_valvs
                # key.sort()
                # key = ''.join(key)
                # if key not in memoization:
                #     memoization[key] = (el_new_tot_flow, el_new_time)
                #     next_op.append([k, my_new_tot_flow, my_new_time, new_my_vals, el_curr_pos, el_tot_flow, el_curr_time, el_vals, new_open_valvs])
                # else:
                #     best_tot_flow, best_time = memoization[key]
                #     if el_new_tot_flow > best_tot_flow:
                #         if el_new_time >= best_time:
                #             memoization[key] = (el_new_tot_flow, el_new_time)
                #         next_op.append([k, my_new_tot_flow, my_new_time, new_my_vals, el_curr_pos, el_tot_flow, el_curr_time, el_vals, new_open_valvs])
                #     else:
                #         if el_new_time > best_time:
                #             next_op.append([k, my_new_tot_flow, my_new_time, new_my_vals, el_curr_pos, el_tot_flow, el_curr_time, el_vals, new_open_valvs])
                next_op.append([my_curr_pos, my_tot_flow, my_curr_time, my_vals, k, el_new_tot_flow, el_new_time, new_el_vals, new_open_valvs])
            elif not el_sent:
                tf = el_tot_flow
                for t in range(el_curr_time):
                    for valv in el_vals:
                        tf += flow[valv]
                el_sent = True
                next_op.append([my_curr_pos, my_tot_flow, my_curr_time, my_vals, k, el_new_tot_flow, 0, new_el_vals, new_open_valvs])

print(max_flow)
print(time.time() - start_time)