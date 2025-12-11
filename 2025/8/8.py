import networkx as nx

with open("input", "r") as fp:
    lines = [[int(x) for x in line.strip().split(',')] for line in fp]

num_connections = 1000

new_lines = []
for line in lines:
    new_lines.append(tuple(line))
lines = new_lines

G = nx.Graph()
G.add_nodes_from(lines)

distances = {}

for j, y in enumerate(lines):
    for i, x in enumerate(lines[j+1:]):
        a1, b1, c1 = y
        a2, b2, c2 = x
        distances[(y, x)] = abs(a1 - a2)**2 + abs(b2 - b1)**2 + abs(c2 - c1)**2

new_distances = dict(sorted(distances.items(), key=lambda item: item[1]))

i = 0
gold = 0
for k, v in new_distances.items():
    if i == num_connections:
        silver = 1
        silver_found = []
        for j in range(3):
            max_list = []
            for x in list(nx.connected_components(G)):
                if len(x) > len(max_list) and x not in silver_found:
                    max_list = x

            silver *= len(max_list)
            silver_found.append(max_list)

        print(silver)

    G.add_edge(k[0], k[1])
    i += 1

    if len(list(nx.connected_components(G))) == 1:
        k1, k2 = k
        print(k1[0] * k2[0])
        break