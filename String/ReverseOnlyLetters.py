"""
https://leetcode.com/problems/reverse-only-letters/
Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.



Example 1:

Input: "ab-cd"
Output: "dc-ba"
Example 2:

Input: "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
Example 3:

Input: "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"


Note:

S.length <= 100
33 <= S[i].ASCIIcode <= 122
S doesn't contain \ or "

Runtime: 28 ms, faster than 82.26% of Python3 online submissions for Reverse Only Letters.
Memory Usage: 14.2 MB, less than 28.96% of Python3 online submissions for Reverse Only Letters.
"""


class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        Sl = list(S)
        n = len(S)
        l = 0
        r = n-1
        while l < r:
            while l < r and not Sl[l].isalpha():
                l += 1
            while r > l and not Sl[r].isalpha():
                r -= 1
            if l >= r:
                break
            Sl[l], Sl[r] = Sl[r], Sl[l]
            l += 1
            r -= 1
        return "".join(Sl)


tests = [
    ("ab-cd", "dc-ba"),
    ("a-bC-dEf-ghIj", "j-Ih-gfE-dCba"),
    ("Test1ng-Leet=code-Q!", "Qedo1ct-eeLg=ntse-T!")
]

for test in tests:
    result = Solution().reverseOnlyLetters(test[0])
    expected = test[1]
    if result == expected:
        print("PASS")
    else:
        print("FAIL - expected " + str(expected) + ", got " + str(result))