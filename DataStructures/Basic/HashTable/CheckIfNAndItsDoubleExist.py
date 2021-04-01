"""
https://leetcode.com/problems/check-if-n-and-its-double-exist/

Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).

More formally check if there exists two indices i and j such that :

i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]


Example 1:

Input: arr = [10,2,5,3]
Output: true
Explanation: N = 10 is the double of M = 5,that is, 10 = 2 * 5.
Example 2:

Input: arr = [7,1,14,11]
Output: true
Explanation: N = 14 is the double of M = 7,that is, 14 = 2 * 7.
Example 3:

Input: arr = [3,1,7,11]
Output: false
Explanation: In this case does not exist N and M, such that N = 2 * M.


Constraints:

2 <= arr.length <= 500
-10^3 <= arr[i] <= 10^3
"""
from typing import List


# Runtime: 60 ms, faster than 37.47% of Python3 online submissions for Check If N and Its Double Exist.
# Memory Usage: 14.3 MB, less than 82.05% of Python3 online submissions for Check If N and Its Double Exist.
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
        for a in arr:
            if 2*a in seen:
                return True
            if a % 2 == 0 and a // 2 in seen:
                return True
            seen.add(a)
        return False


tests = [
    ([10,2,5,3], True),
    ([7,1,14,11], True),
    ([3,1,7,11], False)
]

for test in tests:
    result = Solution().checkIfExist(test[0])
    if result == test[1]:
        print("PASS")
    else:
        print("FAIL - " + str(result))