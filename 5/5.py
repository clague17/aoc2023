'''
Given this [
    soil-to-fertilizer map:,
    0 15 37,
    37 52 2,
    39 0 15
]
Return  {}
'''

from tqdm import tqdm, trange
from intervaltree import Interval, IntervalTree


def makeMapping(tree, lines):
    for line in lines:
        startDestination = eval(line[0])
        startSource = eval(line[1])
        width = eval(line[2])
        # Create an interval for the source range with the destination range as its data
        interval = Interval(startSource, startSource + width, (startDestination, startDestination + width))
        tree.add(interval)
    tree.merge_overlaps()
    print('LOL: ', tree.begin())
    return tree

def findMapping(tree, range_start, range_end):
    # Find all intervals that overlap with the input range
    intervals = tree.overlap(range_start, range_end)
    # if there are no overlapping intervals, then the number maps to itself
    mappings = []
    for interval in intervals:
        # Calculate the offset of the start and end of the input range from the start of the source range
        start_offset = range_start - interval.begin
        end_offset = range_end - interval.begin
        # Calculate the corresponding range in the destination space
        mapping_start = interval.data[0] + start_offset
        mapping_end = interval.data[0] + end_offset
        mappings.append((mapping_start, mapping_end))
    return mappings

def main():
    inputFile = list(open('ex.txt'))
    seeds = inputFile[0].split(': ')[1].split()
    # will look like [(), (), ()...], where each tuple is (hasConverted, [start, end])
    answer = []
    tree = IntervalTree()
    for i in trange(1, len(seeds), 2, desc='Parsing seeds line'):
        starting = int(seeds[i - 1])
        offset = int(seeds[i])
        answer.append([False, [starting, starting + offset]])
    idx = 2
    with tqdm(total=len(inputFile), desc='Creating the interval tree') as pbar:
        # step 1: create the interval tree from the input file
        while idx < len(inputFile):
            line = inputFile[idx]
            lines = []
            while line[0].isdigit():
                if line[-2] != ':': # has to be -2 bc of the \n
                    lines.append(line.split())
                idx += 1
                if idx == len(inputFile): break
                line = inputFile[idx]
            if line[0] == '\n':
                tree = makeMapping(tree, lines)
                # iterate through answer. See if there exists a range that matches the mapping. If so, convert it
                # if not, continue. We may not need the hasConverted boolean anymore.
            idx += 1
            # before going to the next map, update the tree!

            if idx >= len(inputFile):
                makeMapping(tree, lines)
                pbar.update(idx)
                break
            pbar.update(idx)
    # step 2: find range overlaps from the answer mapping -> interval tree
    for i in trange(len(answer), desc="Finding range overlaps"):
        ranges = answer[i][1]
        print(findMapping(tree, ranges[0], ranges[1]))
    

def main_old():
    inputFile = list(open('input.txt'))
    seeds = inputFile[0].split(': ')[1].split()
    # will look like [(), (), ()...], where each tuple is (hasConverted, value)
    answer = []
    print('parsing seeds line')
    for i in tqdm.trange(1, len(seeds), 2):
        starting = int(seeds[i - 1])
        offset = int(seeds[i])
        for j in range(starting, starting + offset):
            val = [False, j]
            answer.append(val)
    print('going through each of the maps')
    # parse each of the maps
    for idx in tqdm.trange(2, len(inputFile)): # skipping seeds and \n
        line = inputFile[idx]
        if line[0] == '\n': # we assume this is a \n case
            # we're moving on from this map to the next one
            # any numbers that havent been mapped by now stay what they were
            for i in range(len(answer)): answer[i][0] = False
        splitLine = line.split()
        if len(splitLine) == 3:
            startDestination = eval(splitLine[0])
            startSource = eval(splitLine[1])
            width = eval(splitLine[2])
            # now go through beforeConverting and see if we have a key match
            for i in range(len(answer)): # ideally we modify beforeConverting
                if answer[i][0] == True:
                    continue
                if answer[i][1] in range(startSource, startSource + width):
                    offset = answer[i][1] - startSource
                    conversion = startDestination + offset
                    answer[i][1] = conversion
                    answer[i][0] = True 
    return min(answer, key=lambda x: x[1])[1]

def parseSeeds(seeds):
    answer = []
    for i in trange(1, len(seeds), 2, desc="parsing seeds"):
        start = int(seeds[i - 1])
        offset = int(seeds[i])
        answer.append((start, start + offset))
    return answer

def parseChunks(lines):
    maps = []
    print('lines', lines)
    for line in lines:
        if line[0].isdigit():
            lineItems = line.split()
            destinationStart = eval(lineItems[0])
            sourceStart = eval(lineItems[1])
            width = eval(lineItems[2])
            maps.append(((sourceStart, sourceStart + width), (destinationStart, destinationStart + width)))
    return maps

'''
Given two ranges represented by (start, end) tuples
calculate their overlap

need to figure out a way to splice the ranges if some part of it overlaps and another part doesn't
'''
def doesOverlap(range1, range2):
    if range1[0]

def driver():
    # want to get to a simple [(start, stop)] tuple
    inputFile = list(open('ex.txt'))
    seeds = parseSeeds(inputFile[0].split(': ')[1].split())
    maps = parseChunks(inputFile[2:])
    print(seeds)
    # iterate through source ranges
    # if source range is completely encapsulated by a range in maps[0], then convert it to its destination, maps[1].
    # if partially encapsulated, split the range in maps and split the range in source, convert what can be converted, and just 
    # keep the other range that did not have a corresponding range in map. This is because things in source that do not 
    # map to anything, always map to themselves.
    for entry in seeds:
        for m in maps:
            origin_range = m[0]
            dest_range = m[1]
            if doesOverlap(entry, origin_range):
                # just assuming the full overlap rn
                entry = dest_range
            break



    print(maps)




# Another approach would be to go bottoms up
# Since we know we want the minimum, we can go bottoms up until we have a valid path

# def main_gpt():
#     with open('ex.txt') as f:
#         inputFile = f.readlines()

#     seeds = inputFile[0].split(': ')[1].split()
#     beforeConverting = {int(seeds[i - 1]) + j for i in range(1, len(seeds), 2) for j in range(int(seeds[i]))}

#     afterConverting = []
#     for line in inputFile[2:]:  # skipping seeds and \n
#         if line[0] == '\n':
#             beforeConverting = set(afterConverting)
#             afterConverting = []
#             continue

#         splitLine = line.split()
#         if len(splitLine) == 3:
#             startDestination = int(splitLine[0])
#             startSource = int(splitLine[1])
#             width = int(splitLine[2])

#             for i in list(beforeConverting):  # create a copy to iterate over
#                 if startSource <= i < startSource + width:
#                     offset = i - startSource
#                     conversion = startDestination + offset
#                     afterConverting.append(conversion)
#                     beforeConverting.remove(i)

#     afterConverting += list(beforeConverting)
#     return min(afterConverting)

# print(main())
driver()