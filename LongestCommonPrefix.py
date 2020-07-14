"""
https://leetcode.com/problems/longest-common-prefix/
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""
from typing import List

"""
Runtime: 40 ms, faster than 38.56% of Python3 online submissions for Longest Common Prefix.
Memory Usage: 13.9 MB, less than 63.13% of Python3 online submissions for Longest Common Prefix.
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        n = len(strs)
        if 0 == n:
            return result
        m = len(strs[0])
        for i in range(m):
            for j in range(1, n):
                if i >= len(strs[j]) or strs[j][i] != strs[0][i]:
                    return result
            result += strs[0][i]
        return result


print(Solution().longestCommonPrefix([]))  # ""
print(Solution().longestCommonPrefix(["flower","flow","flight"]))  # "fl"
print(Solution().longestCommonPrefix(["dog","racecar","car"]))  # ""