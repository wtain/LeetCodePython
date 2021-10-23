"""
https://leetcode.com/problems/first-unique-character-in-a-string/
Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode"
return 2.


Note: You may assume the string contains only lowercase English letters.
"""


"""
Runtime: 136 ms, faster than 50.84% of Python3 online submissions for First Unique Character in a Strings.
Memory Usage: 14 MB, less than 34.37% of Python3 online submissions for First Unique Character in a Strings.
"""
class Solution:
    def firstUniqChar(self, s: str) -> int:
        unique = {}
        seen = set()
        for i in range(len(s)):
            if s[i] not in seen:
                unique[s[i]] = i
                seen.add(s[i])
            else:
                if unique.get(s[i]) is not None:
                    del unique[s[i]]
        firstI = -1
        for c in unique:
            if firstI == -1 or firstI > unique[c]:
                firstI = unique[c]
        return firstI


print(Solution().firstUniqChar("leetcode"))  # 0
print(Solution().firstUniqChar("loveleetcode"))  # 2
print(Solution().firstUniqChar("eee"))  # -1
print(Solution().firstUniqChar("eeed"))  # 3
