"""
https://leetcode.com/explore/featured/card/march-leetcoding-challenge-2021/591/week-4-march-22nd-march-28th/3685/
https://leetcode.com/problems/word-subsets/

We are given two arrays A and B of words.  Each word is a string of lowercase letters.

Now, say that word b is a subset of word a if every letter in b occurs in a, including multiplicity.  For example, "wrr" is a subset of "warrior", but is not a subset of "world".

Now say a word a from A is universal if for every b in B, b is a subset of a.

Return a list of all universal words in A.  You can return the words in any order.



Example 1:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","o"]
Output: ["facebook","google","leetcode"]
Example 2:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["l","e"]
Output: ["apple","google","leetcode"]
Example 3:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","oo"]
Output: ["facebook","google"]
Example 4:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["lo","eo"]
Output: ["google","leetcode"]
Example 5:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["ec","oc","ceo"]
Output: ["facebook","leetcode"]


Note:

1 <= A.length, B.length <= 10000
1 <= A[i].length, B[i].length <= 10
A[i] and B[i] consist only of lowercase letters.
All words in A[i] are unique: there isn't i != j with A[i] == A[j].
"""
from collections import Counter
from functools import reduce
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 928 ms, faster than 50.00% of Python3 online submissions for Word Subsets.
# Memory Usage: 20.6 MB, less than 11.17% of Python3 online submissions for Word Subsets.
# Runtime: 856 ms, faster than 59.22% of Python3 online submissions for Word Subsets.
# Memory Usage: 21 MB, less than 9.50% of Python3 online submissions for Word Subsets.
class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        result = []
        Bc = [Counter(b) for b in B]
        letters = reduce(lambda res, l: res.union(l.keys()), Bc, set())
        agg_c = {l: max([bc[l] for bc in Bc]) for l in letters}
        # agg_c = reduce(lambda res, x: (for c in x: (res[c] = max(res[c], x[c]))), Bc)
        for a in A:
            c = Counter(a)
            is_universal = True
            for k in agg_c:
                if c[k] < agg_c[k]:
                    is_universal = False
                    break
            if is_universal:
                result.append(a)

        return result


tests = [
    (["amazon","apple","facebook","google","leetcode"], ["e","o"], ["facebook","google","leetcode"]),
    (["amazon","apple","facebook","google","leetcode"], ["l","e"], ["apple","google","leetcode"]),
    (["amazon","apple","facebook","google","leetcode"], ["e","oo"], ["facebook","google"]),
    (["amazon","apple","facebook","google","leetcode"], ["lo","eo"], ["google","leetcode"]),
    (["amazon","apple","facebook","google","leetcode"], ["ec","oc","ceo"], ["facebook","leetcode"])
]

run_functional_tests(Solution().wordSubsets, tests)