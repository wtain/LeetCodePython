"""
https://leetcode.com/explore/featured/card/march-leetcoding-challenge-2021/589/week-2-march-8th-march-14th/3666/
https://leetcode.com/problems/add-one-row-to-tree/

Given the root of a binary tree, then value v and depth d, you need to add a row of nodes with value v at the given depth d. The root node is at depth 1.

The adding rule is: given a positive integer depth d, for each NOT null tree nodes N in depth d-1, create two tree nodes with value v as N's left subtree root and right subtree root. And N's original left subtree should be the left subtree of the new left subtree root, its original right subtree should be the right subtree of the new right subtree root. If depth d is 1 that means there is no depth d-1 at all, then create a tree node with value v as the new root of the whole original tree, and the original tree is the new root's left subtree.

Example 1:
Input:
A binary tree as following:
       4
     /   \
    2     6
   / \   /
  3   1 5

v = 1

d = 2

Output:
       4
      / \
     1   1
    /     \
   2       6
  / \     /
 3   1   5

Example 2:
Input:
A binary tree as following:
      4
     /
    2
   / \
  3   1

v = 1

d = 3

Output:
      4
     /
    2
   / \
  1   1
 /     \
3       1
Note:
The given d is in range [1, maximum depth of the given tree + 1].
The given binary tree has at least one tree node.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Runtime: 52 ms, faster than 82.23% of Python3 online submissions for Add One Row to Tree.
# Memory Usage: 16.2 MB, less than 89.12% of Python3 online submissions for Add One Row to Tree.
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:

        fakeRoot = TreeNode(0)

        current = [[root, fakeRoot, 1]]
        depth = 1
        while depth < d:
            next_level = []
            for n, p, _ in current:
                if n:
                    next_level.append([n.left, n, 1])
                    next_level.append([n.right, n, 2])

            depth += 1
            current = next_level

        for n, p, x in current:
            if p:
                if x == 1:
                    p.left = TreeNode(v, n)
                elif x == 2:
                    p.right = TreeNode(v, None, n)

        return root if d > 1 else fakeRoot.left


tests = [
    (
        TreeNode(1,
                 TreeNode(2,
                          TreeNode(4)),
                 TreeNode(3)),
        5, 4,
        TreeNode(1,
                 TreeNode(2,
                          TreeNode(4,
                                   TreeNode(5),
                                   TreeNode(5))),
                 TreeNode(3))
    ),


    (
        TreeNode(4,
                 TreeNode(2,
                          TreeNode(3),
                          TreeNode(1)),
                 TreeNode(6,
                          TreeNode(5))),
        1, 1,
        TreeNode(1,
                 TreeNode(4,
                          TreeNode(2,
                                   TreeNode(3),
                                   TreeNode(1)),
                          TreeNode(6,
                                   TreeNode(5)))
                 ),
    ),

    (
        TreeNode(4,
                 TreeNode(2,
                          TreeNode(3),
                          TreeNode(1)),
                 TreeNode(6,
                          TreeNode(5))),
        1, 2,
        TreeNode(4,
                 TreeNode(1,
                          TreeNode(2,
                                   TreeNode(3),
                                   TreeNode(1))
                          ),
                 TreeNode(1,
                          None,
                          TreeNode(6,
                                   TreeNode(5))
                          )),
    ),

    (
        TreeNode(4,
                 TreeNode(2,
                          TreeNode(3),
                          TreeNode(1))),
        1, 3,
        TreeNode(4,
                 TreeNode(2,
                          TreeNode(1,
                                   TreeNode(3)),
                          TreeNode(1,
                                   None,
                                   TreeNode(1))))
    )
]


def compareTrees(t1: TreeNode, t2: TreeNode) -> bool:
    if not t1 and not t2:
        return True
    if not t1 or not t2:
        return False
    if t1.val != t2.val:
        return False
    return compareTrees(t1.left, t2.left) and compareTrees(t1.right, t2.right)


def printTree(root: TreeNode):
    def printTreeImpl(root: TreeNode):
        if root is None:
            return
        print(root.val, '(', end='')
        printTreeImpl(root.left)
        printTreeImpl(root.right)
        print(')', end='')
    printTreeImpl(root)
    print()

for test in tests:
    result = Solution().addOneRow(test[0], test[1], test[2])
    if not compareTrees(result, test[3]):
        print("FAIL")
        printTree(result)
    else:
        print("PASS")