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

'''

# """
# takes in a line in the shape of 
# '467..114..' and returns 467 because it's valid
# """
# def parseLine():
#     pass




'''
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
[i][j] = true/false

"""
def findSymbols(fileLines):
    # symbols = ['!', '@', '#', '$','%','^','&','*','(',')','=','-', '+']
    parsedSymbols = []
    symbols = set([])
    # making the matrix
    for i in range(len(fileLines)):
        row = []
        for c in fileLines[i]:
            if (c.isdigit() or c == '.' or c == '\n'):
                row.append(False)
            else:
                symbols.add(c)
                row.append(True)
        parsedSymbols.append(row)
    print(symbols)
    return parsedSymbols


"""
This function will 
1. evaluate the number. Going from char to multi-digit number
2. Saving the index metadata for that number

[[number, [i[ji, jf]]], where i and j are the indices directly before and after the number
Special cases
123...456
[
  [123, [0, [-1, 3]],
  [456, [0, [5,9]]
]

"""
def parseNumbers(fileLines):
    parseNumbers = []
    for i in range(len(fileLines)):
        j = 0
        while j < len(fileLines[i]):
            # calculating where the window is.
            window = 0
            candidate = ''
            while(fileLines[i][j].isdigit()):
                candidate += fileLines[i][j]
                window += 1
                j += 1
            else:
                if (candidate):
                    number = eval(candidate)
                    left = j - window - 1
                    right = j
                    parseNumbers.append({'num': number, 'i': i, 'ji': left, 'jf': right})
                j += 1
    return parseNumbers

def outOfBoundsWrapper(i, j, maxRow, maxCol, symbols):
    '''
    Check that i and j aren't out of bounds
    '''
    if i < 0 or j < 0 or i > maxRow or j > maxCol: 
        return False
    else:
      try:
          symbol = symbols[i][j]
      except IndexError: 
          print('Out of Bounds: i:{0}, j:{1}. Max {2}, {3}'.format(i, j, maxRow, maxCol))
          return
      return symbols[i][j]

"""
Given an index in grid (i,j), check all possible directions for a symbol
NOTE: need to check the entire width of the number. i.e. a 3 digit number could be adjacent in multiple places
Returns true if symbol found, false otherwise
if i,j is out of bounds, return false
"""
def isValid(i, ji, jf, symbols, maxRow, maxCol):
    # check immediately before, on the same line
    if outOfBoundsWrapper(i, ji, maxRow, maxCol,symbols) or outOfBoundsWrapper(i, jf, maxRow, maxCol, symbols):
        return True

    # check row above and row below
    # row above
    for k in range(ji, jf + 1):
        if outOfBoundsWrapper(i - 1, k, maxRow, maxCol, symbols):
            return True
        
    # row below
    for k in range(ji, jf + 1):
        if outOfBoundsWrapper(i + 1, k, maxRow, maxCol, symbols):
            return True
    return False

def main():
    inputFile = open('input.txt', 'r')
    fileLines = inputFile.readlines()
    maxRow = len(fileLines) - 1
    maxCol = len(fileLines[0]) - 2
    symbols = findSymbols(fileLines)
    print('maxRow', maxRow)
    print('maxCol', maxCol)
    numbers = parseNumbers(fileLines)
    answer = 0
    for entry in numbers:
        number = entry['num']
        i = entry['i']
        ji = entry['ji']
        jf = entry['jf']
        if (isValid(i, ji, jf, symbols, maxRow, maxCol)):
            answer += number
    return answer
    # for each number 

print(main())