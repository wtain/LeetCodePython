"""
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/
https://leetcode.com/explore/featured/card/april-leetcoding-challenge-2021/595/week-3-april-15th-april-21st/3710/
Given a string s, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them causing the left and the right side of the deleted substring to concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made.

It is guaranteed that the answer is unique.



Example 1:

Input: s = "abcd", k = 2
Output: "abcd"
Explanation: There's nothing to delete.
Example 2:

Input: s = "deeedbbcccbdaa", k = 3
Output: "aa"
Explanation:
First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"
Example 3:

Input: s = "pbbcggttciiippooaais", k = 2
Output: "ps"


Constraints:

1 <= s.length <= 10^5
2 <= k <= 10^4
s only contains lower case English letters.
"""


# Runtime: 92 ms, faster than 38.54% of Python3 online submissions for Remove All Adjacent Duplicates in String II.
# Memory Usage: 15.8 MB, less than 50.98% of Python3 online submissions for Remove All Adjacent Duplicates in String II.
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        st = []
        for c in s:
            if len(st) > 0 and st[-1][0] == c:
                st[-1][1] += 1
                if st[-1][1] == k:
                    st.pop()
            else:
                st.append([c, 1])
        return "".join([c * n for c, n in st])


tests = [
    ("abcd", 2, "abcd"),
    ("deeedbbcccbdaa", 3, "aa"),
    ("pbbcggttciiippooaais", 2, "ps")
]

for test in tests:
    result = Solution().removeDuplicates(test[0], test[1])
    if result == test[2]:
        print("PASS")
    else:
        print("FAIL - " + result)