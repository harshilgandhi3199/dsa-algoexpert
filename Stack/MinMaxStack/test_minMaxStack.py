import pytest
from minMaxStack import MinMaxStack

def test_min_max_stack():
    stack = MinMaxStack()

    # Test Case 1: Push 5
    stack.push(5)
    assert stack.getMin() == 5, "Failed: getMin after pushing 5"
    assert stack.getMax() == 5, "Failed: getMax after pushing 5"
    assert stack.peek() == 5, "Failed: peek after pushing 5"

    # Test Case 2: Push 7
    stack.push(7)
    assert stack.getMin() == 5, "Failed: getMin after pushing 7"
    assert stack.getMax() == 7, "Failed: getMax after pushing 7"
    assert stack.peek() == 7, "Failed: peek after pushing 7"

    # Test Case 3: Push 2
    stack.push(2)
    assert stack.getMin() == 2, "Failed: getMin after pushing 2"
    assert stack.getMax() == 7, "Failed: getMax after pushing 2"
    assert stack.peek() == 2, "Failed: peek after pushing 2"

    # Test Case 4: Pop (should remove 2)
    assert stack.pop() == 2, "Failed: pop after pushing 2"

    # Test Case 5: Pop (should remove 7)
    assert stack.pop() == 7, "Failed: pop after pushing 7"

    # Test Case 6: Check Min, Max, and Peek after pops
    assert stack.getMin() == 5, "Failed: getMin after popping 7 and 2"
    assert stack.getMax() == 5, "Failed: getMax after popping 7 and 2"
    assert stack.peek() == 5, "Failed: peek after popping 7 and 2"