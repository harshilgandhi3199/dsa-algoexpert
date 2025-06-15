# Write a function that takes in a string made up of brackets ( ( [. [.). ]land 3 ) and other optional characters. The function should return a boolean representing whether the string is balanced with regards to brackets.
# A string is said to be balanced if it has as many opening brackets of a certain type as it has closing brackets of that type and if no bracket is unmatched. Note that an opening bracket can't match a corresponding closing bracket that comes before it, and similarly, a closing bracket can't match a corresponding opening bracket that comes after it.
# Also, brackets can't overlap each other as in [(J) •

def balancedBrackets(string):
    # Write your code here.
    # Time - O(n)
    # Space - O(n)
    stack = []
    matching_brackets = {')': '(', '}': '{', ']': '['}

    for char in string:
        # ignore non-bracket characters
        if char.isalpha():
            continue

        # push opening brackets onto the stack
        if char in matching_brackets.values():
            stack.append(char)

        # handle closing brackets
        elif char in matching_brackets:
            # check if stack is empty or if the top of the stack doesn't match
            if len(stack) == 0 or stack[-1] != matching_brackets[char]:
                return False
            
            # pop the matching opening bracket from the stack
            stack.pop()
       
    return len(stack) == 0
                