"""
https://leetcode.com/explore/featured/card/february-leetcoding-challenge-2021/586/week-3-february-15th-february-21st/3643/
https://leetcode.com/problems/container-with-most-water/

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.



Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
Example 3:

Input: height = [4,3,2,1,4]
Output: 16
Example 4:

Input: height = [1,2,1]
Output: 2


Constraints:

n == height.length
2 <= n <= 3 * 104
0 <= height[i] <= 3 * 104
"""
from typing import List


# Runtime: 180 ms, faster than 34.24% of Python3 online submissions for Container With Most Water.
# Memory Usage: 16.5 MB, less than 50.30% of Python3 online submissions for Container With Most Water.
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        v = min(height[r], height[l]) * (r - l)
        result = v
        while l < r:
            if height[l] < height[r]:
                l0 = l
                l += 1
                v -= height[l0]
                v += (min(height[l], height[r]) - height[l0]) * (r - l)
                result = max(result, v)
            else:
                r0 = r
                r -= 1
                v -= height[r0]
                v += (min(height[l], height[r]) - height[r0]) * (r - l)
                result = max(result, v)
        return result


tests = [
    ([1,8,6,2,5,4,8,3,7], 49),
    ([1,1], 1),
    ([4,3,2,1,4], 16),
    ([1,2,1], 2)
]

for test in tests:
    result = Solution().maxArea(test[0])
    if result == test[1]:
        print("PASS")
    else:
        print("FAIL - " + str(result))