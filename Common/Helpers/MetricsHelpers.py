from Common.Leetcode import TreeNode
from Common.NAryTree import Node

# todo: recursive calc_size, e.g. List of Lists
# def calc_size(obj) -> int:


def count_tree_nodes(root: TreeNode) -> int:
    if not root:
        return 0
    return 1 + count_tree_nodes(root.left) + count_tree_nodes(root.right)


def count_nary_tree_nodes(root: Node) -> int:
    if not root:
        return 0
    result = 1
    if root.children:
        for child in root.children:
            result += count_nary_tree_nodes(child)
    return result