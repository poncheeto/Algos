# O(2^n) time    O(n) space
# Recursive
def getNthFib(n):
    if n == 2:
        return 1
    elif n == 1:
        return 0
    else:
         return getNthFib(n - 1) + getNthFib(n - 2)

# O(n) time     O(1) space
# Iterative
def getNthFib:
    firstNum = 0
    secondNum = 1
    counter = 3
    
    while counter <= n:
        fibNum = firstNum + secondNum
        firstNum = secondNum
        secondNum = fibNum
        counter += 1
    return secondNum if n > 1 else firstNum


