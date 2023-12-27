'''
Recursively does the calculation all the way down
'''
def approximateNext(nums):
    if (all(x == 0 for x in nums)):
        return 0
    deltas = [y - x for x, y in zip(nums, nums[1:])]
    diff = approximateNext(deltas)
    return nums[-1] + diff 
    
# we can basically go from right -> left subtracting each one
def main():
    inputFile = open('input.txt')
    nums = 0
    for line in inputFile: 
        nums += approximateNext(list(map(int, line.split())))
    return nums

print(main())