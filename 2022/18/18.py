ex = """
2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5
"""

from itertools import combinations


# total number of sides is 6 * number of lines

# then go through and find the sides that we need to subtract from that


"""
Given two coordinates, calculate the number of sides that are overlapping
given [2,2,2][1,2,2] => 1


A side is defined as overlapping if it meets two conditions
two of their coordinates must be the same
The third coordinate must be 1 unit away
"""
def calculateOverlap(p1, p2):
    [x1,y1,z1] = p1
    [x2,y2,z2] = p2
    exes = x1 == x2
    whys = y1 == y2
    zees = z1 == z2
    # find all combinations if they're the same
    if (exes and whys):
        if (abs(z1-z2) == 1):
            return 1
        # check zees 
    if (exes and zees):
        if (abs(y1 - y2) == 1):
            return 1
        # check whys
    if (whys and zees):
        if (abs(x1 - x2) == 1):
            return 1
        # check exes
    return 0
    


def main():
    inputFile = open('puzzleInput.txt', 'r')
    totalSides = 1
    overlap = 0
    string = inputFile.read()
    lines = string.split('\n')
    totalSides = 6*len(lines)
    combos = list(combinations(lines, 2))
    for p1,p2 in combos:
      p1 = [eval(i) for i in p1.split(',')]
      p2 = [eval(i) for i in p2.split(',')]
        #(1,2,2),(2,2,2)
      overlap += calculateOverlap(p1,p2)
    return totalSides - (overlap * 2)


print(main())