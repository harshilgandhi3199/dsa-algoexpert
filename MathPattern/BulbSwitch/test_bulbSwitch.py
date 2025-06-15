import pytest
from bulbSwitch import Solution

def test_bulbSwitch():
    solution = Solution()

    # Test Case 1: n = 0 (no bulbs)
    assert solution.bulbSwitch(0) == 0, "Failed for n = 0"

    # Test Case 2: n = 1 (only one bulb, toggled once)
    assert solution.bulbSwitch(1) == 1, "Failed for n = 1"

    # Test Case 3: n = 3 (bulbs [1, 2, 3])
    assert solution.bulbSwitch(3) == 1, "Failed for n = 3"

    # Test Case 4: n = 4 (bulbs [1, 2, 3, 4])
    assert solution.bulbSwitch(4) == 2, "Failed for n = 4"

    # Test Case 5: n = 10 (bulbs [1, 2, ..., 10])
    assert solution.bulbSwitch(10) == 3, "Failed for n = 10"

    # Test Case 6: n = 25 (bulbs [1, 2, ..., 25])
    assert solution.bulbSwitch(25) == 5, "Failed for n = 25"

    # Test Case 7: Large input n = 100 (bulbs [1, 2, ..., 100])
    assert solution.bulbSwitch(100) == 10, "Failed for n = 100"

    # Test Case 8: Edge case n = 2 (bulbs [1, 2])
    assert solution.bulbSwitch(2) == 1, "Failed for n = 2"