# O(log(n)) time	O(1) space
# Iterative 
def binarySearch(array, target):
    low = 0
	high = len(array) - 1
	
	while low <= high:
		mid = (low + high) // 2
		guess = array[mid]
		if guess == target:
			return mid
		elif guess > target:
			high = mid - 1
		else:
			low = mid + 1
	return -1

# O(log(n)) time	O(log(n)) space
# Recursive
def binarySearch(array, target):
    return binarySearchHelper(array, target, 0, len(array) - 1)

def binarySearchHelper(array, target, low, high):
	
	if low > high:
		return -1
	mid = (low + high) // 2
	guess = array[mid]
	if guess == target:
		return mid
	elif guess > target:
		return binarySearchHelper(array, target, low, mid - 1)
	else: 
		return binarySearchHelper(array, target, mid + 1, high)
