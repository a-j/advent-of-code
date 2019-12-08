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
    
    leaf_nodes = []
    for key, values in graph.items():
        for value in values:
            if value not in graph:
                leaf_nodes.append(value)
    for node in leaf_nodes:
        graph[node] = []
    return graph

def get_orbit_for_node(graph, node):
    for key, values in graph.items():
        if node in values:
            return key

def compute_min_orbital_transfers(graph, begin, end):
    visited = []
    parent = get_orbit_for_node(graph, begin)
    while parent != 'COM':
        visited.append(parent)
        parent = get_orbit_for_node(graph, parent)

    lca = None
    end_ancestors = []
    parent = get_orbit_for_node(graph, end)
    while parent != 'COM':
        end_ancestors.append(parent)
        if parent in visited:
            lca = parent
            break
        parent = get_orbit_for_node(graph, parent)
    begin_ancestors = visited[:visited.index(lca)+1]
    print(begin_ancestors)
    print(end_ancestors)
    return len(begin_ancestors) + len(end_ancestors)


def compute_orbits_for_node(graph, node):
    if node == 'COM':
        return 0
    for key, value in graph.items():
        if node in value:
            return 1 + compute_orbits_for_node(graph, key)


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
#     'K)L',
#     'K)YOU',
#     'I)SAN'
# ]
with open('input.txt') as file:
    line = file.readline()
    input_map = []
    while line:
        input_map.append(line.strip())
        line = file.readline()

graph = construct_graph(input_map)
begin = get_orbit_for_node(graph, 'YOU')
end = get_orbit_for_node(graph, 'SAN')
print(compute_min_orbital_transfers(graph, begin, end))


### Alternate (much better) solution - https://github.com/Gravitar64/Advent-of-Code-2019/blob/master/AoC_Tag%2006a.py
# from collections import defaultdict
# planets = defaultdict(list)

# # orbits = "COM)B B)C C)D D)E E)F B)G G)H D)I E)J J)K K)L K)YOU I)SAN".split()
# with open('input.txt') as f:
#     orbits = f.read().splitlines()

# for orbit in orbits:
#     planet, satellite = orbit.split(')')
#     planets[planet].append(satellite)
#     planets[satellite].append(planet)
#     if satellite == 'YOU':
#         start = planet
#     if satellite == 'SAN':
#         end = planet

# path = set()
# def find_way(node, counter):
#     path.add(node)
#     if node == end:
#         print(counter)
#         return True
#     for next_node in planets[node]:
#         if next_node in path:
#             continue
#         find_way(next_node, counter+1)

# find_way(start, 0)