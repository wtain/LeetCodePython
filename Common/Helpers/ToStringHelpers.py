from Common.DataTypes.Leetcode import ListNode
from Common.DataTypes.LeetcodeMultilevelList import is_multilevel_list, multilevel_list_to_string
from Common.ListUtils import list_to_string
from Common.DataTypes.NestedInteger import NestedInteger, nestedIntegerToString


def to_string(v) -> str:
    if type(v) is ListNode:
        return list_to_string(v)
    elif type(v) is NestedInteger:
        return nestedIntegerToString(v)
    elif is_multilevel_list(v):
        return multilevel_list_to_string(v)
    else:
        return str(v)