# O(n) time     O(1) space
def isValidSubsequence(array, seq):
    seqIndex = 0
    for value in array:
        if seqIndex == len(seq):
            break
        if seq[seqIndex] == value:
            seqIndex += 1
    return seqIndex == len(seq)