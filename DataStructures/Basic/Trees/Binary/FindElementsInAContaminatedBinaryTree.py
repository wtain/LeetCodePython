"""
https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/

Given a binary tree with the following rules:

root.val == 0
If treeNode.val == x and treeNode.left != null, then treeNode.left.val == 2 * x + 1
If treeNode.val == x and treeNode.right != null, then treeNode.right.val == 2 * x + 2
Now the binary tree is contaminated, which means all treeNode.val have been changed to -1.

Implement the FindElements class:

FindElements(TreeNode* root) Initializes the object with a contaminated binary tree and recovers it.
bool find(int target) Returns true if the target value exists in the recovered binary tree.


Example 1:


Input
["FindElements","find","find"]
[[[-1,null,-1]],[1],[2]]
Output
[null,false,true]
Explanation
FindElements findElements = new FindElements([-1,null,-1]);
findElements.find(1); // return False
findElements.find(2); // return True
Example 2:


Input
["FindElements","find","find","find"]
[[[-1,-1,-1,-1,-1]],[1],[3],[5]]
Output
[null,true,true,false]
Explanation
FindElements findElements = new FindElements([-1,-1,-1,-1,-1]);
findElements.find(1); // return True
findElements.find(3); // return True
findElements.find(5); // return False
Example 3:


Input
["FindElements","find","find","find","find"]
[[[-1,null,-1,-1,null,-1]],[2],[3],[4],[5]]
Output
[null,true,false,false,true]
Explanation
FindElements findElements = new FindElements([-1,null,-1,-1,null,-1]);
findElements.find(2); // return True
findElements.find(3); // return False
findElements.find(4); // return False
findElements.find(5); // return True


Constraints:

TreeNode.val == -1
The height of the binary tree is less than or equal to 20
The total number of nodes is between [1, 104]
Total calls of find() is between [1, 104]
0 <= target <= 106
"""
from typing import Optional, List

from Common.Constants import null, false, true
from Common.DataTypes.Leetcode import TreeNode
from Common.ObjectTestingUtils import run_object_tests
from Common.TreeUtils import build_tree_from_list


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Runtime
# 103 ms
# Beats
# 42.71%
# Memory
# 17.9 MB
# Beats
# 76.4%
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.restore()

    def restore(self):
        to_visit = [(self.root, 0)]
        while to_visit:
            node, value = to_visit.pop()
            node.val = value
            if node.left:
                to_visit.append((node.left, 2*value+1))
            if node.right:
                to_visit.append((node.right, 2*value+2))

    def find(self, target: int) -> bool:

        def build_path(value: int) -> List[int]:
            result = []
            while value:
                result.insert(0, value)
                if value % 2:
                    value -= 1
                else:
                    value -= 2
                value //= 2
            return result

        path = build_path(target)

        node = self.root
        for step in path:
            if not node:
                break
            if step % 2:
                node = node.left
            else:
                node = node.right

        if node and node.val == target:
            return True

        return False

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)


tests = [
    [
        ["FindElements","find","find"],
        [[build_tree_from_list([-1,null,-1])],[1],[2]],
        [null,false,true]
    ],
    [
        ["FindElements","find","find","find"],
        [[build_tree_from_list([-1,-1,-1,-1,-1])],[1],[3],[5]],
        [null,true,true,false]
    ],
    [
        ["FindElements","find","find","find","find"],
        [[build_tree_from_list([-1,null,-1,-1,null,-1])],[2],[3],[4],[5]],
        [null,true,false,false,true]
    ]
]

run_object_tests(tests, cls=FindElements)
