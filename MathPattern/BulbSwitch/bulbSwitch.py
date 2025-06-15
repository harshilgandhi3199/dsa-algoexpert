import math
# https://leetcode.com/problems/bulb-switcher/
# You are given n bulbs, initially turned off.
# There are n rounds of toggling operations that you perform, which are described below:
# In the i-th round, you toggle every bulb whose number is a multiple of i (i.e., bulb i, 2*i, 3*i, ...).
# For example, if n = 3, bulbs are labeled as [1, 2, 3].
# After the first round, the bulbs are [1, 1, 1] (all turned on).
# After the second round, the bulbs are [1, 0, 1] (bulb 2 is turned off).
# After the third round, the bulbs are [1, 0, 0] (bulb 3 is turned off).
# Return the number of bulbs that are on after n rounds.

class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(math.sqrt(n))
        