"""
https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/description/?envType=daily-question&envId=2024-01-02

You are given an integer array nums. You need to create a 2D array from nums satisfying the following conditions:

The 2D array should contain only the elements of the array nums.
Each row in the 2D array contains distinct integers.
The number of rows in the 2D array should be minimal.
Return the resulting array. If there are multiple answers, return any of them.

Note that the 2D array can have a different number of elements on each row.



Example 1:

Input: nums = [1,3,4,1,2,3,1]
Output: [[1,3,4,2],[1,3],[1]]
Explanation: We can create a 2D array that contains the following rows:
- 1,3,4,2
- 1,3
- 1
All elements of nums were used, and each row of the 2D array contains distinct integers, so it is a valid answer.
It can be shown that we cannot have less than 3 rows in a valid array.
Example 2:

Input: nums = [1,2,3,4]
Output: [[4,3,2,1]]
Explanation: All elements of the array are distinct, so we can keep all of them in the first row of the 2D array.


Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= nums.length
"""
from collections import Counter
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 119
# ms
# Beats
# 5.01%
# of users with Python3
# Memory
# 17.29
# MB
# Beats
# 20.19%
# of users with Python3
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        cnt = Counter(nums)
        m = max(cnt[x] for x in cnt)
        result = [[] for _ in range(m)]
        for x in cnt:
            for i in range(cnt[x]):
                result[i].append(x)
        return result


def custom_check(test, result) -> bool:
    nums = test[0]
    cnt1 = Counter(nums)
    cnt2 = Counter()
    for row in result:
        cnt2 += Counter(row)
        if len(set(row)) != len(row):
            return False
    return cnt1 == cnt2


tests = [
    [[1,3,4,1,2,3,1], [[1,3,4,2],[1,3],[1]]],
    [[1,2,3,4], [[4,3,2,1]]],
]

run_functional_tests(Solution().findMatrix, tests, custom_check=custom_check)
