"""
https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/
Given the root of a binary tree and an integer distance. A pair of two different leaf nodes of a binary tree is said to be good if the length of the shortest path between them is less than or equal to distance.

Return the number of good leaf node pairs in the tree.



Example 1:


Input: root = [1,2,3,null,4], distance = 3
Output: 1
Explanation: The leaf nodes of the tree are 3 and 4 and the length of the shortest path between them is 3. This is the only good pair.
Example 2:


Input: root = [1,2,3,4,5,6,7], distance = 3
Output: 2
Explanation: The good pairs are [4,5] and [6,7] with shortest path = 2. The pair [4,6] is not good because the length of ther shortest path between them is 4.
Example 3:

Input: root = [7,1,4,6,null,5,3,null,null,null,null,null,2], distance = 3
Output: 1
Explanation: The only good pair is [2,5].
Example 4:

Input: root = [100], distance = 1
Output: 0
Example 5:

Input: root = [1,1,1], distance = 2
Output: 1


Constraints:

The number of nodes in the tree is in the range [1, 2^10].
Each node's value is between [1, 100].
1 <= distance <= 10
"""


# Definition for a binary tree node.
from typing import List

from sortedcontainers import SortedDict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# WRONG
# class Solution:
#     def countPairs(self, root: TreeNode, distance: int) -> int:
#
#         cnt = 0
#         leaves = SortedDict()
#
#         def dfs(root: TreeNode, d: int):
#             nonlocal distance, cnt, leaves
#             if not root:
#                 return
#             if not root.left and not root.right:
#                 d1 = distance - d
#                 for k, v in leaves.items():
#                     if k > d1:
#                         break
#                     cnt += v
#                 # cnt += sum(leaves[:d1+1])
#                 if not leaves.get(d):
#                     leaves[d] = 0
#                 leaves[d] += 1
#             else:
#                 dfs(root.left, d+1)
#                 dfs(root.right, d+1)
#
#         dfs(root, 0)
#
#         return cnt


# Runtime: 536 ms, faster than 10.66% of Python3 online submissions for Number of Good Leaf Nodes Pairs.
# Memory Usage: 16.8 MB, less than 5.48% of Python3 online submissions for Number of Good Leaf Nodes Pairs.
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:

        leaves = []

        def dfs(parent, current: TreeNode):
            nonlocal leaves
            if not current:
                return
            if not current.left and not current.right:
                leaves.append(current)
            current.parent = parent
            dfs(current, current.left)
            dfs(current, current.right)

        dfs(None, root)

        cnt = 0

        def search(leave: TreeNode, d: int, visited: List[TreeNode]):
            if not leave:
                return
            if leave in visited:
                return
            visited.append(leave)
            if d > 0:
                search(leave.left, d-1, visited)
                search(leave.right, d-1, visited)
                search(leave.parent, d-1, visited)
            nonlocal cnt
            if not leave.left and not leave.right:
                # print("target: " + str(leave.val))
                cnt += 1

        for leave in leaves:
            # print("leave: " + str(leave.val))
            visited = []
            search(leave, distance, visited)
            cnt -= 1
            # print("visited: " + str([n.val for n in visited]))

        return cnt // 2


root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.right = TreeNode(4)

root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
root2.left.left = TreeNode(4)
root2.left.right = TreeNode(5)
root2.right.left = TreeNode(6)
root2.right.right = TreeNode(7)


tests = [
    (root1, 3, 1),
    (root2, 3, 2),
]

for test in tests:
    result = Solution().countPairs(test[0], test[1])
    if result == test[2]:
        print("PASS")
    else:
        print("FAIL - " + str(result))