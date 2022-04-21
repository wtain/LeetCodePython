"""
https://leetcode.com/problems/design-hashset/

Design a HashSet without using any built-in hash table libraries.

Implement MyHashSet class:

void add(key) Inserts the value key into the HashSet.
bool contains(key) Returns whether the value key exists in the HashSet or not.
void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.


Example 1:

Input
["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]
Output
[null, null, null, true, false, null, true, null, false]

Explanation
MyHashSet myHashSet = new MyHashSet();
myHashSet.add(1);      // set = [1]
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(1); // return True
myHashSet.contains(3); // return False, (not found)
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(2); // return True
myHashSet.remove(2);   // set = [1]
myHashSet.contains(2); // return False, (already removed)


Constraints:

0 <= key <= 106
At most 104 calls will be made to add, remove, and contains.
"""
from Common.Constants import false, true, null
from Common.ObjectTestingUtils import run_object_tests


# Runtime: 225 ms, faster than 72.58% of Python3 online submissions for Design HashSet.
# Memory Usage: 19.8 MB, less than 35.77% of Python3 online submissions for Design HashSet.
class MyHashSet:

    def __init__(self):
        self.buckets = [[] for _ in range(10000)]

    def add(self, key: int) -> None:
        if self.contains(key):
            return
        self.buckets[key % len(self.buckets)].append(key)

    def remove(self, key: int) -> None:
        if not self.contains(key):
            return
        self.buckets[key % len(self.buckets)].remove(key)

    def contains(self, key: int) -> bool:
        return key in self.buckets[key % len(self.buckets)]

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)


tests = [
    [
        ["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"],
        [[], [1], [2], [1], [3], [2], [2], [2], [2]],
        [null, null, null, true, false, null, true, null, false]
    ],
    [
        ["MyHashSet","add","remove","add","remove","remove","add","add","add","add","remove"],
        [[],[9],[19],[14],[19],[9],[0],[3],[4],[0],[9]],
        [null,null,null,null,null,null,null,null,null,null,null]
    ]
]

run_object_tests(tests, cls=MyHashSet, debug=True)
