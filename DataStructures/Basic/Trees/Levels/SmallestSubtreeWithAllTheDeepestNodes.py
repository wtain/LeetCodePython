"""
https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/570/week-2-december-8th-december-14th/3563/
https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/
Similar:
https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/

Given the root of a binary tree, the depth of each node is the shortest distance to the root.

Return the smallest subtree such that it contains all the deepest nodes in the original tree.

A node is called the deepest if it has the largest depth possible among any node in the entire tree.

The subtree of a node is tree consisting of that node, plus the set of all descendants of that node.

Note: This question is the same as 1123: https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/



Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4]
Output: [2,7,4]
Explanation: We return the node with value 2, colored in yellow in the diagram.
The nodes coloured in blue are the deepest nodes of the tree.
Notice that nodes 5, 3 and 2 contain the deepest nodes in the tree but node 2 is the smallest subtree among them, so we return it.
Example 2:

Input: root = [1]
Output: [1]
Explanation: The root is the deepest node in the tree.
Example 3:

Input: root = [0,1,3,null,2]
Output: [2]
Explanation: The deepest node in the tree is 2, the valid subtrees are the subtrees of nodes 2, 1 and 0 but the subtree of node 2 is the smallest.


Constraints:

The number of nodes in the tree will be in the range [1, 500].
0 <= Node.val <= 500
The values of the nodes in the tree are unique.

Runtime: 60 ms, faster than 5.45% of Python3 online submissions for Smallest Subtree with all the Deepest Nodes.
Memory Usage: 14.6 MB, less than 8.28% of Python3 online submissions for Smallest Subtree with all the Deepest Nodes.

"""
from Common.DataTypes.Leetcode import TreeNode
from Common.ObjectTestingUtils import run_functional_tests


class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def dfs(root: TreeNode) -> (TreeNode, int):
            if root is None:
                return root, 0
            L = dfs(root.left)
            R = dfs(root.right)
            if L[1] > R[1]:
                return L[0], L[1] + 1
            if R[1] > L[1]:
                return R[0], R[1] + 1
            return root, L[1] + 1
        return dfs(root)[0]


root = TreeNode(3)
root.left = TreeNode(5)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
root.right = TreeNode(1)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)

tests = [
    (
        root,
        TreeNode(2,
                 TreeNode(7),
                 TreeNode(4))
    )
]

run_functional_tests(Solution().subtreeWithAllDeepest, tests)
