from copy import deepcopy

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

DP = {}
def recursion(current_position, time_left, open_valves):
    # If all valves are open, calculate the rest of the time and return
    if time_left == 0:
        return 0

    DPkey = deepcopy(open_valves)
    DPkey.sort()
    DPkey = ''.join(DPkey) + current_position + str(time_left)

    if DPkey in DP:
        return DP[DPkey]

    ret_flows = []
    for next_position, t in graph[current_position].items():
        # If we have opened this valve already, skip
        if next_position in open_valves:
            continue
        # If we have time to open this valve, open it
        if time_left >= (t+1):

            # add next position to new open valves
            new_open_valves = deepcopy(open_valves)
            new_open_valves.append(next_position)

            # run recursion with new_position, subtracted time, and new open valves
            new_total_flow = recursion(next_position, time_left - (t+1), new_open_valves)

            # calculate the additonal flow for moving to this position and opening valve
            for ov in open_valves:
                new_total_flow += flow[ov] * (t+1)

            # append to returned flows from other paths
            ret_flows.append(new_total_flow)
    
    # Calculate the total flow if we don't open any more valves
    new_total_flow = 0
    for ov in open_valves:
        new_total_flow += flow[ov] * (time_left)
    ret_flows.append(new_total_flow)

    max_flow = max(ret_flows)
    DP[DPkey] = max_flow
    return max_flow
        

# Calculate max flow
max_flow = recursion("AA", 30, [])
print(max_flow)


# Part 2
# we now keep track of 2 different instances of valves
# open_valves are valves that are opened across all players.  A player will skip the next valve if already open
# player_valves are valves only opened by the current player.  Used to keep track of total flow for that player

# We also need to use dynamic programming
DP = {}
def recursion2(current_position, time_left, open_valves, player_valves, player):

    if time_left == 0:
        # If we have finished me, switch to the elephant
        if player == 0:
            return recursion2("AA", 26, deepcopy(open_valves), [], 1)
        # If we have run through all players, return 0
        if player == 1:
            return 0

    pv = deepcopy(player_valves)
    pv.sort()
    ov = deepcopy(open_valves)
    ov.sort()
    DPkey = ''.join(ov) + ' ' + ''.join(pv) + ' ' + current_position + ' ' + str(time_left)
    # DPkey = ''.join(pv) + ' ' + current_position + ' ' + str(time_left)
    if DPkey in DP:
        return DP[DPkey]

    # store possible flow values down each path
    ret_flows = []
    # for each other valve with flow > 0
    for next_position, t in graph[current_position].items():
        # If we have opened this valve already, skip
        if next_position in open_valves:
            continue
        # If we have time to open this valve, open it
        if time_left >= (t+1):

            # add next position to new open valves and to the player valves
            new_open_valves = deepcopy(open_valves)
            new_open_valves.append(next_position)
            new_player_valves = deepcopy(player_valves)
            new_player_valves.append(next_position)

            # run recursion2 with new_position, subtracted time, and new open valves
            new_total_flow = recursion2(next_position, time_left - (t+1), new_open_valves, new_player_valves, player)

            # calculate the additonal flow for moving to this position and opening valve
            for pv in player_valves:
                new_total_flow += flow[pv] * (t+1)

            # append to returned flows from other paths
            ret_flows.append(new_total_flow)
    
    # Calculate the total flow if we don't open any more valves
    # This time we need to run recursion incase the elephant is up next
    new_total_flow = recursion2(current_position, 0, deepcopy(open_valves), deepcopy(player_valves), player)
    for pv in player_valves:
        new_total_flow += flow[pv] * (time_left)
    ret_flows.append(new_total_flow)

    max_flow = max(ret_flows)
    DP[DPkey] = max_flow
    return max_flow
        

# Calculate max flow
print(recursion2("AA", 26, [], [], 0))