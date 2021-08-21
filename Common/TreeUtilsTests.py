import unittest

from Common.Constants import null
from Common.Leetcode import TreeNode
from Common.TreeUtils import build_tree_from_list, compareTrees


class TreeUtilsTestCase(unittest.TestCase):
    def test_build_tree_from_list(self):
        tree_constructed = build_tree_from_list([1,null,2,3,4,null,null,5,6])
        tree_expected = TreeNode(1,
                 null,
                 TreeNode(2,
                          TreeNode(3),
                          TreeNode(4,
                                   TreeNode(5),
                                   TreeNode(6))))
        self.assertTrue(compareTrees(tree_constructed, tree_expected))


if __name__ == '__main__':
    unittest.main()
