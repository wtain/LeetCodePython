"""
https://leetcode.com/problems/lfu-cache/

Design and implement a data structure for a Least Frequently Used (LFU) cache.

Implement the LFUCache class:

LFUCache(int capacity) Initializes the object with the capacity of the data structure.
int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
void put(int key, int value) Update the value of the key if present, or inserts the key if not already present. When the cache reaches its capacity, it should invalidate and remove the least frequently used key before inserting a new item. For this problem, when there is a tie (i.e., two or more keys with the same frequency), the least recently used key would be invalidated.
To determine the least frequently used key, a use counter is maintained for each key in the cache. The key with the smallest use counter is the least frequently used key.

When a key is first inserted into the cache, its use counter is set to 1 (due to the put operation). The use counter for a key in the cache is incremented either a get or put operation is called on it.

The functions get and put must each run in O(1) average time complexity.



Example 1:

Input
["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, 3, null, -1, 3, 4]

Explanation
// cnt(x) = the use counter for key x
// cache=[] will show the last used order for tiebreakers (leftmost element is  most recent)
LFUCache lfu = new LFUCache(2);
lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
lfu.get(1);      // return 1
                 // cache=[1,2], cnt(2)=1, cnt(1)=2
lfu.put(3, 3);   // 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.
                 // cache=[3,1], cnt(3)=1, cnt(1)=2
lfu.get(2);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,1], cnt(3)=2, cnt(1)=2
lfu.put(4, 4);   // Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
                 // cache=[4,3], cnt(4)=1, cnt(3)=2
lfu.get(1);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,4], cnt(4)=1, cnt(3)=3
lfu.get(4);      // return 4
                 // cache=[4,3], cnt(4)=2, cnt(3)=3


Constraints:

0 <= capacity <= 104
0 <= key <= 105
0 <= value <= 109
At most 2 * 105 calls will be made to get and put.
"""
from collections import deque

from sortedcontainers import SortedSet

from Common.Constants import null
from Common.ObjectTestingUtils import run_object_tests
from LFUCache_big_test import test_calls, test_parameters


# NAIVE - TLE
# class LFUCache:
#
#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.use_count = {}
#         self.use_times = {}
#         self.values = {}
#         self.time = 0
#
#     def use_time(self):
#         self.time += 1
#         return self.time
#
#     def get(self, key: int) -> int:
#         if key not in self.use_count:
#             return -1
#         self.use_count[key] += 1
#         self.use_times[key] = self.use_time()
#         return self.values[key]
#
#     def put(self, key: int, value: int) -> None:
#         if self.capacity == 0:
#             return
#         if key not in self.use_count:
#             if len(self.use_count) == self.capacity:
#                 self.invalidate()
#             self.use_count[key] = 0
#         self.use_times[key] = self.use_time()
#         self.values[key] = value
#         self.use_count[key] += 1
#
#     def invalidate(self):
#         if len(self.use_count) == 0:
#             return
#         _, _, key = min((self.use_count[key], self.use_times[key], key) for key in self.values)
#         del self.use_count[key]
#         del self.use_times[key]
#         del self.values[key]


# Runtime
# 862 ms
# Beats
# 79.6%
# Memory
# 77.5 MB
# Beats
# 87%
# https://leetcode.com/problems/lfu-cache/solutions/2815229/lfu-cache/
class LFUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.frequencies = {}
        self.minf = 0
        self.capacity = capacity
        self.t = 0

    def insert(self, key, frequency, value):
        self.cache[key] = (frequency, value)
        if frequency not in self.frequencies:
            self.frequencies[frequency] = deque()
        self.frequencies[frequency].append(key)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        frequency, value = self.cache[key]
        self.frequencies[frequency].remove(key)
        if self.minf == frequency and len(self.frequencies[frequency]) == 0:
            self.minf += 1
        self.insert(key, frequency+1, value)
        return value

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return
        if key in self.cache:
            frequency, _ = self.cache[key]
            self.cache[key] = (frequency, value)
            self.get(key)
            return
        if self.capacity == len(self.cache):
            keyToDelete = self.frequencies[self.minf].popleft()
            del self.cache[keyToDelete]
        self.minf = 1
        self.insert(key, 1, value)


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


tests = [
    [
        ["LFUCache","put","get"],
        [[0],[0,0],[0]],
        [null, null, -1]
    ],
    [
        ["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"],
        [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]],
        [null, null, null, 1, null, -1, 3, null, -1, 3, 4]
    ],
    [
        ["LFUCache","put","put","get","get","put","get","get","get"],
        [[2],[2,1],[3,2],[3],[2],[4,3],[2],[3],[4]],
        [null,null,null,2,1,null,1,-1,3]
    ],
    # [
    #     test_calls,
    #     test_parameters,
    #     [null]
    # ],
]

run_object_tests(tests, cls=LFUCache)
