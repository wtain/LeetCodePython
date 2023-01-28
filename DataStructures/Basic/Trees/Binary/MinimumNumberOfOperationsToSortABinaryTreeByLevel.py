"""
https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/

You are given the root of a binary tree with unique values.

In one operation, you can choose any two nodes at the same level and swap their values.

Return the minimum number of operations needed to make the values at each level sorted in a strictly increasing order.

The level of a node is the number of edges along the path between it and the root node.



Example 1:


Input: root = [1,4,3,7,6,8,5,null,null,null,null,9,null,10]
Output: 3
Explanation:
- Swap 4 and 3. The 2nd level becomes [3,4].
- Swap 7 and 5. The 3rd level becomes [5,6,8,7].
- Swap 8 and 7. The 3rd level becomes [5,6,7,8].
We used 3 operations so return 3.
It can be proven that 3 is the minimum number of operations needed.
Example 2:


Input: root = [1,3,2,7,6,5,4]
Output: 3
Explanation:
- Swap 3 and 2. The 2nd level becomes [2,3].
- Swap 7 and 4. The 3rd level becomes [4,6,5,7].
- Swap 6 and 5. The 3rd level becomes [4,5,6,7].
We used 3 operations so return 3.
It can be proven that 3 is the minimum number of operations needed.
Example 3:


Input: root = [1,2,3,4,5,6]
Output: 0
Explanation: Each level is already sorted in increasing order so return 0.


Constraints:

The number of nodes in the tree is in the range [1, 105].
1 <= Node.val <= 105
All the values of the tree are unique.
"""
from typing import Optional, List

from Common.Constants import null
from Common.DataTypes.Leetcode import TreeNode
from Common.ObjectTestingUtils import run_functional_tests
from Common.TreeUtils import build_tree_from_list


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Runtime
# 724 ms
# Beats
# 97.98%
# Memory
# 54.3 MB
# Beats
# 69.74%
# https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/solutions/2809008/level-order-traversal-cyclesort/
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:

        def min_swaps(arr: List[int]) -> int:
            map = {v: i for i, v in enumerate(arr)}
            arr.sort()
            visited = set()
            result = 0
            n = len(arr)
            for i in range(n):
                if i in visited or map[arr[i]] == i:
                    continue
                j, cycle_size = i, 0
                while j not in visited:
                    visited.add(j)
                    j = map[arr[j]]
                    cycle_size += 1
                if cycle_size > 0:
                    result += cycle_size - 1
            return result

        result = 0
        level = [root]
        while level:
            next_level = []
            result += min_swaps([node.val for node in level])
            for node in level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            level = next_level

        return result


tests = [
    [build_tree_from_list([1,4,3,7,6,8,5,null,null,null,null,9,null,10]), 3],
    [build_tree_from_list([1,3,2,7,6,5,4]), 3],
    [build_tree_from_list([1,2,3,4,5,6]), 0],
]

run_functional_tests(Solution().minimumOperations, tests)
