"""
https://leetcode.com/problems/find-the-highest-altitude/

There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.

You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.



Example 1:

Input: gain = [-5,1,5,0,-7]
Output: 1
Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.
Example 2:

Input: gain = [-4,-3,-2,-1,4,3,2]
Output: 0
Explanation: The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. The highest is 0.


Constraints:

n == gain.length
1 <= n <= 100
-100 <= gain[i] <= 100
"""
from typing import List


# Runtime: 36 ms, faster than 70.13% of Python3 online submissions for Find the Highest Altitude.
# Memory Usage: 14.3 MB, less than 8.11% of Python3 online submissions for Find the Highest Altitude.
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxalt = 0
        alt = 0
        for a in gain:
            alt += a
            maxalt = max(maxalt, alt)
        return maxalt


tests = [
    ([-5,1,5,0,-7], 1),
    ([-4,-3,-2,-1,4,3,2], 0)
]

for test in tests:
    result = Solution().largestAltitude(test[0])
    if result == test[1]:
        print("PASS")
    else:
        print("FAIL - " + str(result))