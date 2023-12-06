with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

seeds = []
seed_soil = []
soil_fertilizer = []
fertilizer_water = []
water_light = []
light_temperature = []
temperature_humidity = []
humidity_location = []

seed_range = []

lists = [seed_soil, soil_fertilizer, fertilizer_water, water_light, light_temperature, temperature_humidity, humidity_location]

curr_list = None
for line in lines:
    if line[:5] == "seeds":
        seeds = [int(z) for z in line[7:].split()]
        for i in range(0, len(seeds), 2):
            seed_range.append([seeds[i], seeds[i+1]])
    elif line == "seed-to-soil map:":
        curr_list = seed_soil
    elif line == "soil-to-fertilizer map:":
        curr_list = soil_fertilizer
    elif line == "fertilizer-to-water map:":
        curr_list = fertilizer_water
    elif line == "water-to-light map:":
        curr_list = water_light
    elif line == "light-to-temperature map:":
        curr_list = light_temperature
    elif line == "temperature-to-humidity map:":
        curr_list = temperature_humidity
    elif line == "humidity-to-location map:":
        curr_list = humidity_location
    elif line:
        curr_list.append([int(z) for z in line.split()])

lowest1 = 9999999999999
lowest2 = lowest1

for s in seeds:
    c = s
    for l in lists:
        for dst, src, size in l:
            if c in range(src, src + size):
                c = dst + (c - src)
                break
    lowest1 = min((c, lowest1))
print(lowest1)

def check_range(l, a, b):
    ret_ranges = []
    ranges = [[a, b]]

    for dst, src, size in l:
        l_range = range(src, src+size)
        new_ranges = []
        for ra, rb in ranges:
            ab_range = range(ra, ra+rb)
            overlap = range(max(ab_range[0], l_range[0]), min(ab_range[-1], l_range[-1])+1)
            if len(overlap) > 0:
                d = overlap[0] - src + dst
                dl = len(overlap)
                ret_ranges.append([d, dl])
                if overlap[0] - 1 in ab_range:
                    leftover = [a, overlap[0] - a]
                    new_ranges.append(leftover)
                if overlap[-1] + 1 in ab_range:
                    leftover = [overlap[-1] + 1, b - (overlap[-1] + 1 - a)]
                    new_ranges.append(leftover)
            else:
                new_ranges.append([ra, rb])
        
        ranges = new_ranges
    return ret_ranges + ranges

for i, l in enumerate(lists):
    new_seed_range = []
    for ra, rb in seed_range:
        new_seed_range += check_range(l, ra, rb)
        tmp = 0
    seed_range = new_seed_range
        
for s in seed_range:
    lowest2 = min(s[0], lowest2)
print(lowest2)
    