"""
https://leetcode.com/problems/find-unique-binary-string/description/?envType=daily-question&envId=2023-11-16

Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. If there are multiple answers, you may return any of them.



Example 1:

Input: nums = ["01","10"]
Output: "11"
Explanation: "11" does not appear in nums. "00" would also be correct.
Example 2:

Input: nums = ["00","01"]
Output: "11"
Explanation: "11" does not appear in nums. "10" would also be correct.
Example 3:

Input: nums = ["111","011","001"]
Output: "101"
Explanation: "101" does not appear in nums. "000", "010", "100", and "110" would also be correct.


Constraints:

n == nums.length
1 <= n <= 16
nums[i].length == n
nums[i] is either '0' or '1'.
All the strings of nums are unique.
"""
import random
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# Details
# 46ms
# Beats 35.15%of users with Python3
# Memory
# Details
# 16.52MB
# Beats 14.04%of users with Python3
# https://leetcode.com/problems/find-unique-binary-string/editorial/?envType=daily-question&envId=2023-11-16
# class Solution:
#     def findDifferentBinaryString(self, nums: List[str]) -> str:
#
#         def generate(curr):
#             if len(curr) == n:
#                 if curr not in nums:
#                     return curr
#                 return ""
#
#             add_zero = generate(curr + "0")
#             if add_zero:
#                 return add_zero
#
#             return generate(curr + "1")
#
#         n = len(nums)
#         nums = set(nums)
#         return generate("")


# Runtime
# Details
# 41ms
# Beats 63.77%of users with Python3
# Memory
# Details
# 16.37MB
# Beats 42.98%of users with Python3
# https://leetcode.com/problems/find-unique-binary-string/editorial/?envType=daily-question&envId=2023-11-16
# class Solution:
#     def findDifferentBinaryString(self, nums: List[str]) -> str:
#         integers = set()
#         for num in nums:
#             integers.add(int(num, 2))
#         n = len(nums)
#         for num in range(n+1):
#             if num not in integers:
#                 result = bin(num)[2:]
#                 return "0" * (n - len(result)) + result
#         return ""


# Runtime
# Details
# 38ms
# Beats 78.89%of users with Python3
# Memory
# Details
# 16.31MB
# Beats 42.98%of users with Python3
# https://leetcode.com/problems/find-unique-binary-string/editorial/?envType=daily-question&envId=2023-11-16
# class Solution:
#     def findDifferentBinaryString(self, nums: List[str]) -> str:
#         integers = set()
#         for num in nums:
#             integers.add(int(num, 2))
#         result = int(nums[0], 2)
#         n = len(nums)
#         while result in integers:
#             result = random.randrange(0, 2 ** n)
#         s = bin(result)[2:]
#         return "0" * (n - len(s)) + s


# Runtime
# Details
# 32ms
# Beats 96.08%of users with Python3
# Memory
# Details
# 16.25MB
# Beats 66.27%of users with Python3
# https://leetcode.com/problems/find-unique-binary-string/editorial/?envType=daily-question&envId=2023-11-16
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        result = []
        for i in range(len(nums)):
            curr = nums[i][i]
            result.append("1" if curr == "0" else "0")
        return "".join(result)


tests = [
    [["01","10"], "11"],
    [["00","01"], "11"],
    [["111","011","001"], "101"],
]


def customCheck(test, result):
    strings = set(test[0])
    n = len(test[0][0])

    def is_binary(result):
        return all(c in ["0", "1"] for c in result)

    return len(result) == n and result not in strings and is_binary(result)


run_functional_tests(Solution().findDifferentBinaryString, tests, custom_check=customCheck)
