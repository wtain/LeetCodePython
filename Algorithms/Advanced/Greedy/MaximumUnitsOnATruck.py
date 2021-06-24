"""
https://leetcode.com/problems/maximum-units-on-a-truck/
https://leetcode.com/explore/featured/card/june-leetcoding-challenge-2021/604/week-2-june-8th-june-14th/3778/

You are assigned to put some amount of boxes onto one truck. You are given a 2D array boxTypes, where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:

numberOfBoxesi is the number of boxes of type i.
numberOfUnitsPerBoxi is the number of units in each box of the type i.
You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck. You can choose any boxes to put on the truck as long as the number of boxes does not exceed truckSize.

Return the maximum total number of units that can be put on the truck.



Example 1:

Input: boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4
Output: 8
Explanation: There are:
- 1 box of the first type that contains 3 units.
- 2 boxes of the second type that contain 2 units each.
- 3 boxes of the third type that contain 1 unit each.
You can take all the boxes of the first and second types, and one box of the third type.
The total number of units will be = (1 * 3) + (2 * 2) + (1 * 1) = 8.
Example 2:

Input: boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10
Output: 91


Constraints:

1 <= boxTypes.length <= 1000
1 <= numberOfBoxesi, numberOfUnitsPerBoxi <= 1000
1 <= truckSize <= 106
"""
from functools import reduce
from itertools import accumulate
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 156 ms, faster than 58.81% of Python3 online submissions for Maximum Units on a Truck.
# Memory Usage: 14.8 MB, less than 70.89% of Python3 online submissions for Maximum Units on a Truck.
# class Solution:
#     def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
#         result = 0
#         sz = truckSize
#         for _nu, nb in sorted([(-nu, nb) for nb, nu in boxTypes]):
#             nu = -_nu
#             nfit = min(nb, sz)
#             result += nfit * nu
#             sz -= nfit
#         return result


# Runtime: 164 ms, faster than 37.89% of Python3 online submissions for Maximum Units on a Truck.
# Memory Usage: 14.7 MB, less than 89.31% of Python3 online submissions for Maximum Units on a Truck.
# Runtime: 168 ms, faster than 34.56% of Python3 online submissions for Maximum Units on a Truck.
# Memory Usage: 15 MB, less than 12.29% of Python3 online submissions for Maximum Units on a Truck.
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        return reduce(lambda res, box: (res[0] + min(res[1], box[1]) * (-box[0]), res[1] - min(res[1], box[1])), sorted([(-nu, nb) for nb, nu in boxTypes]), (0, truckSize))[0]


tests = [
    [[[1,3],[2,2],[3,1]], 4, 8],
    [[[5,10],[2,5],[4,7],[3,9]], 10, 91]
]

run_functional_tests(Solution().maximumUnits, tests)