"""
https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/580/week-2-january-8th-january-14th/3599/
https://leetcode.com/problems/create-sorted-array-through-instructions/

Given an integer array instructions, you are asked to create a sorted array from the elements in instructions. You start with an empty container nums. For each element from left to right in instructions, insert it into nums. The cost of each insertion is the minimum of the following:

The number of elements currently in nums that are strictly less than instructions[i].
The number of elements currently in nums that are strictly greater than instructions[i].
For example, if inserting element 3 into nums = [1,2,3,5], the cost of insertion is min(2, 1) (elements 1 and 2 are less than 3, element 5 is greater than 3) and nums will become [1,2,3,3,5].

Return the total cost to insert all elements from instructions into nums. Since the answer may be large, return it modulo 109 + 7



Example 1:

Input: instructions = [1,5,6,2]
Output: 1
Explanation: Begin with nums = [].
Insert 1 with cost min(0, 0) = 0, now nums = [1].
Insert 5 with cost min(1, 0) = 0, now nums = [1,5].
Insert 6 with cost min(2, 0) = 0, now nums = [1,5,6].
Insert 2 with cost min(1, 2) = 1, now nums = [1,2,5,6].
The total cost is 0 + 0 + 0 + 1 = 1.
Example 2:

Input: instructions = [1,2,3,6,5,4]
Output: 3
Explanation: Begin with nums = [].
Insert 1 with cost min(0, 0) = 0, now nums = [1].
Insert 2 with cost min(1, 0) = 0, now nums = [1,2].
Insert 3 with cost min(2, 0) = 0, now nums = [1,2,3].
Insert 6 with cost min(3, 0) = 0, now nums = [1,2,3,6].
Insert 5 with cost min(3, 1) = 1, now nums = [1,2,3,5,6].
Insert 4 with cost min(3, 2) = 2, now nums = [1,2,3,4,5,6].
The total cost is 0 + 0 + 0 + 0 + 1 + 2 = 3.
Example 3:

Input: instructions = [1,3,3,3,2,4,2,1,2]
Output: 4
Explanation: Begin with nums = [].
Insert 1 with cost min(0, 0) = 0, now nums = [1].
Insert 3 with cost min(1, 0) = 0, now nums = [1,3].
Insert 3 with cost min(1, 0) = 0, now nums = [1,3,3].
Insert 3 with cost min(1, 0) = 0, now nums = [1,3,3,3].
Insert 2 with cost min(1, 3) = 1, now nums = [1,2,3,3,3].
Insert 4 with cost min(5, 0) = 0, now nums = [1,2,3,3,3,4].
​​​​​​​Insert 2 with cost min(1, 4) = 1, now nums = [1,2,2,3,3,3,4].
​​​​​​​Insert 1 with cost min(0, 6) = 0, now nums = [1,1,2,2,3,3,3,4].
​​​​​​​Insert 2 with cost min(2, 4) = 2, now nums = [1,1,2,2,2,3,3,3,4].
The total cost is 0 + 0 + 0 + 0 + 1 + 0 + 1 + 0 + 2 = 4.


Constraints:

1 <= instructions.length <= 105
1 <= instructions[i] <= 105
"""
from typing import List



# TLE, 56 of 65
# class Solution:
#
#     class SegmentNode:
#
#         def __init__(self, value, count=1):
#             self.left = value
#             self.right = value
#             self.value = value
#             self.count = count
#             self.left_child = None
#             self.right_child = None
#
#         def inside(self, value) -> bool:
#             return self.left <= value <= self.right
#
#         def is_leaf(self) -> bool:
#             return not self.left_child and not self.right_child
#
#         def insert(self, value):
#             if self.is_leaf():
#                 if self.value == value:
#                     self.count += 1
#                 else:
#                     if self.value < value:
#                         self.left_child = Solution.SegmentNode(self.value, self.count)
#                         self.right_child = Solution.SegmentNode(value)
#                         self.count += 1
#                         self.right = value
#                     else:
#                         self.right_child = Solution.SegmentNode(self.value, self.count)
#                         self.left_child = Solution.SegmentNode(value)
#                         self.count += 1
#                         self.left = value
#             elif self.inside(value):
#                 if self.left_child.inside(value):
#                     self.left_child.insert(value)
#                 else: # self.right_child.inside(value):
#                     self.right_child.insert(value)
#                 self.count += 1
#             else:
#                 if self.left > value:
#                     self.left_child.insert(value)
#                     self.left = value
#                     self.count += 1
#                 else:
#                     self.right_child.insert(value)
#                     self.right = value
#                     self.count += 1
#
#         def count_left(self, value) -> int:
#             if self.is_leaf():
#                 if self.value < value:
#                     return self.count
#                 else:
#                     return 0
#             else:
#                 if self.right < value:
#                     return self.count
#                 if self.left > value:
#                     return 0
#                 return self.left_child.count_left(value) + self.right_child.count_left(value)
#
#         def count_right(self, value) -> int:
#             if self.is_leaf():
#                 if self.value > value:
#                     return self.count
#                 else:
#                     return 0
#             else:
#                 if self.left > value:
#                     return self.count
#                 if self.right < value:
#                     return 0
#                 return self.left_child.count_right(value) + self.right_child.count_right(value)
#
#     def createSortedArray(self, instructions: List[int]) -> int:
#         n = len(instructions)
#         if not n:
#             return 0
#         cost = 0
#         root = self.SegmentNode(instructions[0])
#         for i in range(1, n):
#             vi = instructions[i]
#             left_cost = root.count_left(vi)
#             right_cost = root.count_right(vi)
#             #print("Inserting " + str(vi) + ": " + str(left_cost) + " " + str(right_cost))
#             cost += min(left_cost, right_cost)
#             root.insert(vi)
#         return cost

# TLE
# class Solution:
#
#     class SegmentNode:
#
#         def __init__(self, value, count=1):
#             self.left = value
#             self.right = value
#             self.value = value
#             self.count = count
#             self.left_child = None
#             self.right_child = None
#
#         def inside(self, value) -> bool:
#             return self.left <= value <= self.right
#
#         def is_leaf(self) -> bool:
#             return not self.left_child and not self.right_child
#
#         def insert(self, value):
#             node = self
#             while node:
#                 node.count += 1
#                 if node.is_leaf():
#                     if node.value == value:
#                         pass
#                     else:
#                         if node.value < value:
#                             node.left_child = Solution.SegmentNode(node.value, node.count-1)
#                             node.right_child = Solution.SegmentNode(value)
#                             node.right = value
#                         else:
#                             node.right_child = Solution.SegmentNode(node.value, node.count-1)
#                             node.left_child = Solution.SegmentNode(value)
#                             node.left = value
#                     break
#                 elif node.inside(value):
#                     if node.right_child.inside(value):
#                         node = node.right_child
#                     else:
#                         node = node.left_child
#                 else:
#                     if node.left > value:
#                         node.left = value
#                         node = node.left_child
#                     else:
#                         node.right = value
#                         node = node.right_child
#
#         def count_left(self, value) -> int:
#             node = self
#             result = 0
#             while node:
#                 if node.is_leaf():
#                     if node.value < value:
#                         result += node.count
#                     break
#                 else:
#                     if node.right < value:
#                         result += node.count
#                         break
#                     if node.left > value:
#                         break
#                     if value < node.right_child.left:
#                         node = node.left_child
#                     else:
#                         result += node.left_child.count
#                         node = node.right_child
#             return result
#
#         def count_right(self, value) -> int:
#             node = self
#             result = 0
#             while node:
#                 if node.is_leaf():
#                     if node.value > value:
#                         result += node.count
#                     break
#                 else:
#                     if node.left > value:
#                         result += node.count
#                         break
#                     if node.right < value:
#                         break
#                     if value > node.left_child.right:
#                         node = node.right_child
#                     else:
#                         result += node.right_child.count
#                         node = node.left_child
#             return result
#
#         def get_cost(self, value) -> int:
#             left_cost = self.count_left(value)
#             right_cost = self.count_right(value)
#             # print("Inserting " + str(value) + ": " + str(left_cost) + " " + str(right_cost))
#             return min(left_cost, right_cost)
#
#     def createSortedArray(self, instructions: List[int]) -> int:
#         n = len(instructions)
#         if not n:
#             return 0
#         cost = 0
#         root = self.SegmentNode(instructions[0])
#         MOD = 10**9 + 7
#         done = 1
#         lastp = 0
#         for i in range(1, n):
#             perc = int(100*done/n)
#             if perc != lastp:
#                 print("Done - " + str(perc) + "%")
#                 lastp = perc
#             vi = instructions[i]
#             cost = (cost + root.get_cost(vi)) % MOD
#             root.insert(vi)
#             done += 1
#         return cost


tests = [
    ([1,5,6,2], 1),
    ([1,2,3,6,5,4], 3),
    ([1,3,3,3,2,4,2,1,2], 4)
]

# MLE/TLE
# class Solution:
#
#     def createSortedArray(self, instructions: List[int]) -> int:
#
#         MAXV = 10 ** 5
#         TREE_SIZE = 4000040  # 2*(MAXV + 2)
#         tree = [0] * TREE_SIZE  # 1..MAXV
#
#         def get_mid(a: int, b: int) -> int:
#             return a + (b-a) // 2
#
#         def query(index: int, s: int, e: int, qs: int, qe: int) -> int:
#             if s >= qs and e <= qe:
#                 return tree[index]
#
#             if e < qs or s > qe:
#                 return 0
#
#             mid = get_mid(s, e)
#
#             res_l = query(2*index + 1, s, mid, qs, qe)
#             res_r = query(2 * index + 2, mid+1, e, qs, qe)
#
#             return res_l + res_r
#
#         def update(index: int, s: int, e: int, pos: int):
#             if s == e:
#                 tree[index] += 1
#                 return
#             mid = get_mid(s, e)
#             if pos <= mid:
#                 update(2*index+1, s, mid, pos)
#             else:
#                 update(2*index+2, mid+1, e, pos)
#
#             tree[index] = tree[2*index+1] + tree[2*index+2]
#
#         n = len(instructions)
#         cost = 0
#         MOD = 10**9 + 7
#         for i in range(n):
#             vi = instructions[i]
#
#             less_cnt = query(0, 0, MAXV, 0, vi-1)
#             greater_cnt = query(0, 0, MAXV, vi+1, MAXV)
#
#             update(0, 0, MAXV, vi)
#
#             cost_i = min(less_cnt, greater_cnt)
#
#             cost = (cost + cost_i) % MOD
#         return cost



# Runtime: 6060 ms, faster than 44.15% of Python3 online submissions for Create Sorted Array through Instructions.
# Memory Usage: 29.9 MB, less than 26.32% of Python3 online submissions for Create Sorted Array through Instructions.
#
# from sortedcontainers import SortedList
#
# class Solution:
#     def createSortedArray(self, instructions):
#         sl = SortedList()
#         cost = 0
#         MOD = 10 ** 9 + 7
#         for i, vi in enumerate(instructions):
#             cost1 = sl.bisect_left(vi)
#             cost2 = i - sl.bisect_right(vi)
#             cost_i = min(cost1, cost2)
#             cost = (cost + cost_i) % MOD
#             sl.add(vi)
#         return cost

# Runtime: 8284 ms, faster than 15.50% of Python3 online submissions for Create Sorted Array through Instructions.
# Memory Usage: 28.1 MB, less than 87.43% of Python3 online submissions for Create Sorted Array through Instructions.
class Solution:

    class Fenwick:

        def __init__(self, size):
            self.data = [0] * size
            self.size = size

        def add(self, index: int, value: int):
            while index < self.size:
                self.data[index] += value
                index += index & -index

        def query(self, index: int) -> int:
            result = 0
            while index:
                result += self.data[index]
                index -= index & -index
            return result


    def createSortedArray(self, instructions):
        MAXV = 10**5+1
        fenwick = Solution.Fenwick(MAXV+1)
        cost = 0
        MOD = 10 ** 9 + 7
        for i, vi in enumerate(instructions):
            cost1 = fenwick.query(vi-1)
            cost2 = i - fenwick.query(vi)
            cost_i = min(cost1, cost2)
            cost = (cost + cost_i) % MOD
            fenwick.add(vi, 1)
        return cost


for test in tests:
    result = Solution().createSortedArray(test[0])
    if result == test[1]:
        print("PASS")
    else:
        print("FAIL - " + str(result))