'''
Given this [
  soil-to-fertilizer map:,
  0 15 37,
  37 52 2,
  39 0 15
]
Return  {}
'''

'''
We can just do it inline, we dont need to parse each of the maps
'''
def parseMap(lst):
    pass

def main():
    inputFile = list(open('input.txt'))
    seeds = inputFile[0].split(': ')[1].split()
    beforeConverting = [int(x) for x in seeds]
    afterConverting = []
    # parse each of the maps
    for idx in range(2, len(inputFile)): # skipping seeds and \n
        line = inputFile[idx]
        if line[0] == '\n': # we assume this is a \n case
            # we're moving on from this map to the next one
            # any numbers that havent been mapped by now stay what they were
            afterConverting += [x for x in beforeConverting if x != -1]
            beforeConverting = afterConverting
            afterConverting = []
        splitLine = line.split()
        if len(splitLine) == 3:
            startDestination = eval(splitLine[0])
            startSource = eval(splitLine[1])
            width = eval(splitLine[2])
            # now go through beforeParsing and see if we have a key match
            for i in range(len(beforeConverting)): # ideally we modify beforeConverting
                if beforeConverting[i] == -1:
                    continue
                if beforeConverting[i] in range(startSource, startSource + width):
                    offset = beforeConverting[i] - startSource
                    conversion = startDestination + offset
                    afterConverting.append(conversion)
                    beforeConverting[i] = -1

    # do a final translation
    afterConverting += [x for x in beforeConverting if x != -1]
    return min(afterConverting)

print(main())