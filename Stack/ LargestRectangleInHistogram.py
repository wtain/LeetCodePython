"""
https://leetcode.com/problems/largest-rectangle-in-histogram/
https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/573/week-5-december-29th-december-31st/3587/

Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.




Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].




The largest rectangle is shown in the shaded area, which has area = 10 unit.



Example:

Input: [2,1,5,6,2,3]
Output: 10

Runtime: 108 ms, faster than 42.57% of Python3 online submissions for Largest Rectangle in Histogram.
Memory Usage: 16.3 MB, less than 75.59% of Python3 online submissions for Largest Rectangle in Histogram.
"""
from typing import List


# class Solution:
#     def largestRectangleArea(self, heights: List[int]) -> int:
#         max_area = 0
#         n = len(heights)
#         if n == 0:
#             return 0
#         i = 0
#         minh = heights[0]
#         for j in range(1, n):
#             minh = min(minh, heights[j])
#
#         return max_area

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st, result = [], 0
        for i, h in enumerate(heights + [0]):
            while st and heights[st[-1]] >= h:
                H = heights[st.pop()]
                W = i if not st else i-st[-1]-1
                result = max(result, H*W)
            st.append(i)
        return result


tests = [
    ([2,1,5,6,2,3], 10)
]

for test in tests:
    result = Solution().largestRectangleArea(test[0])
    if result == test[1]:
        print("PASS")
    else:
        print("FAIL")