"""
https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/
https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/573/week-5-december-29th-december-31st/3585/
Given a binary tree where node values are digits from 1 to 9. A path in the binary tree is said to be pseudo-palindromic if at least one permutation of the node values in the path is a palindrome.

Return the number of pseudo-palindromic paths going from the root node to leaf nodes.



Example 1:



Input: root = [2,3,1,3,1,null,1]
Output: 2
Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the red path [2,3,3], the green path [2,1,1], and the path [2,3,1]. Among these paths only red path and green path are pseudo-palindromic paths since the red path [2,3,3] can be rearranged in [3,2,3] (palindrome) and the green path [2,1,1] can be rearranged in [1,2,1] (palindrome).
Example 2:



Input: root = [2,1,1,1,3,null,null,null,null,null,1]
Output: 1
Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the green path [2,1,1], the path [2,1,3,1], and the path [2,1]. Among these paths only the green path is pseudo-palindromic since [2,1,1] can be rearranged in [1,2,1] (palindrome).
Example 3:

Input: root = [9]
Output: 1


Constraints:

The given binary tree will have between 1 and 10^5 nodes.
Node values are digits from 1 to 9.

Runtime: 376 ms, faster than 82.11% of Python3 online submissions for Pseudo-Palindromic Paths in a Binary Tree.
Memory Usage: 49.8 MB, less than 58.42% of Python3 online submissions for Pseudo-Palindromic Paths in a Binary Tree.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        nodes = []
        result = 0

        def dfs(current: TreeNode):
            nonlocal nodes
            nonlocal result
            if not current:
                return
            if current.val in nodes:
                nodes.remove(current.val)
            else:
                nodes.append(current.val)
            if not current.left and not current.right:
                if len(nodes) <= 1:
                    result += 1
            dfs(current.left)
            dfs(current.right)
            if current.val in nodes:
                nodes.remove(current.val)
            else:
                nodes.append(current.val)

        dfs(root)
        return result


root1 = TreeNode(2)
root1.left = TreeNode(3)
root1.left.left = TreeNode(3)
root1.left.right = TreeNode(1)
root1.right = TreeNode(1)
root1.right.right = TreeNode(1)

if Solution().pseudoPalindromicPaths(root1) == 2:
    print("PASS")
else:
    print("FAIL")

root2 = TreeNode(2)
root2.left = TreeNode(1)
root2.left.left = TreeNode(1)
root2.left.right = TreeNode(3)
root2.left.right.right = TreeNode(1)
root2.right = TreeNode(1)

if Solution().pseudoPalindromicPaths(root2) == 1:
    print("PASS")
else:
    print("FAIL")

root3 = TreeNode(9)

if Solution().pseudoPalindromicPaths(root3) == 1:
    print("PASS")
else:
    print("FAIL")


root4 = TreeNode(9)
root4.left = TreeNode(5)
root4.right = TreeNode(4)

root4.left.left = TreeNode(5)
root4.right.left = TreeNode(2)
root4.right.right = TreeNode(6)

root4.left.left.left = TreeNode(2)
root4.left.left.left.left = TreeNode(2)
root4.left.left.left.left.left = TreeNode(6)
root4.left.left.left.left.right = TreeNode(4)
root4.left.left.left.right = TreeNode(3)
root4.left.left.right = TreeNode(5)
root4.left.left.right.left = TreeNode(1)
root4.left.left.right.right = TreeNode(1)

# root1.left.right = TreeNode(1)


# [9,5,4,5,null,2,6,2,5,null,8,3,9,2,3,1,1,null,4,5,4,2,2,6,4,null,null,1,7,null,5,4,7,null,null,7,null,1,5,6,1,null,null,null,null,9,2,null,9,7,2,1,null,null,null,6,null,null,null,null,null,null,null,null,null,5,null,null,3,null,null,null,8,null,1,null,null,8,null,null,null,null,2,null,8,7]
# if Solution().pseudoPalindromicPaths(root4) == 1:
#     print("PASS")
# else:
#     print("FAIL")