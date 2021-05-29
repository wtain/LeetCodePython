"""
https://leetcode.com/explore/featured/card/may-leetcoding-challenge-2021/601/week-4-may-22nd-may-28th/3756/
https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/

A decimal number is called deci-binary if each of its digits is either 0 or 1 without any leading zeros. For example, 101 and 1100 are deci-binary, while 112 and 3001 are not.

Given a string n that represents a positive decimal integer, return the minimum number of positive deci-binary numbers needed so that they sum up to n.



Example 1:

Input: n = "32"
Output: 3
Explanation: 10 + 11 + 11 = 32
Example 2:

Input: n = "82734"
Output: 8
Example 3:

Input: n = "27346209830709182346"
Output: 9


Constraints:

1 <= n.length <= 105
n consists of only digits.
n does not contain any leading zeros and represents a positive integer.

Think about if the input was only one digit. Then you need to add up as many ones as the value of this digit.
If the input has multiple digits, then you can solve for each digit independently, and merge the answers to form numbers that add up to that input.
Thus the answer is equal to the max digit.
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 196 ms, faster than 32.28% of Python3 online submissions for Partitioning Into Minimum Number Of Deci-Binary Numbers.
# Memory Usage: 16.1 MB, less than 13.90% of Python3 online submissions for Partitioning Into Minimum Number Of Deci-Binary Numbers.
class Solution:
    def minPartitions(self, n: str) -> int:
        return max([int(c) for c in n])


tests = [
    ["32", 3],
    ["82734", 8],
    ["27346209830709182346", 9]
]

run_functional_tests(Solution().minPartitions, tests)