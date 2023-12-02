'''
The Elf would first like to know which games would have been possible 
if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?
'''

"""
- game is a dictionary of { color: number} of the die necessary to play that game
- cubes is a dictionary of {color: number} of all available colors and number of die of each color
- returns t/f if possible
"""
def isGamePossible(cubes, game):
    for color in game.keys():
        if (cubes[color] < game[color]):
            return False
    return True

"""
given a list of 
[   '3 blue, 4 red',
    '1 red, 2 green, 6 blue',
    '2 green'
]

it'll return an object {color: number} of the minimum number of cubes of each color
necessary to play this game
{ blue: 6
  red: 4,
  green: 2
}
"""
def createGameMapping(subsets):
    # for each line of subset, split on , 
    # for each line of colors, check gameDic, if exists, take max, otherwise set
    gameDic = {}
    for line in subsets:
        for cubes in line.split(','):
            [number, color] = cubes.strip().split(' ')
            if color in gameDic:
                gameDic[color] = max(gameDic[color], int(number))
            else:
                gameDic[color] = int(number)
    return gameDic


"""
For part 2
given a game mapping gotten from createGameMapping, we need to calculate the power of a set of cubes.
The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together.

So for { blue: 6
  red: 4,
  green: 2
}, the power is 48
"""
def getPower(game):
    # iterate through the values and multiply them
    power = 1
    for number in game.values():
        power *= number
    return power

"""
Given a line in the form of 'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green'
it will transform to {color: number} and gameId
"""
def preProcess(inputLine):
    # split on :
    # on the left side, split on " ", then take whats left of the string, that's the id
    [left, right] = inputLine.split(':')
    gameId = left.split(' ')[-1]
    subsets = right.split(';')
    game = createGameMapping(subsets)
    return [int(gameId), game]

def partOne():
    testFile = open('part1.txt', 'r')
    summation = 0
    cubes = {"red": 12, "green": 13, "blue": 14}
    for inputLine in testFile:      
      [gameId, game] = preProcess(inputLine)
      if isGamePossible(cubes, game):
        summation += gameId
    return summation

def partTwo():
    testFile = open('part1.txt', 'r')
    summation = 0
    cubes = {"red": 12, "green": 13, "blue": 14}
    for inputLine in testFile:
        [gameId, game] = preProcess(inputLine)
        summation += getPower(game)
    return summation

print(partTwo())


