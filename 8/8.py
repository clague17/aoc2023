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
    # while there is no cycle
    idx = 0
    iters = 100000 
    traverse = 'AAA'
    with tqdm(total=iters) as pbar:
        while idx < iters:
            if traverse == 'ZZZ':
                return idx
            match instructions[idx % len(instructions)]:
                case 'L':
                    # we take the left one
                    traverse = graph[traverse][0]
                case 'R':
                    traverse = graph[traverse][1]
            idx += 1
            pbar.update(1)    
print(main())