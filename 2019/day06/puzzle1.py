def construct_graph(map):
    graph = {}
    for orbit in map:
        arr = orbit.split(')')
        left = arr[0]
        right = arr[1]
        if left in graph:
            graph[left].append(right)
        else:
            graph[left] = [right]
    return graph

def compute_orbits_for_node(graph, node):
    if node == 'COM':
        return 0
    for key, value in graph.items():
        if node in value:
            return 1 + compute_orbits_for_node(graph, key)

def compute_orbits(graph):
    vertices = set()
    for key, values in graph.items():
        vertices.add(key)
        for value in values:
            vertices.add(value)
    count = 0
    for node in vertices:
        count += compute_orbits_for_node(graph, node)
    return count

# input_map = [
#     'COM)B',
#     'B)C',
#     'C)D',
#     'D)E',
#     'E)F',
#     'B)G',
#     'G)H',
#     'D)I',
#     'E)J',
#     'J)K',
#     'K)L'
# ]
with open('input.txt') as file:
    line = file.readline()
    input_map = []
    while line:
        input_map.append(line.strip())
        line = file.readline()

graph = construct_graph(input_map)
print(compute_orbits(graph))
#print(compute_orbits_for_node(graph, 'L'))


#### Alternate (much better) solution - https://github.com/Gravitar64/Advent-of-Code-2019/blob/master/AoC_Tag%2006.py
# from collections import defaultdict
# planets = defaultdict(list)

# # orbits = "COM)B B)C C)D D)E E)F B)G G)H D)I E)J J)K K)L".split()
# with open('input.txt') as f:
#     orbits = f.read().splitlines()

# for orbit in orbits:
#     planet, satellite = orbit.split(')')
#     planets[planet].append(satellite)

# orbit_counts = {}
# def count_orbits(node, counter):
#     orbit_counts[node] = counter
#     for satellite in planets[node]:
#         count_orbits(satellite, counter+1)

# count_orbits('COM', 0)
# print(sum(orbit_counts.values()))
