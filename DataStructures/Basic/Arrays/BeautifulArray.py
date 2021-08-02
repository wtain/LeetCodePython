"""
https://leetcode.com/explore/featured/card/july-leetcoding-challenge-2021/611/week-4-july-22nd-july-28th/3829/
https://leetcode.com/problems/beautiful-array/

For some fixed n, an array nums is beautiful if it is a permutation of the integers 1, 2, ..., n, such that:

For every i < j, there is no k with i < k < j such that nums[k] * 2 = nums[i] + nums[j].

Given n, return any beautiful array nums.  (It is guaranteed that one exists.)



Example 1:

Input: n = 4
Output: [2,1,4,3]
Example 2:

Input: n = 5
Output: [3,1,2,5,4]


Note:

1 <= n <= 1000
"""
from functools import lru_cache
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 40 ms, faster than 51.43% of Python3 online submissions for Beautiful Array.
# Memory Usage: 14.8 MB, less than 8.57% of Python3 online submissions for Beautiful Array.
# https://leetcode.com/problems/beautiful-array/solution/
class Solution:

    @lru_cache(None)
    def beautifulArray(self, n: int) -> List[int]:
        if n == 1:
            return [1]
        odds = self.beautifulArray((n+1) // 2)
        evens = self.beautifulArray(n // 2)
        return [2*x-1 for x in odds] + [2*x for x in evens]


tests = [
    [4, [2,1,4,3]],
    [5, [3,1,2,5,4]]
]


def is_beautiful(arr: List[int]) -> bool:
    n = len(arr)
    if sum(arr) != n * (n+1) // 2:
        return False
    for i in range(n-2):
        for j in range(i+2, n):
            for k in range(i+1, j):
                if 2*arr[k] == arr[i] + arr[j]:
                    return False
    return True


def customCheck(test, result) -> bool:
    return len(result) == test[0] and is_beautiful(result)


run_functional_tests(Solution().beautifulArray, tests, custom_check=customCheck)