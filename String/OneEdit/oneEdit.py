# You're given two strings stringOne and stringTwo. Write a function that determines if these two strings can be
# made equal using only one edit.
# There are 3 possible edits:
# • Replace: One character in one string is swapped for a different character.
# • Add: One character is added at any index in one string.
# • Remove: One character is removed at any index in one string.
# Note that both strings will contain at least one character. If the strings are the same, your function should return true.
# Sample Input
# stringOne = "hello"
# stringTwo = "hollo"
# Sample Output
# True // A single replace at index 1 of either string can make the strings equal

def oneEdit(stringOne, stringTwo):
    # If the strings are already equal, no edits needed
    if stringOne == stringTwo:
        return True

    len1, len2 = len(stringOne), len(stringTwo)

    # If length difference is more than 1, can't be one edit away
    if abs(len1 - len2) > 1:
        return False

    # Case 1: Replacement (same length)
    if len1 == len2:
        differences = sum(1 for a, b in zip(stringOne, stringTwo) if a != b)
        return differences == 1

    # Case 2: Insertion/Deletion (lengths differ by 1)
    # Always make stringOne the shorter one
    if len1 > len2:
        stringOne, stringTwo = stringTwo, stringOne

    i = j = 0
    foundDifference = False
    while i < len(stringOne) and j < len(stringTwo):
        if stringOne[i] != stringTwo[j]:
            if foundDifference:
                return False
            foundDifference = True
            j += 1  # skip character in longer string
        else:
            i += 1
            j += 1

    return True