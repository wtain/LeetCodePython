"""
https://leetcode.com/problems/decode-string/

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].



Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
Example 4:

Input: s = "abc3[cd]xyz"
Output: "abccdcdcdxyz"


Constraints:

1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 39 ms, faster than 17.02% of Python3 online submissions for Decode Strings.
# Memory Usage: 14.3 MB, less than 20.70% of Python3 online submissions for Decode Strings.
class Solution:
    def decodeString(self, s: str) -> str:
        i, n = 0, len(s)
        result = ""
        st = []
        while i < n:
            if str.isdigit(s[i]):
                v = 0
                while i < n and str.isdigit(s[i]):
                    v = 10*v + int(s[i])
                    i += 1
                i += 1  # swallow [
                st.append((result, v))
                result = ""
            elif s[i] == ']':
                ss, v = st.pop()
                result = ss + result * v
                i += 1
            else:
                result += s[i]
                i += 1

        return result


tests = [
    ["3[a]2[bc]", "aaabcbc"],
    ["3[a2[c]]", "accaccacc"],
    ["2[abc]3[cd]ef", "abcabccdcdcdef"],
    ["abc3[cd]xyz", "abccdcdcdxyz"]
]

run_functional_tests(Solution().decodeString, tests)