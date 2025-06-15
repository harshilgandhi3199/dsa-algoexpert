import pytest
from balancedBrackets import balancedBrackets

def test_balanced_brackets():
    # Test Case 1: Empty string
    assert balancedBrackets("") == True, "Failed: Empty string"

    # Test Case 2: Single pair of brackets
    assert balancedBrackets("()") == True, "Failed: Single pair of brackets"

    # Test Case 3: Nested brackets
    assert balancedBrackets("([])") == True, "Failed: Nested brackets"

    # Test Case 4: Multiple types of brackets
    assert balancedBrackets("{[()]}") == True, "Failed: Multiple types of brackets"

    # Test Case 5: Unbalanced brackets
    assert balancedBrackets("{[(])}") == False, "Failed: Unbalanced brackets"

    # Test Case 6: Overlapping brackets
    assert balancedBrackets("([)]") == False, "Failed: Overlapping brackets"

    # Test Case 7: Only opening brackets
    assert balancedBrackets("(((") == False, "Failed: Only opening brackets"

    # Test Case 8: Only closing brackets
    assert balancedBrackets(")))") == False, "Failed: Only closing brackets"

    # Test Case 9: Mixed brackets with characters
    assert balancedBrackets("a(b)c") == True, "Failed: Mixed brackets with characters"

    # Test Case 10: Mixed brackets with unmatched closing
    assert balancedBrackets("a(b]c") == False, "Failed: Mixed brackets with unmatched closing"

    # Test Case 11: Mixed brackets with unmatched opening
    assert balancedBrackets("a[b(c]") == False, "Failed: Mixed brackets with unmatched opening"

    # Test Case 12: Balanced brackets with extra characters
    assert balancedBrackets("abc{[()]}xyz") == True, "Failed: Balanced brackets with extra characters"

    # Test Case 13: Balanced brackets with spaces
    assert balancedBrackets(" { [ ( ) ] } ") == True, "Failed: Balanced brackets with spaces"

    # Test Case 14: Unbalanced brackets with spaces
    assert balancedBrackets(" { [ ( ] ) } ") == False, "Failed: Unbalanced brackets with spaces"

    # Test Case 15: Long balanced string
    assert balancedBrackets("(((((((((())))))))))") == True, "Failed: Long balanced string"

    # Test Case 16: Long unbalanced string
    assert balancedBrackets("(((((((((()))))))))") == False, "Failed: Long unbalanced string"

    # Test Case 17: No brackets, only characters
    assert balancedBrackets("abcdef") == True, "Failed: No brackets, only characters"

    # Test Case 18: Single unmatched opening bracket
    assert balancedBrackets("(") == False, "Failed: Single unmatched opening bracket"

    # Test Case 19: Single unmatched closing bracket
    assert balancedBrackets(")") == False, "Failed: Single unmatched closing bracket"

    # Test Case 20: Balanced brackets with digits
    assert balancedBrackets("1{2[3(4)5]6}7") == True, "Failed: Balanced brackets with digits"