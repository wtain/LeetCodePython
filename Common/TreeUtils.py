from Common.Leetcode import TreeNode


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