"""
https://leetcode.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters/

Given a string s containing only lower case English letters and the '?' character, convert all the '?' characters into lower case letters such that the final string does not contain any consecutive repeating characters. You cannot modify the non '?' characters.

It is guaranteed that there are no consecutive repeating characters in the given string except for '?'.

Return the final string after all the conversions (possibly zero) have been made. If there is more than one solution, return any of them. It can be shown that an answer is always possible with the given constraints.



Example 1:

Input: s = "?zs"
Output: "azs"
Explanation: There are 25 solutions for this problem. From "azs" to "yzs", all are valid. Only "z" is an invalid modification as the string will consist of consecutive repeating characters in "zzs".
Example 2:

Input: s = "ubv?w"
Output: "ubvaw"
Explanation: There are 24 solutions for this problem. Only "v" and "w" are invalid modifications as the strings will consist of consecutive repeating characters in "ubvvw" and "ubvww".
Example 3:

Input: s = "j?qg??b"
Output: "jaqgacb"
Example 4:

Input: s = "??yw?ipkj?"
Output: "acywaipkja"


Constraints:

1 <= s.length <= 100
s contains only lower case English letters and '?'.
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 48 ms, faster than 5.21% of Python3 online submissions for Replace All ?'s to Avoid Consecutive Repeating Characters.
# Memory Usage: 14.1 MB, less than 79.14% of Python3 online submissions for Replace All ?'s to Avoid Consecutive Repeating Characters.
class Solution:
    def modifyString(self, s: str) -> str:
        st = []
        n = len(s)
        for i in range(n):
            if s[i] == '?':
                for c in "abc":
                    if st and st[-1] == c:
                        continue
                    if i+1 < n and s[i+1] == c:
                        continue
                    st.append(c)
                    break
            else:
                st.append(s[i])
        return "".join(st)


tests = [
    ["?zs", "azs"],
    ["ubv?w", "ubvaw"],
    ["j?qg??b", "jaqgacb"],
    ["??yw?ipkj?", "acywaipkja"]
]


def custom_check(test, result) -> bool:
    return len(result) == len(test[0]) and not any(a == b for a, b in zip(result, result[1:])) and all(a == b for a, b in zip(test[0], result) if a != '?') and not any(a == '?' for a in result)


run_functional_tests(Solution().modifyString, tests, custom_check=custom_check)