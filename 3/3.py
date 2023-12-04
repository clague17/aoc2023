'''
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
'''

'''
......755.
...$.*....
.664.598..
'''


'''
iterate through each line
starting with the second line. Check above and below and diagonal to see if there's symbol
if so, add to list, if not, skip

At the end of iteration, return the sum over list

......755.
...$.*....
.664.598..
'''

# IDEA: 
'''
What if we have three functions. 
1. Scans the whole file and sees where all the symbols are and returns their coordinates
2. Scans the whole file and returns the numbers (in '357' -> 357) and their coordinates
3. Driver function that iterates through the numbers in 2 and checkForSymbol() each.
'''


"""
1. Scans the whole file and sees where all the symbols are and returns their coordinates
Returns the coordinates of the symbols in the document [[i, j], [i1, j1]...]

"""
def findSymbols(fileLines):
    coords = []
    for i in range(len(fileLines)):
        for j, c in enumerate(fileLines[i]):
            if not (c.isdigit() or c == '.' or c == '\n'):
                coords.append((i, j))
    return coords


def parseNumbers(fileLines):
    parseNumbers = {}
    for i in range(len(fileLines)):
        j = 0
        while j < len(fileLines[i]):
            candidate = ''
            while j < len(fileLines[i]) and fileLines[i][j].isdigit():
                candidate += fileLines[i][j]
                j += 1
            if candidate:
                number = int(candidate)
                for l in range(j - len(candidate), j):
                    parseNumbers[(i, l)] = number
            j += 1
    return parseNumbers

"""
This function will 
1. evaluate the number. Going from char to multi-digit number
2. Saving the index metadata for that number
parseNumbers.append({'num': number, 'i': i, 'ji': left, 'jf': right})
"""
def outOfBoundsWrapper(i, j, maxRow, maxCol, symbols):
    if i < 0 or j < 0 or i >= maxRow or j >= maxCol: 
        return False
    return symbols[i][j]



"""
Given an index in grid (i,j), check all possible directions for a symbol
NOTE: need to check the entire width of the number. i.e. a 3 digit number could be adjacent in multiple places
Returns true if symbol found, false otherwise
if i,j is out of bounds, return false
"""
def isValid(i, ji, jf, symbols, maxRow, maxCol):
    if outOfBoundsWrapper(i, ji, maxRow, maxCol,symbols) or outOfBoundsWrapper(i, jf, maxRow, maxCol, symbols):
        return True
    for k in range(ji, jf + 1):
        if outOfBoundsWrapper(i - 1, k, maxRow, maxCol, symbols) or outOfBoundsWrapper(i + 1, k, maxRow, maxCol, symbols):
            return True
    return False

def indexWrapper(i, j, numbers):
    return numbers.get((i, j))



'''
Given a symbol at (i, j), search all 8 directions to find all adjacent numbers
Take care not to count number twice.

i and j are integers, numbers is the form of, denoting the coordinate and the number value {(0, 1): 755, (0, 2): 755, (0, 3): 755, (2, 0): 598, (2, 1): 598, (2, 2): 598}

The bug in the previous code was that we were double counting a number as a neighbor. 
for the input findNeighbors(1, 0, {(0, 1): 755, (0, 2): 755, (0, 3): 755, (2, 0): 598, (2, 1): 598, (2, 2): 598})
We return [755, 598, 598] but the correct answer is [755, 598]. This is because we are double counting 598. 
'''

def findNeighbors(i, j, numbers):
    '''
    case 1: .567...456..
            ....*...

    case 2: ...567.456..
            ....*...
    '''
    directions = [(i - 1, j - 1), (i, j - 1), (i + 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j + 1), (i + 1, j), (i + 1, j + 1)]
    neighbors = set([])

    seen = set()
    for di, dj in directions:
        if (di, dj) in numbers and (di, dj) not in seen:
            neighbors.add(numbers[(di, dj)])
            # Add the first cell of the number to the seen set
            seen.add((di, dj))
    return neighbors


def main():
    inputFile = open('input.txt', 'r')
    fileLines = inputFile.readlines()
    symbols = findSymbols(fileLines)
    numbers = parseNumbers(fileLines)
    answer = 0
    for entry in symbols:
        i, j = entry
        neighbors = findNeighbors(i, j, numbers)
        gear_ratio = 1
        if len(neighbors) == 2:
            for n in neighbors:
                gear_ratio *= n
            answer += gear_ratio
    return answer

print(main())


'''
input: 
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..

any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)
In this schematic, there are two gears. The first is in the top left; it has part numbers 467 and 35, so its gear ratio is 16345. The second gear is in the lower right; its gear ratio is 451490. (The * adjacent to 617 is not a gear because it is only adjacent to one part number.) Adding up all of the gear ratios produces 467835.
'''