"""
https://leetcode.com/problems/mini-parser/

Given a string s represents the serialization of a nested list, implement a parser to deserialize it and return the deserialized NestedInteger.

Each element is either an integer or a list whose elements may also be integers or other lists.



Example 1:

Input: s = "324"
Output: 324
Explanation: You should return a NestedInteger object which contains a single integer 324.
Example 2:

Input: s = "[123,[456,[789]]]"
Output: [123,[456,[789]]]
Explanation: Return a NestedInteger object containing a nested list with 2 elements:
1. An integer containing value 123.
2. A nested list containing two elements:
    i.  An integer containing value 456.
    ii. A nested list with one element:
         a. An integer containing value 789


Constraints:

1 <= s.length <= 5 * 104
s consists of digits, square brackets "[]", negative sign '-', and commas ','.
s is the serialization of valid NestedInteger.
"""


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
from Common.DataTypes.NestedInteger import NestedInteger, CreateNestedInteger, compareNestedIntegers
from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 60 ms, faster than 93.18% of Python3 online submissions for Mini Parser.
# Memory Usage: 17.3 MB, less than 94.32% of Python3 online submissions for Mini Parser.
# Runtime: 72 ms, faster than 61.93% of Python3 online submissions for Mini Parser.
# Memory Usage: 17.3 MB, less than 86.93% of Python3 online submissions for Mini Parser.
class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        n = len(s)
        i = 0

        def parse_int():
            nonlocal i
            i0 = i
            while i < n and (str.isdigit(s[i]) or s[i] == '-'):
                i += 1
            return NestedInteger(int(s[i0:i]))

        def parse_list():
            nonlocal i
            v = NestedInteger()
            i += 1  # swallow "["
            while i < n:
                if s[i] == ']':
                    break
                val = parse_value()
                v.add(val)
                if i < n and s[i] != ',':
                    break
                i += 1  # swallow ","
            i += 1  # swallow "]"
            return v

        def parse_value():
            if str.isdigit(s[i]) or s[i] == '-':
                return parse_int()
            if s[i] == '[':
                return parse_list()
            return None

        return parse_value()


tests = [
    [
        "-3",
        NestedInteger(-3)
    ],
    [
        "[123,456,[788,799,833],[[]],10,[]]",
        CreateNestedInteger([123,456,[788,799,833],[[]],10,[]])
    ],
    [
        "324",
        CreateNestedInteger(324)
    ],
    [
        "[123,[456,[789]]]",
        CreateNestedInteger([123, [456, [789]]])
    ]
]


run_functional_tests(Solution().deserialize, tests, custom_check=compareNestedIntegers)