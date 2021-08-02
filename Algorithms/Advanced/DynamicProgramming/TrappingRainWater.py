"""
https://leetcode.com/explore/featured/card/july-leetcoding-challenge-2021/612/week-5-july-29th-july-31st/3833/
https://leetcode.com/problems/trapping-rain-water/

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.



Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9


Constraints:

n == height.length
0 <= n <= 3 * 104
0 <= height[i] <= 105
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 64 ms, faster than 31.02% of Python3 online submissions for Trapping Rain Water.
# Memory Usage: 15.3 MB, less than 8.25% of Python3 online submissions for Trapping Rain Water.
# class Solution:
#     def trap(self, height: List[int]) -> int:
#         n = len(height)
#         if not n:
#             return 0
#         mx1 = [0] * n
#         mx2 = [0] * n
#         mx1[0] = height[0]
#         mx2[n-1] = height[n-1]
#         for i in range(1, n):
#             mx1[i] = max(mx1[i-1], height[i])
#             i1 = n-1-i
#             mx2[i1] = max(mx2[i1+1], height[i1])
#         return sum(max(0, min(m1, m2)-h) for m1, m2, h in zip(mx1, mx2, height))


# Runtime: 60 ms, faster than 43.97% of Python3 online submissions for Trapping Rain Water.
# Memory Usage: 14.7 MB, less than 97.28% of Python3 online submissions for Trapping Rain Water.
# https://leetcode.com/problems/trapping-rain-water/solution/
class Solution:
    def trap(self, height: List[int]) -> int:
        res, cur, n = 0, 0, len(height)
        st = []
        while cur < n:
            while st and height[cur] > height[st[-1]]:
                t = st.pop()
                if not st:
                    break
                dist = cur - st[-1] - 1
                b_h = min(height[cur], height[st[-1]]) - height[t]
                res += dist * b_h
            st.append(cur)
            cur += 1
        return res


tests = [
    [[0,1,0,2,1,0,1,3,2,1,2,1], 6],
    [[4,2,0,3,2,5], 9]
]

run_functional_tests(Solution().trap, tests)