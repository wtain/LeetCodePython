"""
https://leetcode.com/problems/groups-of-special-equivalent-strings/
You are given an array A of strings.

A move onto S consists of swapping any two even indexed characters of S, or any two odd indexed characters of S.

Two strings S and T are special-equivalent if after any number of moves onto S, S == T.

For example, S = "zzxy" and T = "xyzz" are special-equivalent because we may make the moves "zzxy" -> "xzzy" -> "xyzz" that swap S[0] and S[2], then S[1] and S[3].

Now, a group of special-equivalent strings from A is a non-empty subset of A such that:

Every pair of strings in the group are special equivalent, and;
The group is the largest size possible (ie., there isn't a string S not in the group such that S is special equivalent to every string in the group)
Return the number of groups of special-equivalent strings from A.


Example 1:

Input: ["abcd","cdab","cbad","xyzz","zzxy","zzyx"]
Output: 3
Explanation:
One group is ["abcd", "cdab", "cbad"], since they are all pairwise special equivalent, and none of the other strings are all pairwise special equivalent to these.

The other two groups are ["xyzz", "zzxy"] and ["zzyx"].  Note that in particular, "zzxy" is not special equivalent to "zzyx".
Example 2:

Input: ["abc","acb","bac","bca","cab","cba"]
Output: 3


Note:

1 <= A.length <= 1000
1 <= A[i].length <= 20
All A[i] have the same length.
All A[i] consist of only lowercase letters.

Runtime: 56 ms, faster than 31.12% of Python3 online submissions for Groups of Special-Equivalent Strings.
Memory Usage: 14.3 MB, less than 90.96% of Python3 online submissions for Groups of Special-Equivalent Strings.
"""
from typing import List


class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        def canonize(s: str) -> str:
            s1 = s[0::2]
            s2 = s[1::2]
            return "".join(sorted(s1)) + "".join(sorted(s2))
        groups = []
        for s in A:
            group = canonize(s)
            if group not in groups:
                groups.append(group)
        return len(groups)


tests = [
    (["abcd","cdab","cbad","xyzz","zzxy","zzyx"], 3),
    (["abc","acb","bac","bca","cab","cba"], 3)
]

for test in tests:
    result = Solution().numSpecialEquivGroups(test[0])
    expected = test[1]
    if result == expected:
        print("PASS")
    else:
        print("FAIL - expected " + str(expected) + ", got " + str(result))