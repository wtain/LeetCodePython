"""
https://leetcode.com/problems/shuffle-string/

Given a string s and an integer array indices of the same length.

The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

Return the shuffled string.



Example 1:


Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
Output: "leetcode"
Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.
Example 2:

Input: s = "abc", indices = [0,1,2]
Output: "abc"
Explanation: After shuffling, each character remains in its position.
Example 3:

Input: s = "aiohn", indices = [3,1,4,2,0]
Output: "nihao"
Example 4:

Input: s = "aaiougrt", indices = [4,0,2,6,7,3,1,5]
Output: "arigatou"
Example 5:

Input: s = "art", indices = [1,0,2]
Output: "rat"


Constraints:

s.length == indices.length == n
1 <= n <= 100
s contains only lower-case English letters.
0 <= indices[i] < n
All values of indices are unique (i.e. indices is a permutation of the integers from 0 to n - 1).
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 64 ms, faster than 12.45% of Python3 online submissions for Shuffle Strings.
# Memory Usage: 14.4 MB, less than 18.54% of Python3 online submissions for Shuffle Strings.
# class Solution:
#     def restoreString(self, s: str, indices: List[int]) -> str:
#         return "".join(c for i, c in sorted([i, c] for i, c in zip(indices, s)))


# Runtime: 96 ms, faster than 5.05% of Python3 online submissions for Shuffle Strings.
# Memory Usage: 14.1 MB, less than 92.21% of Python3 online submissions for Shuffle Strings.
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = [' '] * len(s)
        for i in indices:
            result[indices[i]] = s[i]
        return "".join(result)


tests = [
    ["codeleet", [4,5,6,7,0,2,1,3], "leetcode"],
    ["abc", [0,1,2], "abc"],
    ["aiohn", [3,1,4,2,0], "nihao"],
    ["aaiougrt", [4,0,2,6,7,3,1,5], "arigatou"],
    ["art", [1,0,2], "rat"]
]

run_functional_tests(Solution().restoreString, tests)