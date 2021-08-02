"""
https://leetcode.com/explore/featured/card/july-leetcoding-challenge-2021/612/week-5-july-29th-july-31st/3832/
https://leetcode.com/problems/map-sum-pairs/

Implement the MapSum class:

MapSum() Initializes the MapSum object.
void insert(String key, int val) Inserts the key-val pair into the map. If the key already existed, the original key-value pair will be overridden to the new one.
int sum(string prefix) Returns the sum of all the pairs' value whose key starts with the prefix.


Example 1:

Input
["MapSum", "insert", "sum", "insert", "sum"]
[[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]
Output
[null, null, 3, null, 5]

Explanation
MapSum mapSum = new MapSum();
mapSum.insert("apple", 3);
mapSum.sum("ap");           // return 3 (apple = 3)
mapSum.insert("app", 2);
mapSum.sum("ap");           // return 5 (apple + app = 3 + 2 = 5)


Constraints:

1 <= key.length, prefix.length <= 50
key and prefix consist of only lowercase English letters.
1 <= val <= 1000
At most 50 calls will be made to insert and sum.
"""
from collections import defaultdict

from Common.Constants import null
from Common.ObjectTestingUtils import run_object_tests


# Runtime: 24 ms, faster than 97.01% of Python3 online submissions for Map Sum Pairs.
# Memory Usage: 14.4 MB, less than 56.87% of Python3 online submissions for Map Sum Pairs.
# class MapSum:
#
#     class TrieNode:
#
#         def __init__(self):
#             self.children = defaultdict(MapSum.TrieNode)
#             self.value = 0
#
#         def insert(self, key: str, val: int):
#             if len(key) > 0:
#                 self.children[key[0]].insert(key[1:], val)
#             else:
#                 self.value = val
#
#
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.root = MapSum.TrieNode()
#
#     def insert(self, key: str, val: int) -> None:
#         self.root.insert(key, val)
#
#     def sum(self, prefix: str) -> int:
#         node = self.root
#         result = 0
#         for c in prefix:
#             node = node.children[c]
#         q = [node]
#         while q:
#             node = q.pop()
#             result += node.value
#             for c in node.children:
#                 q.append(node.children[c])
#         return result


# Runtime: 32 ms, faster than 70.60% of Python3 online submissions for Map Sum Pairs.
# Memory Usage: 14.3 MB, less than 80.00% of Python3 online submissions for Map Sum Pairs.
# https://leetcode.com/problems/map-sum-pairs/solution/
class MapSum:

    class TrieNode:

        def __init__(self):
            self.children = defaultdict(MapSum.TrieNode)
            self.value = 0

        def insert(self, key: str, val: int):
            self.value += val
            if len(key) > 0:
                self.children[key[0]].insert(key[1:], val)

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = MapSum.TrieNode()
        self.map = defaultdict(int)

    def insert(self, key: str, val: int) -> None:
        delta = val - self.map[key]
        self.map[key] = val
        self.root.insert(key, delta)

    def sum(self, prefix: str) -> int:
        node = self.root
        for c in prefix:
            if c not in node.children:
                return 0
            node = node.children[c]
        return node.value

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)


tests = [
    [
        ["MapSum", "insert", "sum", "insert", "sum"],
        [[], ["apple",3], ["apple"], ["app",2], ["ap"]],
        [null,null,3,null,5]
    ],
    [
        ["MapSum", "insert", "sum", "insert", "sum"],
        [[], ["apple", 3], ["ap"], ["app", 2], ["ap"]],
        [null, null, 3, null, 5]
    ]
]

run_object_tests(tests, cls=MapSum)