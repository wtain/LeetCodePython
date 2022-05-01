"""
https://leetcode.com/problems/fruit-into-baskets/

You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.



Example 1:

Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.
Example 2:

Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2].
If we had started at the first tree, we would only pick from trees [0,1].
Example 3:

Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: We can pick from trees [2,3,2,2].
If we had started at the first tree, we would only pick from trees [1,2].


Constraints:

1 <= fruits.length <= 105
0 <= fruits[i] < fruits.length
"""
from collections import defaultdict
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 1575 ms, faster than 10.97% of Python3 online submissions for Fruit Into Baskets.
# Memory Usage: 20.5 MB, less than 15.83% of Python3 online submissions for Fruit Into Baskets.
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        result = 0
        n = len(fruits)
        i1 = -1
        counts = defaultdict(int)
        for i2 in range(n):
            counts[fruits[i2]] += 1
            while len(counts) > 2:
                i1 += 1
                counts[fruits[i1]] -= 1
                if not counts[fruits[i1]]:
                    del counts[fruits[i1]]
            result = max(result, i2-i1)

        return result


tests = [
    [[1,2,1], 3],
    [[0,1,2,2], 3],
    [[1,2,3,2,2], 4]
]

run_functional_tests(Solution().totalFruit, tests)
