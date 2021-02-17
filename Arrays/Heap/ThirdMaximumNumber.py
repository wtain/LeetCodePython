"""
https://leetcode.com/problems/third-maximum-number/
Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
Example 2:
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Example 3:
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
"""
from heapq import heappush, heappop
from typing import List


"""
Runtime: 56 ms, faster than 68.53% of Python3 online submissions for Third Maximum Number.
Memory Usage: 14.5 MB, less than 81.10% of Python3 online submissions for Third Maximum Number.
"""
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        h = []
        mx = None
        for n in nums:
            if mx is None or mx < n:
                mx = n
            if n not in h:
                heappush(h, n)
                if len(h) > 3:
                    heappop(h)
        if len(h) < 3:
            return mx
        return h[0]


print(Solution().thirdMax([3, 2, 1]))  # 1
print(Solution().thirdMax([1, 2]))  # 2
print(Solution().thirdMax([1, 2, 2]))  # 2
print(Solution().thirdMax([2, 2, 3, 1]))  # 1
