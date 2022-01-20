from unittest import TestCase

from Common.Leetcode import ListNode
from Common.ListUtils import list_length_loop_proof, build_list, build_list_with_loop


class test_list_length_loop_proof(TestCase):
    def test__empty_list(self):
        self.assertEqual(0, list_length_loop_proof(None))

    def test__single_node(self):
        self.assertEqual(1, list_length_loop_proof(ListNode(1)))

    def test__single_node_loop(self):
        l = ListNode(1)
        l.next = l
        self.assertEqual(1, list_length_loop_proof(l))

    def test__three_nodes(self):
        l = build_list([1, 2, 3])
        self.assertEqual(3, list_length_loop_proof(l))

    def test__three_nodes_loop1(self):
        l = build_list_with_loop([1, 2, 3], 0)
        self.assertEqual(3, list_length_loop_proof(l))

    def test__three_nodes_loop2(self):
        l = build_list_with_loop([1, 2, 3], 1)
        self.assertEqual(3, list_length_loop_proof(l))


    def test__three_nodes_loop3(self):
        l = build_list_with_loop([1, 2, 3], 2)
        self.assertEqual(3, list_length_loop_proof(l))
