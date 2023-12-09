'''
Given this [
    soil-to-fertilizer map:,
    0 15 37,
    37 52 2,
    39 0 15
]
Return  {}
'''

import tqdm

# This just takes too long LOL 
def main():
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

print(main())