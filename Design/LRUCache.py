"""
https://leetcode.com/problems/lru-cache/description/

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.



Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4


Constraints:

1 <= capacity <= 3000
0 <= key <= 104
0 <= value <= 105
At most 2 * 105 calls will be made to get and put.
"""
from collections import OrderedDict

from Common.Constants import null
from Common.ObjectTestingUtils import run_object_tests


# WRONG
# class LRUCache:
#
#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.values = []
#         self.index = {}
#
#     def _put(self, key, value):
#         self.values.append((key, value))
#         self.index[key] = len(self.values) - 1
#
#     def get(self, key: int) -> int:
#         print(f"get {key}")
#         if key not in self.index:
#             return -1
#         value = self.values[self.index[key]][1]
#         del self.values[self.index[key]]
#         del self.index[key]
#         self._put(key, value)
#         return value
#
#     def put(self, key: int, value: int) -> None:
#         print(f"put {key} {value}")
#         if key in self.index:
#             del self.values[self.index[key]]
#             del self.index[key]
#         if len(self.values) == self.capacity:
#             key1 = self.values[0][0]
#             del self.values[0]
#             del self.index[key1]
#         self._put(key, value)


# Runtime
# Details
# 714ms
# Beats 86.14%of users with Python3
# Memory
# Details
# 76.62mb
# Beats 98.91%of users with Python3
# https://leetcode.com/problems/lru-cache/solutions/3171305/solution/
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data = OrderedDict()

    def get(self, key: int) -> int:
        return -1 if key not in self.data else self.data.setdefault(key, self.data.pop(key))

    def put(self, key: int, value: int) -> None:
        try:
            self.data.move_to_end(key)
            self.data[key] = value
        except KeyError:
            self.data[key] = value
            if len(self.data) > self.capacity:
                self.data.popitem(last=False)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


tests = [
    [
        ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"],
        [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]],
        [null, null, null, 1, null, -1, null, -1, 3, 4]
    ],
]

run_object_tests(tests, cls=LRUCache)
