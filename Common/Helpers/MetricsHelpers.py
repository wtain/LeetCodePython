from Common.DataTypes.Graph import is_graph_node, graph_size
from Common.DataTypes.Leetcode import TreeNode, ListNode
from Common.DataTypes.LeetcodeMultilevelList import is_multilevel_list, list_size
from Common.ListUtils import list_length_loop_proof
from Common.DataTypes.NAryTree import Node

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


def get_input_mertic(result_instance):
    if type(result_instance) is TreeNode:
        input_metric = lambda test: count_tree_nodes(test[0])
    elif type(result_instance) is Node:
        input_metric = lambda test: count_nary_tree_nodes(test[0])
    elif type(result_instance) is ListNode:
        input_metric = lambda test: list_length_loop_proof(test[0])
    elif type(result_instance) is int:
        input_metric = lambda test: test[0]
    elif is_multilevel_list(result_instance):
        input_metric = lambda test: list_size(test[0])
    elif is_graph_node(result_instance):
        input_metric = lambda test: graph_size(test[0])
    else:
        input_metric = lambda test: len(test[0]) if test[0] else 0
    return input_metric