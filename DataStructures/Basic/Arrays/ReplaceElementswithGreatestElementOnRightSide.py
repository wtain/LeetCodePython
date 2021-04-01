"""
https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/
Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.



Example 1:

Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
Explanation:
- index 0 --> the greatest element to the right of index 0 is index 1 (18).
- index 1 --> the greatest element to the right of index 1 is index 4 (6).
- index 2 --> the greatest element to the right of index 2 is index 4 (6).
- index 3 --> the greatest element to the right of index 3 is index 4 (6).
- index 4 --> the greatest element to the right of index 4 is index 5 (1).
- index 5 --> there are no elements to the right of index 5, so we put -1.
Example 2:

Input: arr = [400]
Output: [-1]
Explanation: There are no elements to the right of index 0.


Constraints:

1 <= arr.length <= 104
1 <= arr[i] <= 105
"""
from typing import List


# Runtime: 120 ms, faster than 84.84% of Python3 online submissions for Replace Elements with Greatest Element on Right Side.
# Memory Usage: 15.7 MB, less than 18.93% of Python3 online submissions for Replace Elements with Greatest Element on Right Side.
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        mx = -1
        result = [0] * n
        for i in range(n-1, -1, -1):
            newmx = max(mx, arr[i])
            result[i] = mx
            mx = newmx
        return result


tests = [
    ([17,18,5,4,6,1], [18,6,6,6,1,-1]),
    ([400], [-1])
]

for test in tests:
    result = Solution().replaceElements(test[0])
    if result == test[1]:
        print("PASS")
    else:
        print("FAIL - " + str(result))