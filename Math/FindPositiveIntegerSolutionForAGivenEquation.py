"""
https://leetcode.com/problems/find-positive-integer-solution-for-a-given-equation/
Given a function  f(x, y) and a value z, return all positive integer pairs x and y where f(x,y) == z.

The function is constantly increasing, i.e.:

f(x, y) < f(x + 1, y)
f(x, y) < f(x, y + 1)
The function interface is defined like this:

interface CustomFunction {
public:
  // Returns positive integer f(x, y) for any given positive integer x and y.
  int f(int x, int y);
};
For custom testing purposes you're given an integer function_id and a target z as input, where function_id represent one function from an secret internal list, on the examples you'll know only two functions from the list.

You may return the solutions in any order.



Example 1:

Input: function_id = 1, z = 5
Output: [[1,4],[2,3],[3,2],[4,1]]
Explanation: function_id = 1 means that f(x, y) = x + y
Example 2:

Input: function_id = 2, z = 5
Output: [[1,5],[5,1]]
Explanation: function_id = 2 means that f(x, y) = x * y


Constraints:

1 <= function_id <= 9
1 <= z <= 100
It's guaranteed that the solutions of f(x, y) == z will be on the range 1 <= x, y <= 1000
It's also guaranteed that f(x, y) will fit in 32 bit signed integer if 1 <= x, y <= 1000
"""
from bisect import bisect_left, bisect
from typing import List, Callable

from Common.Helpers.ResultComparators import compareSets

"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):

"""

class CustomFunction:
    def __init__(self, f: Callable[[int, int], int]):
        self.f = f

    def __call__(self, x, y, *args, **kwargs):
        return self.f(x, y)


# class Solution:
#     def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
#         results = []
#         l1 = l2 = 1
#         r1 = r2 = 1000 + 1
#         for l in range(l1, r1+1):
#             for r in range(l2, r2 + 1):
#                 if customfunction.f(l, r) == z:
#                     results.append([l, r])
#
#         return results


# Runtime: 248 ms, faster than 5.53% of Python3 online submissions for Find Positive Integer Solution for a Given Equation.
# Memory Usage: 14.3 MB, less than 63.22% of Python3 online submissions for Find Positive Integer Solution for a Given Equation.
# class Solution:
#     def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
#         results = []
#
#         def find(f, x1: int, x2: int, y1: int, y2: int):
#             nonlocal results, z
#             if x1 >= x2 or y1 >= y2:
#                 return
#             x = x1 + (x2-x1) // 2
#             y = y1 + (y2-y1) // 2
#             fxy = f(x, y)
#             if fxy == z:
#                 results.append([x, y])
#             elif fxy < z:
#                 find(f, x+1, x2, y1, y2)
#                 find(f, x1, x+1, y+1, y2)
#             else:
#                 find(f, x1, x2, y1, y)
#                 find(f, x1, x, y, y2)
#
#         find(customfunction.f, 1, 1001, 1, 1001)
#
#         return results

# Runtime: 16 ms, faster than 100.00% of Python3 online submissions for Find Positive Integer Solution for a Given Equation.
# Memory Usage: 14.4 MB, less than 6.05% of Python3 online submissions for Find Positive Integer Solution for a Given Equation.
class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        results = []

        def findInRow(f, x: int, y1: int, y2: int) -> int:
            nonlocal results, z
            while y1 <= y2:
                y = y1 + (y2-y1) // 2
                fxy = f(x, y)
                if fxy == z:
                    return y
                elif fxy < z:
                    y1 = y+1
                else:
                    y2 = y-1
            return y2


        def find(f, x1: int, x2: int, y1: int, y2: int):
            nonlocal results, z
            if x1 > x2 or y1 > y2:
                return
            x = x1 + (x2-x1) // 2
            i = findInRow(f, x, y1, y2)
            l, r = i, i+1
            if 1 <= i <= 1000 and f(x, i) == z:
                l -= 1
                results.append([x, i])
            find(f, x1, x-1, l + 1, y2)
            find(f, x+1, x2, y1, r-1)

        find(customfunction.f, 1, z, 1, z)

        return results

# class Solution:
#     def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
#         results = []
#
#         def find(f, x1: int, x2: int, y1: int, y2: int):
#             nonlocal results, z
#             if x1 >= x2 or y1 >= y2:
#                 return
#             x = x1 + (x2-x1) // 2
#             y = y1 + (y2-y1) // 2
#             fxy = f(x, y)
#             if fxy == z:
#                 results.append([x, y])
#             elif fxy < z:
#                 find(f, x+1, x2, y1, y2)
#                 find(f, x1, x+1, y+1, y2)
#             else:
#                 find(f, x1, x2, y1, y)
#                 find(f, x1, x, y, y2)
#
#         find(customfunction.f, 1, z+1, 1, z+1)
#
#         return results


tests = [
    (CustomFunction(lambda x, y: x+y), 5, [[1,4],[2,3],[3,2],[4,1]]),
    (CustomFunction(lambda x, y: x*y), 5, [[1,5],[5,1]])
]


for test in tests:
    result = Solution().findSolution(test[0], test[1])
    if compareSets(test, result):
        print("PASS")
    else:
        print("FAIL - " + str(result))