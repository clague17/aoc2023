from tqdm import tqdm

'''
Given a list of instructions, it will return a dictionary that looks like this that represents the graph
dictA = {'AAA': ['BBB', 'BBB'], 'BBB': ['AAA', 'ZZZ'], 'ZZZ': ['ZZZ', 'ZZZ']}

'''
def parseInstructions(instructions):
    nodes = {}
    for line in instructions:
        [source, dest] = line.split(' = ')
        [left, right] = dest.split(', ')
        nodes[source] = [left[1:], right[:len(right.rstrip()) - 1]]
    return nodes




dictA = {'A': ['B', 'B'], 'B': ['A', 'ZZZ'], 'Z': ['Z', 'Z']}
dictB = {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['Z', 'G'], 'D': ['D', 'D'], 'E': ['E', 'E'], 'G': ['G', 'G'], 'Z': ['Z', 'Z']}

def to_dot(graph):
    dot = "digraph {\n"
    for node, edges in graph.items():
        for edge in edges:
            dot += f'    "{node}" -> "{edge}";\n'
    dot += "}"
    return dot


ex = '''
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
'''
def main():
    inputFile = list(open('input.txt'))
    instructions = inputFile[0].rstrip()
    graph = parseInstructions(inputFile[2:])
    frontier = {x for x in graph.keys() if x[-1] == 'A'}
    frontier_last_chars = {x[-1] for x in frontier}
    # Do i need to check cycles?
    idx = 0
    iters = 100000000000 
    with tqdm(total=iters) as pbar:
        while idx < iters:
            if all(x == 'Z' for x in frontier_last_chars):
                return idx
            instruction = instructions[idx % len(instructions)]
            selection = 0 # assume 'L'
            if instruction == 'R':
                selection = 1
            frontier = {graph[x][selection] for x in frontier}
            frontier_last_chars = {x[-1] for x in frontier}
            idx += 1
            pbar.update(1)
        return idx, set(frontier)
print(main())