import copy

from Common.DataTypes.Graph import is_graph_node, graphs_equal
from Common.DataTypes.Leetcode import ListNode, TreeNode
from Common.DataTypes.LeetcodeMultilevelList import is_multilevel_list, multilevel_list_equal
from Common.ListUtils import lists_equal
from Common.QuadTreeUtils import compareQuadTrees
from Common.TreeUtils import compareTrees, compareTreeSets
from Common.DataTypes.QuadTree import Node as QuadTreeNode


def compare_floats(v1, v2, eps=1e-5):
    return abs(v1 - v2) < eps


def compare_bools(v1: bool, v2: bool) -> bool:
    return v1 and v2 or not v1 and not v2  # Deal with None's


def compare_values(v1, v2) -> bool:
    if type(v1) is ListNode:
        return lists_equal(v1, v2)
    elif type(v1) is TreeNode:
        return compareTrees(v1, v2)
    elif type(v1) is QuadTreeNode:
        return compareQuadTrees(v1, v2)
    elif type(v1) is list and v1 and type(v1[0]) is TreeNode:
        return compareTreeSets(v1, v2)
    elif type(v1) is float:
        return compare_floats(v1, v2)
    elif type(v1) is bool or type(v2) is bool:
        return compare_bools(v1, v2)
    elif is_multilevel_list(v1) or is_multilevel_list(v2):
        return multilevel_list_equal(v1, v2)
    elif is_graph_node(v1) or is_multilevel_list(v2):
        return graphs_equal(v1, v2)
    else:
        return v1 == v2


def compare_result_and_expected(custom_check, expected, result, test):
    if custom_check:
        result_copy = copy.deepcopy(result)
        comparison_result = custom_check(test, result_copy)
    else:
        comparison_result = compare_values(result, expected)
    return comparison_result