from typing import List

from Common.Constants import null
from Common.Leetcode import TreeNode


def cloneTree(root: TreeNode) -> TreeNode:
    if root:
        newRoot = TreeNode(root.val)
        newRoot.left = cloneTree(root.left)
        newRoot.right = cloneTree(root.right)
        return newRoot
    return None


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
        print(",", end='')
        printTreeImpl(root.right)
        print(')', end='')
    printTreeImpl(root)
    print()


def build_tree_from_list(values: List[int]) -> TreeNode:
    n = len(values)
    if not n:
        return null
    root = TreeNode(values[0])
    level = [root]
    i = 1
    while i < n:
        next_level = []
        for node in level:
            if i >= n:
                break
            if values[i]:
                node.left = TreeNode(values[i])
                next_level.append(node.left)
            i += 1
            if i >= n:
                break
            if values[i]:
                node.right = TreeNode(values[i])
                next_level.append(node.right)
            i += 1
        level = next_level
    return root