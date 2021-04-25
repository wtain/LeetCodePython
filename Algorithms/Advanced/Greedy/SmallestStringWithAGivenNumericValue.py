"""
https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/
https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/582/week-4-january-22nd-january-28th/3619/
The numeric value of a lowercase character is defined as its position (1-indexed) in the alphabet, so the numeric value of a is 1, the numeric value of b is 2, the numeric value of c is 3, and so on.

The numeric value of a string consisting of lowercase characters is defined as the sum of its characters' numeric values. For example, the numeric value of the string "abe" is equal to 1 + 2 + 5 = 8.

You are given two integers n and k. Return the lexicographically smallest string with length equal to n and numeric value equal to k.

Note that a string x is lexicographically smaller than string y if x comes before y in dictionary order, that is, either x is a prefix of y, or if i is the first position such that x[i] != y[i], then x[i] comes before y[i] in alphabetic order.



Example 1:

Input: n = 3, k = 27
Output: "aay"
Explanation: The numeric value of the string is 1 + 1 + 25 = 27, and it is the smallest string with such a value and length equal to 3.
Example 2:

Input: n = 5, k = 73
Output: "aaszz"


Constraints:

1 <= n <= 105
n <= k <= 26 * n
"""


# Runtime: 8980 ms, faster than 5.02% of Python3 online submissions for Smallest Strings With A Given Numeric Value.
# Memory Usage: 15.6 MB, less than 55.02% of Python3 online submissions for Smallest Strings With A Given Numeric Value.
# TLE??
# class Solution:
#     def getSmallestString(self, n: int, k: int) -> str:
#         value = n
#         result = "a" * n
#         pos = n-1
#         while value < k:
#             diff = k - value
#             if diff > 26-1:
#                 diff = 26-1
#             result = result[:pos] + chr(ord('a') + diff) + result[pos+1:]
#             pos -= 1
#             value += diff
#         return result

# Runtime: 40 ms, faster than 87.17% of Python3 online submissions for Smallest Strings With A Given Numeric Value.
# Memory Usage: 15.4 MB, less than 75.28% of Python3 online submissions for Smallest Strings With A Given Numeric Value.
class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        value = n
        diff = k - value
        numZ = diff // 25
        numA = n - numZ
        value += 25 * numZ
        result = 'z' * numZ
        if value < k:
            diff = k - value
            result += "" + chr(ord('a') + diff)
            numA -= 1
        result += "a" * numA
        return result[::-1]



tests = [
    # (98611, 2561647, )

    (3, 27, "aay"),
    (5, 73, "aaszz"),
]

for test in tests:
    result = Solution().getSmallestString(test[0], test[1])
    if result == test[2]:
        print("PASS")
    else:
        print("FAIL - " + result)