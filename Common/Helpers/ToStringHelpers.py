from Common.Leetcode import ListNode
from Common.LeetcodeMultilevelList import is_multilevel_list, multilevel_list_to_string
from Common.ListUtils import list_to_string
from Common.NestedInteger import NestedInteger, nestedIntegerToString


def to_string(v) -> str:
    if type(v) is ListNode:
        return list_to_string(v)
    elif type(v) is NestedInteger:
        return nestedIntegerToString(v)
    elif is_multilevel_list(v):
        return multilevel_list_to_string(v)
    else:
        return str(v)