"""
https://leetcode.com/problems/valid-palindrome/

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false


Constraints:

s consists only of printable ASCII characters.
"""

"""
Runtime: 60 ms, faster than 42.03% of Python3 online submissions for Valid Palindrome.
Memory Usage: 14.3 MB, less than 62.73% of Python3 online submissions for Valid Palindrome.
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:

        def skip(s: str, i, delta, bound: int) -> int:
            while i != bound and not s[i].isalnum():
                i += delta
            return i

        n = len(s)
        l = 0
        r = n-1
        while l < r:
            l = skip(s, l, 1, r)
            r = skip(s, r, -1, l)
            if l >= r:
                return True
            if s[l].upper() != s[r].upper():
                return False
            l += 1
            r -= 1
        return True


print(Solution().isPalindrome("A man, a plan, a canal: Panama"))  # True
print(Solution().isPalindrome("race a car"))  # False
