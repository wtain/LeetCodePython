"""
https://leetcode.com/problems/kth-distinct-string-in-an-array/

A distinct string is a string that is present only once in an array.

Given an array of strings arr, and an integer k, return the kth distinct string present in arr. If there are fewer than k distinct strings, return an empty string "".

Note that the strings are considered in the order in which they appear in the array.



Example 1:

Input: arr = ["d","b","c","b","c","a"], k = 2
Output: "a"
Explanation:
The only distinct strings in arr are "d" and "a".
"d" appears 1st, so it is the 1st distinct string.
"a" appears 2nd, so it is the 2nd distinct string.
Since k == 2, "a" is returned.
Example 2:

Input: arr = ["aaa","aa","a"], k = 1
Output: "aaa"
Explanation:
All strings in arr are distinct, so the 1st string "aaa" is returned.
Example 3:

Input: arr = ["a","b","a"], k = 3
Output: ""
Explanation:
The only distinct string is "b". Since there are fewer than 3 distinct strings, we return an empty string "".


Constraints:

1 <= k <= arr.length <= 1000
1 <= arr[i].length <= 5
arr[i] consists of lowercase English letters.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 72 ms, faster than 55.36% of Python3 online submissions for Kth Distinct String in an Array.
# Memory Usage: 14.6 MB, less than 28.06% of Python3 online submissions for Kth Distinct String in an Array.
# class Solution:
#     def kthDistinct(self, arr: List[str], k: int) -> str:
#         seen, distinct = set(), dict()
#         for i, s in enumerate(arr):
#             if s in seen:
#                 continue
#             if s in distinct:
#                 del distinct[s]
#                 seen.add(s)
#             else:
#                 distinct[s] = i
#         if len(distinct) < k:
#             return ""
#         return sorted((distinct[s], s) for s in distinct)[k-1][1]


# Runtime: 60 ms, faster than 97.42% of Python3 online submissions for Kth Distinct String in an Array.
# Memory Usage: 14.5 MB, less than 83.23% of Python3 online submissions for Kth Distinct String in an Array.
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        seen, distinct, d_arr = set(), dict(), []
        for i, s in enumerate(arr):
            if s in seen:
                continue
            if s in distinct:
                d_arr[distinct[s]] = ""
                del distinct[s]
                seen.add(s)
            else:
                distinct[s] = len(d_arr)
                d_arr.append(s)
        d_arr = list(filter(lambda s: s, d_arr))
        if len(d_arr) < k:
            return ""
        return d_arr[k-1]


tests = [
    [["d","b","c","b","c","a"], 2, "a"],
    [["aaa","aa","a"], 1, "aaa"],
    [["a","b","a"], 3, ""]
]

run_functional_tests(Solution().kthDistinct, tests)
