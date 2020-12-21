"""
https://leetcode.com/problems/decoded-string-at-index/
https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/571/week-3-december-15th-december-21st/3572/
An encoded string S is given.  To find and write the decoded string to a tape, the encoded string is read one character at a time and the following steps are taken:

If the character read is a letter, that letter is written onto the tape.
If the character read is a digit (say d), the entire current tape is repeatedly written d-1 more times in total.
Now for some encoded string S, and an index K, find and return the K-th letter (1 indexed) in the decoded string.



Example 1:

Input: S = "leet2code3", K = 10
Output: "o"
Explanation:
The decoded string is "leetleetcodeleetleetcodeleetleetcode".
The 10th letter in the string is "o".
Example 2:

Input: S = "ha22", K = 5
Output: "h"
Explanation:
The decoded string is "hahahaha".  The 5th letter is "h".
Example 3:

Input: S = "a2345678999999999999999", K = 1
Output: "a"
Explanation:
The decoded string is "a" repeated 8301530446056247680 times.  The 1st letter is "a".


Constraints:

2 <= S.length <= 100
S will only contain lowercase letters and digits 2 through 9.
S starts with a letter.
1 <= K <= 10^9
It's guaranteed that K is less than or equal to the length of the decoded string.
The decoded string is guaranteed to have less than 2^63 letters.

Runtime: 32 ms, faster than 44.35% of Python3 online submissions for Decoded String at Index.
Memory Usage: 14.3 MB, less than 19.76% of Python3 online submissions for Decoded String at Index.
"""


# class Solution:
#     def decodeAtIndex(self, S: str, K: int) -> str:
#         prefix = ""
#         i = 0
#         j = 0
#         for k in range(K):
#             if j == len(prefix):
#                 if S[i].isdigit():
#                     r = int(S[i])
#                     prefix = prefix * r
#                 else:
#                     prefix += S[i]
#                     j += 1
#                 i += 1
#             else:
#                 j += 1
#         if j < len(prefix):
#             return prefix[j]
#         else:
#             return S[i]

# class Solution:
#     def decodeAtIndex(self, S: str, K: int) -> str:
#         K -= 1
#         returns = []  # returns - position, counter value, max
#         i = 0  # index in S
#         j = 0  # number of unpacked chars
#         for c in S:
#             if c.isdigit():
#                 r = int(c)
#                 num_to_skip = j * (r-1)
#                 if K >= num_to_skip:
#                     K -= num_to_skip
#                 else:
#                     returns.append((i, 1, r))  # passed one time
#                     i = 0
#             else:
#                 K -= 1
#                 j += 1
#                 i += 1

class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        size = 0
        for c in S:
            if c.isdigit():
                size *= int(c)
            else:
                size += 1
        n = len(S)
        for i in range(n-1, -1, -1):
            K %= size
            if K == 0 and S[i].isalpha():
                return S[i]
            if S[i].isdigit():
                size = int(size / int(S[i]))
            else:
                size -= 1
        return None


tests = [
    ("leet2code3", 10, "o"),
    ("ha22", 5, "h"),
    ("a2345678999999999999999", 1, "a")
]

for test in tests:
    result = Solution().decodeAtIndex(test[0], test[1])
    if result == test[2]:
        print("PASS")
    else:
        print("FAIL")