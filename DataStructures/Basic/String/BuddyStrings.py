"""
https://leetcode.com/problems/buddy-strings/

Given two strings A and B of lowercase letters, return true if you can swap two letters in A so the result is equal to B, otherwise, return false.

Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at A[i] and A[j]. For example, swapping at indices 0 and 2 in "abcd" results in "cbad".



Example 1:

Input: A = "ab", B = "ba"
Output: true
Explanation: You can swap A[0] = 'a' and A[1] = 'b' to get "ba", which is equal to B.
Example 2:

Input: A = "ab", B = "ab"
Output: false
Explanation: The only letters you can swap are A[0] = 'a' and A[1] = 'b', which results in "ba" != B.
Example 3:

Input: A = "aa", B = "aa"
Output: true
Explanation: You can swap A[0] = 'a' and A[1] = 'a' to get "aa", which is equal to B.
Example 4:

Input: A = "aaaaaaabc", B = "aaaaaaacb"
Output: true
Example 5:

Input: A = "", B = "aa"
Output: false


Constraints:

0 <= A.length <= 20000
0 <= B.length <= 20000
A and B consist of lowercase letters.

Runtime: 32 ms, faster than 72.14% of Python3 online submissions for Buddy Strings.
Memory Usage: 14.5 MB, less than 24.09% of Python3 online submissions for Buddy Strings.
"""


class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        n = len(A)
        if len(B) != n:
            return False
        pos = -1
        found = False
        for i in range(n):
            if A[i] != B[i]:
                if pos == -1:
                    pos = i
                else:
                    if found:
                        return False
                    if A[pos] != B[i] or A[i] != B[pos]:
                        return False
                    found = True
        if not found and A == B:
            letters = set()
            for c in A:
                if c in letters:
                    return True
                else:
                    letters.add(c)
        return found


tests = [("ab", "ba", True),
         ("ab", "ab", False),
         ("aa", "aa", True),
         ("aaaaaaabc", "aaaaaaacb", True),
         ("ab", "aa", False)]

for test in tests:
    result = Solution().buddyStrings(test[0], test[1])
    if result == test[2]:
        print("PASS")
    else:
        print("FAIL")