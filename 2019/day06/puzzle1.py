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
