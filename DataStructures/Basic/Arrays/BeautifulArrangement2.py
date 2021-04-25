"""
https://leetcode.com/explore/featured/card/april-leetcoding-challenge-2021/594/week-2-april-8th-april-14th/3705/
https://leetcode.com/problems/beautiful-arrangement-ii/

Given two integers n and k, you need to construct a list which contains n different positive integers ranging from 1 to n and obeys the following requirement:
Suppose this list is [a1, a2, a3, ... , an], then the list [|a1 - a2|, |a2 - a3|, |a3 - a4|, ... , |an-1 - an|] has exactly k distinct integers.

If there are multiple answers, print any of them.

Example 1:
Input: n = 3, k = 1
Output: [1, 2, 3]
Explanation: The [1, 2, 3] has three different positive integers ranging from 1 to 3, and the [1, 1] has exactly 1 distinct integer: 1.
Example 2:
Input: n = 3, k = 2
Output: [1, 3, 2]
Explanation: The [1, 3, 2] has three different positive integers ranging from 1 to 3, and the [2, 1] has exactly 2 distinct integers: 1 and 2.
Note:
The n and k are in the range 1 <= k < n <= 104.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 48 ms, faster than 60.67% of Python3 online submissions for Beautiful Arrangement II.
# Memory Usage: 15.2 MB, less than 51.33% of Python3 online submissions for Beautiful Arrangement II.
class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        result = list(range(1, n-k))
        for i in range(k+1):
            if i % 2 == 0:
                result.append(n - k + i // 2)
            else:
                result.append(n - i // 2)
        return result


tests = [
    (3, 1, [1, 2, 3]),
    (3, 2, [1, 3, 2]),

    (6, 3, [1, 2, 3, 6, 4, 5])
]

run_functional_tests(Solution().constructArray, tests)