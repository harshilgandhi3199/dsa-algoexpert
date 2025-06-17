import pytest
from sunsetViews import sunsetViews

def test_sunset_views():
    # Test Case 1: Example case with direction "EAST"
    buildings = [3, 5, 4, 4, 3, 1, 3, 2]
    direction = "EAST"
    assert sunsetViews(buildings, direction) == [1, 3, 6, 7], "Failed: Example case with direction EAST"

    # Test Case 2: Example case with direction "WEST"
    direction = "WEST"
    assert sunsetViews(buildings, direction) == [0, 1], "Failed: Example case with direction WEST"

    # Test Case 3: All buildings of the same height
    buildings = [4, 4, 4, 4]
    direction = "EAST"
    assert sunsetViews(buildings, direction) == [3], "Failed: All buildings same height with direction EAST"

    direction = "WEST"
    assert sunsetViews(buildings, direction) == [0], "Failed: All buildings same height with direction WEST"

    # Test Case 4: Increasing heights
    buildings = [1, 2, 3, 4, 5]
    direction = "EAST"
    assert sunsetViews(buildings, direction) == [4], "Failed: Increasing heights with direction EAST"

    direction = "WEST"
    assert sunsetViews(buildings, direction) == [0, 1, 2, 3, 4], "Failed: Increasing heights with direction WEST"

    # Test Case 5: Decreasing heights
    buildings = [5, 4, 3, 2, 1]
    direction = "EAST"
    assert sunsetViews(buildings, direction) == [0, 1, 2, 3, 4], "Failed: Decreasing heights with direction EAST"

    direction = "WEST"
    assert sunsetViews(buildings, direction) == [0], "Failed: Decreasing heights with direction WEST"

    # Test Case 6: Single building
    buildings = [10]
    direction = "EAST"
    assert sunsetViews(buildings, direction) == [0], "Failed: Single building with direction EAST"

    direction = "WEST"
    assert sunsetViews(buildings, direction) == [0], "Failed: Single building with direction WEST"

    # Test Case 7: No buildings
    buildings = []
    direction = "EAST"
    assert sunsetViews(buildings, direction) == [], "Failed: No buildings with direction EAST"

    direction = "WEST"
    assert sunsetViews(buildings, direction) == [], "Failed: No buildings with direction WEST"

    # Test Case 8: Mixed heights
    buildings = [2, 3, 1, 5, 6, 2, 4]
    direction = "EAST"
    assert sunsetViews(buildings, direction) == [4, 6], "Failed: Mixed heights with direction EAST"

    direction = "WEST"
    assert sunsetViews(buildings, direction) == [0, 1, 3, 4], "Failed: Mixed heights with direction WEST"

    # Test Case 9: Tallest building in the middle
    buildings = [1, 2, 10, 2, 1]
    direction = "EAST"
    assert sunsetViews(buildings, direction) == [2, 3, 4], "Failed: Tallest building in the middle with direction EAST"

    direction = "WEST"
    assert sunsetViews(buildings, direction) == [0, 1, 2], "Failed: Tallest building in the middle with direction WEST"