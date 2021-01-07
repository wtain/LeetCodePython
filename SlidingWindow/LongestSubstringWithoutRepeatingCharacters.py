"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/
https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/579/week-1-january-1st-january-7th/3595/
Given a string s, find the length of the longest substring without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

Runtime: 160 ms, faster than 20.54% of Python3 online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 14.2 MB, less than 75.40% of Python3 online submissions for Longest Substring Without Repeating Characters.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i1 = 0
        maxLen = 0
        n = len(s)
        h = []
        for i2 in range(n):
            while i2 < n and s[i2] in h:
                h.remove(s[i1])
                i1 += 1
            if i2 >= n:
                break
            currLen = i2 - i1 + 1
            h.append(s[i2])
            maxLen = max(maxLen, currLen)
        return maxLen


tests = [
    ("abcabcbb", 3),
    ("bbbbb", 1),
    ("pwwkew", 3),
    ("", 0)
]

for test in tests:
    result = Solution().lengthOfLongestSubstring(test[0])
    if result == test[1]:
        print("PASS")
    else:
        print("FAIL - " + str(result))