"""
https://leetcode.com/problems/binary-search-tree-iterator/
https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/570/week-2-december-8th-december-14th/3560/
Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):

BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
int next() Moves the pointer to the right, then returns the number at the pointer.
Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.

You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order traversal when next() is called.



Example 1:


Input
["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
Output
[null, 3, 7, true, 9, true, 15, true, 20, false]

Explanation
BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
bSTIterator.next();    // return 3
bSTIterator.next();    // return 7
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 9
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 15
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 20
bSTIterator.hasNext(); // return False


Constraints:

The number of nodes in the tree is in the range [1, 105].
0 <= Node.val <= 106
At most 105 calls will be made to hasNext, and next.


Follow up:

Could you implement next() and hasNext() to run in average O(1) time and use O(h) memory, where h is the height of the tree?

Runtime: 80 ms, faster than 30.11% of Python3 online submissions for Binary Search Tree Iterator.
Memory Usage: 20.8 MB, less than 61.18% of Python3 online submissions for Binary Search Tree Iterator.
"""


# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:

    def move_first(self):
        if not self.current:
            return
        while self.current.left:
            self.parents.append(self.current)
            self.current = self.current.left

    def move_right_parent(self):
        while len(self.parents) > 0:
            parent = self.parents.pop()
            current = self.current
            self.current = parent
            if current is parent.left:
                return
        self.current = None

    def move_right(self):
        self.parents.append(self.current)
        self.current = self.current.right

    def move_next(self):
        if self.current.right:
            self.move_right()
            self.move_first()
        else:
            self.move_right_parent()

    def __init__(self, root: TreeNode):
        self.parents: List[TreeNode] = []
        self.current = root
        self.move_first()

    def next(self) -> int:
        value = self.current.val
        self.move_next()
        return value

    def hasNext(self) -> bool:
        return self.current is not None

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

root = TreeNode(5)
root.left = TreeNode(3)
root.left.right = TreeNode(4)
root.left.left = TreeNode(2)
root.right = TreeNode(7)
root.right.left = TreeNode(6)

it = BSTIterator(root)

while it.hasNext():
    print(it.next())
