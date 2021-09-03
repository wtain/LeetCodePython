"""
https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/
https://leetcode.com/explore/featured/card/august-leetcoding-challenge-2021/616/week-4-august-22nd-august-28th/3920/

One way to serialize a binary tree is to use preorder traversal. When we encounter a non-null node, we record the node's value. If it is a null node, we record using a sentinel value such as '#'.


For example, the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#", where '#' represents a null node.

Given a string of comma-separated values preorder, return true if it is a correct preorder traversal serialization of a binary tree.

It is guaranteed that each comma-separated value in the string must be either an integer or a character '#' representing null pointer.

You may assume that the input format is always valid.

For example, it could never contain two consecutive commas, such as "1,,3".
Note: You are not allowed to reconstruct the tree.



Example 1:

Input: preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
Output: true
Example 2:

Input: preorder = "1,#"
Output: false
Example 3:

Input: preorder = "9,#,#,1"
Output: false


Constraints:

1 <= preorder.length <= 104
preoder consist of integers in the range [0, 100] and '#' separated by commas ','.
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 32 ms, faster than 82.17% of Python3 online submissions for Verify Preorder Serialization of a Binary Tree.
# Memory Usage: 14.2 MB, less than 65.50% of Python3 online submissions for Verify Preorder Serialization of a Binary Tree.
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:

        if preorder == "#":
            return True

        chs = preorder.split(",")
        st = []
        was_empty = False

        for c in chs:
            if not st:
                if was_empty:
                    return False
                was_empty = True
            if c != "#":
                if st:
                    st[-1][1] += 1
                st.append([int(c), 0])
            else:
                if not st:
                    return False
                st[-1][1] += 1
                while st and st[-1][1] == 2:
                    st.pop()
        return not st

# https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/discuss/1314054/Python-Stack-approach


tests = [
    ["9,3,4,#,#,1,#,#,#,2,#,6,#,#", False],
    ["#", True],

    ["9,3,4,#,#,1,#,#,2,#,6,#,#", True],
    ["1,#", False],
    ["9,#,#,1", False],

    ["1,2,#,#,#", True],
    ["1,#,#", True],
    ["1,#,#,2", False],
]

run_functional_tests(Solution().isValidSerialization, tests)