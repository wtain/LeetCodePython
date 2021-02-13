"""
https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

Given an array nums of integers, return how many of them contain an even number of digits.


Example 1:

Input: nums = [12,345,2,6,7896]
Output: 2
Explanation:
12 contains 2 digits (even number of digits).
345 contains 3 digits (odd number of digits).
2 contains 1 digit (odd number of digits).
6 contains 1 digit (odd number of digits).
7896 contains 4 digits (even number of digits).
Therefore only 12 and 7896 contain an even number of digits.
Example 2:

Input: nums = [555,901,482,1771]
Output: 1
Explanation:
Only 1771 contains an even number of digits.


Constraints:

1 <= nums.length <= 500
1 <= nums[i] <= 10^5
"""
from typing import List

# Runtime: 52 ms, faster than 76.57% of Python3 online submissions for Find Numbers with Even Number of Digits.
# Memory Usage: 14.1 MB, less than 91.67% of Python3 online submissions for Find Numbers with Even Number of Digits.
# class Solution:
#     def findNumbers(self, nums: List[int]) -> int:
#         return sum(1 - len(str(x)) % 2 for x in nums)

# Runtime: 68 ms, faster than 15.41% of Python3 online submissions for Find Numbers with Even Number of Digits.
# Memory Usage: 14.2 MB, less than 74.55% of Python3 online submissions for Find Numbers with Even Number of Digits.
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        def countDigits(x: int) -> int:
            n_digits = 0
            while x:
                n_digits += 1
                x //= 10
            return n_digits
        return sum(1 if countDigits(x) % 2 == 0 else 0 for x in nums)


tests = [
    ([12,345,2,6,7896], 2),
    ([555,901,482,1771], 1)
]

for test in tests:
    result = Solution().findNumbers(test[0])
    if result == test[1]:
        print("PASS")
    else:
        print("FAIL - " + str(result))