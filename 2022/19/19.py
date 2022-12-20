from copy import deepcopy

with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

blueprints = {}
for line in lines:
    bp, robots = [l.strip() for l in line.split(":")]
    bp = int(bp.split()[-1])

    ore_r, clay_r, obsidian_r, geode_r, _ = [r.strip() for r in robots.split(".")]
    
    ore_r = int(ore_r.split()[4])
    clay_r = int(clay_r.split()[4])
    obsidian_r = [int(o) for o in [obsidian_r.split()[4], obsidian_r.split()[7]]]
    geode_r = [int(g) for g in [geode_r.split()[4], geode_r.split()[7]]]
    
    blueprints[bp] = {}
    blueprints[bp]["ore"] = ore_r
    blueprints[bp]["clay"] = clay_r
    blueprints[bp]["obsidian"] = obsidian_r
    blueprints[bp]["geode"] = geode_r

DP = {}
def recursion(bp, time_left, robots, resources):
    global index

    cost_ore = bp["ore"]
    cost_clay = bp["clay"]
    cost_obsidian = bp["obsidian"]
    cost_geode = bp["geode"]

    if time_left == 0:
        return resources[3]

    # dynamic programming
    key =  str(time_left) + str(robots) + str(resources[:3])
    if key in DP:
        # print(f"Found key {key}")
        return DP[key]

    # Increase resources by 1 minute.  We need to run this first and break out into new variable because
    # robots need to be checked on old resource numbers below
    new_resources = deepcopy(resources)
    for r_idx in range(4):
        new_resources[r_idx] += robots[r_idx]

    # If we can create a new robot, do it.  If we can't create any, collect more resources and requeue
    ret_geodes = []
    g_flag = False
    ob_flag = False
    rec_needed = ["geode"]

    # Create geode robot
    if resources[2] >= cost_geode[1]:
        if resources[0] >= cost_geode[0]:
            g_flag = True
            new_robots = deepcopy(robots)
            new_robots[3] += 1
            nr = deepcopy(new_resources)
            nr[0] -= cost_geode[0]
            nr[2] -= cost_geode[1]
            ret_geodes.append(recursion(bp, time_left - 1, new_robots, nr))
        else:
            rec_needed.append("ore")
    # limiting factor is obsidian, rec_needed obsidian
    else:
        rec_needed.append("obsidian")

    # Create obsidian robot
    if resources[1] >= cost_obsidian[1]:
        if resources[0] >= cost_obsidian[0]:
            if "obsidian" in rec_needed:
                if not g_flag:
                    ob_flag = True
                    new_robots = deepcopy(robots)
                    new_robots[2] += 1
                    nr = deepcopy(new_resources)
                    nr[0] -= cost_obsidian[0]
                    nr[1] -= cost_obsidian[1]
                    ret_geodes.append(recursion(bp, time_left - 1, new_robots, nr))
        else:
            rec_needed.append("ore")
    # limiting factor is clay, rec_needed clay
    else:
        rec_needed.append("clay")

    # Create clay robot
    if resources[0] >= cost_clay:
        if "clay" in rec_needed or "obsidian" in rec_needed:
            if not (ob_flag or g_flag):
                c_flag = True
                new_robots = deepcopy(robots)
                new_robots[1] += 1
                nr = deepcopy(new_resources)
                nr[0] -= cost_clay
                ret_geodes.append(recursion(bp, time_left - 1, new_robots, nr))
    # limiting factor is ore, rec_needed ore
    else:
        rec_needed.append("ore")

    # Create ore robot
    if resources[0] >= cost_ore:
        if "ore" in rec_needed or "clay" in rec_needed or "obsidian" in rec_needed:
            if not (ob_flag or g_flag):
                o_flag = True
                new_robots = deepcopy(robots)
                new_robots[0] += 1
                nr = deepcopy(new_resources)
                nr[0] -= cost_ore
                ret_geodes.append(recursion(bp, time_left - 1, new_robots, nr))
    else:
        rec_needed.append("ore")

    # if we couldn't create any robots, continue without creating robots
    if not ret_geodes:
        ret_geodes.append(recursion(bp, time_left - 1, deepcopy(robots), deepcopy(new_resources)))
    # if we could make an geode robot, that is the best path.  Dont check if not making obsidian robot and able
    elif "ore" in rec_needed or "clay" in rec_needed or "obsidian" in rec_needed:
        if not g_flag and not ob_flag:
            ret_geodes.append(recursion(bp, time_left - 1, deepcopy(robots), deepcopy(new_resources)))

    ret_val = max(ret_geodes)
    DP[key] = ret_val
    return ret_val    
        

# Part 1
max_geodes = {}
quality_level = 0
for k, v in blueprints.items():
    max_geodes[k] = recursion(v, 24, [1, 0, 0, 0], [0, 0, 0, 0])
    DP ={}
    quality_level += k * max_geodes[k]
print(quality_level)


# Part 2
tot = 1
for k, v in blueprints.items():
    if k >= 4:
        continue
    ret_val = recursion(v, 32, [1, 0, 0, 0], [0, 0, 0, 0])
    DP ={}
    tot *= ret_val
print(tot)