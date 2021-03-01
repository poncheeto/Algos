#O(nlog(n)) time    O(log(n) space
# Recursive method
def quickSort:
    if len(array) < 2:
        return array
    else:
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quickSort(less) + [pivot] + quickSort(greater)