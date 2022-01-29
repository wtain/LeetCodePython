"""
https://leetcode.com/explore/featured/card/april-leetcoding-challenge-2021/594/week-2-april-8th-april-14th/3706/
https://leetcode.com/problems/flatten-nested-list-iterator/
https://leetcode.com/problems/flatten-nested-list-iterator/discuss/1156192/Python-Another-solution-using-deque-explained

You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists. Implement an iterator to flatten it.

Implement the NestedIterator class:

NestedIterator(List<NestedInteger> nestedList) Initializes the iterator with the nested list nestedList.
int next() Returns the next integer in the nested list.
boolean hasNext() Returns true if there are still some integers in the nested list and false otherwise.


Example 1:

Input: nestedList = [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].
Example 2:

Input: nestedList = [1,[4,[6]]]
Output: [1,4,6]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].


Constraints:

1 <= nestedList.length <= 500
The values of the integers in the nested list is in the range [-106, 106].
"""
from collections import deque

from Common.DataTypes.NestedInteger import NestedInteger, ConvertToList, CreateNestedList
from Common.ObjectTestingUtils import run_functional_tests

"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation
"""




# class NestedIterator:
#
#     def fetch(self):
#         self.hasValue = False
#         while self.nestedListStack:
#             while not self.nestedListStack[-1].isInteger():
#                 self.self.nestedListStack.append(self.nestedListStack[-1].getList())
#             self.hasValue = True
#             self.value = self.nestedListStack[-1].getInteger()
#             if not self.nestedListStack[-1].isInteger():
#                 self.nestedListStack[-1].pop()
#
#
#     def __init__(self, nestedList: [NestedInteger]):
#         self.nestedListStack = [nestedList]
#         self.fetch()
#
#     def next(self) -> int:
#         v = self.value
#         self.fetch()
#         return v
#
#     def hasNext(self) -> bool:
#         return self.hasValue


# Runtime: 68 ms, faster than 57.27% of Python3 online submissions for Flatten Nested List Iterator.
# Memory Usage: 17.8 MB, less than 40.61% of Python3 online submissions for Flatten Nested List Iterator.
class NestedIterator:

    def __init__(self, nestedList: [NestedInteger]):
        self.deq = deque(nestedList)

    def fix(self):
        last = self.deq.popleft()
        for e in last.getList()[::-1]:
            self.deq.appendleft(e)

    def next(self) -> int:
        first = self.deq[0]
        if first.isInteger():
            self.deq.popleft()
            return first.getInteger()
        else:
            self.fix()
            return self.next()


    def hasNext(self) -> bool:
        while self.deq and not self.deq[0].isInteger():
            self.fix()
        return self.deq


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

# test1 = CreateNestedList([[1,1],2,[1,1]])
# test2 = CreateNestedList([1,[4,[6]]])

tests = [
    [
        CreateNestedList([[1,1],2,[1,1]]),
        [1,1,2,1,1]
    ],
    [
        CreateNestedList([1,[4,[6]]]),
        [1,4,6]
    ]
]

# it = NestedIterator(test2)

# while it.hasNext():
#     print(it.next())


def CreateNestedIterator(arg):
    return NestedIterator(arg)


def ConvertNestedToFlatList(arg):
    it = CreateNestedIterator(arg)
    return ConvertToList(it)


# for test in tests:
#     it = NestedIterator(test[0])
#     l = ConvertToList(it)
#     if l == test[1]:
#         print("PASS")
#     else:
#         print("FAIL")

    # while it.hasNext():
    #     print(it.next())

run_functional_tests(ConvertNestedToFlatList, tests)