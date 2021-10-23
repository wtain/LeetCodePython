"""
https://leetcode.com/problems/assign-cookies/
Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie. Each child i has a greed factor gi, which is the minimum size of a cookie that the child will be content with; and each cookie j has a size sj. If sj >= gi, we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.

Note:
You may assume the greed factor is always positive.
You cannot assign more than one cookie to one child.

Example 1:
Input: [1,2,3], [1,1]

Output: 1

Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3.
And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
You need to output 1.
Example 2:
Input: [1,2], [1,2,3]

Output: 2

Explanation: You have 2 children and 3 cookies. The greed factors of 2 children are 1, 2.
You have 3 cookies and their sizes are big enough to gratify all of the children,
You need to output 2.
"""
from bisect import bisect_left
from typing import List

from Common.ObjectTestingUtils import run_functional_tests

"""WRONG"""
"""
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        cnt = 0
        i = 0
        for si in s:
            i = bisect_left(g, si, i)
            if i < len(g) and g[i] <= si:
                cnt += 1
            i += 1

        return cnt
"""

"""
Runtime: 172 ms, faster than 81.69% of Python3 online submissions for Assign Cookies.
Memory Usage: 15.5 MB, less than 67.42% of Python3 online submissions for Assign Cookies.
"""
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        cnt = 0
        i = 0
        j = 0
        gn = len(g)
        sn = len(s)
        while i < sn and j < gn:
            if s[i] >= g[j]:
                cnt += 1
                i += 1
                j += 1
            else:
                i += 1

        return cnt


tests = [
    [[1,2,3], [1,1], 1],
    [[1,2], [1,2,3], 2],
    [[10,9,8,7], [5,6,7,8], 2]
]

run_functional_tests(Solution().findContentChildren, tests)
