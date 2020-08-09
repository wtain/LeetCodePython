"""
https://leetcode.com/problems/construct-the-rectangle/
For a web developer, it is very important to know how to design a web page's size. So, given a specific rectangular web page’s area, your job by now is to design a rectangular web page, whose length L and width W satisfy the following requirements:

1. The area of the rectangular web page you designed must equal to the given target area.

2. The width W should not be larger than the length L, which means L >= W.

3. The difference between length L and width W should be as small as possible.
You need to output the length L and the width W of the web page you designed in sequence.
Example:
Input: 4
Output: [2, 2]
Explanation: The target area is 4, and all the possible ways to construct it are [1,4], [2,2], [4,1].
But according to requirement 2, [1,4] is illegal; according to requirement 3,  [4,1] is not optimal compared to [2,2]. So the length L is 2, and the width W is 2.
Note:
The given area won't exceed 10,000,000 and is a positive integer
The web page's width and length you designed must be positive integers.
"""
from math import sqrt
from typing import List


"""WRONG"""
"""
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        l = area
        w = 1
        s = int(sqrt(area))
        result = [l, w]
        minDiff = l - w
        for i in range(s+1, 2, -1):
            while l % i == 0:
                l //= i
                w *= i
                diff = max(l, w) - min(l, w)
                if minDiff > diff:
                    minDiff = diff
                    result = [max(l, w), min(l, w)]
        return result
"""

"""
Runtime: 32 ms, faster than 82.09% of Python3 online submissions for Construct the Rectangle.
Memory Usage: 13.7 MB, less than 77.61% of Python3 online submissions for Construct the Rectangle.
"""
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        s = int(sqrt(area))
        for i in range(s, 0, -1):
            l = area // i
            if i * l == area:
                return [l, i]
        return None


print(Solution().constructRectangle(9999990))  # [3330,3003]
print(Solution().constructRectangle(12))  # 4, 3
print(Solution().constructRectangle(4))  # 2, 2
print(Solution().constructRectangle(10))  # 5, 2
print(Solution().constructRectangle(9))  # 3 3
print(Solution().constructRectangle(11))  # 11 1
