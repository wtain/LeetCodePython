"""
https://leetcode.com/problems/magical-string/

A magical string s consists of only '1' and '2' and obeys the following rules:

The string s is magical because concatenating the number of contiguous occurrences of characters '1' and '2' generates the string s itself.
The first few elements of s is s = "1221121221221121122……". If we group the consecutive 1's and 2's in s, it will be "1 22 11 2 1 22 1 22 11 2 11 22 ......" and the occurrences of 1's or 2's in each group are "1 2 2 1 1 2 1 2 2 1 2 2 ......". You can see that the occurrence sequence is s itself.

Given an integer n, return the number of 1's in the first n number in the magical string s.



Example 1:

Input: n = 6
Output: 3
Explanation: The first 6 elements of magical string s is "122112" and it contains three 1's, so return 3.
Example 2:

Input: n = 1
Output: 1


Constraints:

1 <= n <= 105
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 396 ms
# Beats
# 26.5%
# Memory
# 14.6 MB
# Beats
# 78.60%
# https://leetcode.com/problems/magical-string/solutions/96406/c-3ms-beat-95/
class Solution:
    def magicalString(self, n: int) -> int:
        s = [0] * n
        i, j = 0, 0
        c = 1
        group_characters = 1
        num_characters = 0
        result = 0
        while num_characters < n:
            s[i] = c
            if group_characters == 1:
                result += c
            group_characters = 3 - group_characters
            num_characters += c
            i += 1
            if num_characters >= n:
                break
            if s[j] == 2:
                s[i] = c
                if group_characters == 1:
                    result += c
                group_characters = 3 - group_characters
                num_characters += c
                i += 1
            j += 1
            c = 3 - c
        if num_characters > n and group_characters == 2:
            result -= num_characters - n
        return result


tests = [
    [6, 3],
    [1, 1]
]

run_functional_tests(Solution().magicalString, tests)
