"""
https://leetcode.com/problems/compare-version-numbers/
Given two version numbers, version1 and version2, compare them.

Version numbers consist of one or more revisions joined by a dot '.'. Each revision consists of digits and may contain leading zeros. Every revision contains at least one character. Revisions are 0-indexed from left to right, with the leftmost revision being revision 0, the next revision being revision 1, and so on. For example 2.5.33 and 0.1 are valid version numbers.

To compare version numbers, compare their revisions in left-to-right order. Revisions are compared using their integer value ignoring any leading zeros. This means that revisions 1 and 001 are considered equal. If a version number does not specify a revision at an index, then treat the revision as 0. For example, version 1.0 is less than version 1.1 because their revision 0s are the same, but their revision 1s are 0 and 1 respectively, and 0 < 1.

Return the following:

If version1 < version2, return -1.
If version1 > version2, return 1.
Otherwise, return 0.


Example 1:

Input: version1 = "1.01", version2 = "1.001"
Output: 0
Explanation: Ignoring leading zeroes, both "01" and "001" represent the same integer "1".
Example 2:

Input: version1 = "1.0", version2 = "1.0.0"
Output: 0
Explanation: version1 does not specify revision 2, which means it is treated as "0".
Example 3:

Input: version1 = "0.1", version2 = "1.1"
Output: -1
Explanation: version1's revision 0 is "0", while version2's revision 0 is "1". 0 < 1, so version1 < version2.
Example 4:

Input: version1 = "1.0.1", version2 = "1"
Output: 1
Example 5:

Input: version1 = "7.5.2.4", version2 = "7.5.3"
Output: -1


Constraints:

1 <= version1.length, version2.length <= 500
version1 and version2 only contain digits and '.'.
version1 and version2 are valid version numbers.
All the given revisions in version1 and version2 can be stored in a 32-bit integer.
"""


# Runtime: 28 ms, faster than 82.17% of Python3 online submissions for Compare Version Numbers.
# Memory Usage: 14.3 MB, less than 27.16% of Python3 online submissions for Compare Version Numbers.
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        i1 = 0
        i2 = 0

        n1 = len(version1)
        n2 = len(version2)

        def fetchVersionComponent(version: str, i: int) -> (int, int):
            n = len(version)
            rv = 0
            while i < n and version[i] != '.':
                rv *= 10
                rv += ord(version[i]) - ord('0')
                i += 1
            if i < n and version[i] == '.':
                i += 1
            return rv, i

        while i1 < n1 and i2 < n2:
            v1, i1 = fetchVersionComponent(version1, i1)
            v2, i2 = fetchVersionComponent(version2, i2)
            if v1 > v2:
                return 1
            if v1 < v2:
                return -1

        while i1 < n1:
            v1, i1 = fetchVersionComponent(version1, i1)
            if v1 > 0:
                return 1

        while i2 < n2:
            v2, i2 = fetchVersionComponent(version2, i2)
            if v2 > 0:
                return -1

        return 0


tests = [
    ("1.01", "1.001", 0),
    ("1.0", "1.0.0", 0),
    ("0.1", "1.1", -1),
    ("1.0.1", "1", 1),
    ("7.5.2.4", "7.5.3", -1)
]

for test in tests:
    result = Solution().compareVersion(test[0], test[1])
    if result == test[2]:
        print("PASS")
    else:
        print("FAIL")