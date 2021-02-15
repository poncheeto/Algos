# Olog(n^2) time    O(1) space
# Brute force
def twoNumberSum(array, targetSum):
    for i in range(len(array) - 1):
        firstNum = array[i]
        for j in range(i + 1, len(array)):
            secondNum = array[j]
            if firstNum + secondNum == targetSum: 
                return [firstNum, secondNum] 
    return []

print(twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10)


# O(nlogn) time     O(1) space
# Sorted and using pointers
def twoNumberSum(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1
	
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left], array[right]]
        elif currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right -= 1
    return []

print(twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10))