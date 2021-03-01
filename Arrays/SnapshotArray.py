"""
https://leetcode.com/problems/snapshot-array/

Implement a SnapshotArray that supports the following interface:

SnapshotArray(int length) initializes an array-like data structure with the given length.  Initially, each element equals 0.
void set(index, val) sets the element at the given index to be equal to val.
int snap() takes a snapshot of the array and returns the snap_id: the total number of times we called snap() minus 1.
int get(index, snap_id) returns the value at the given index, at the time we took the snapshot with the given snap_id


Example 1:

Input: ["SnapshotArray","set","snap","set","get"]
[[3],[0,5],[],[0,6],[0,0]]
Output: [null,null,0,null,5]
Explanation:
SnapshotArray snapshotArr = new SnapshotArray(3); // set the length to be 3
snapshotArr.set(0,5);  // Set array[0] = 5
snapshotArr.snap();  // Take a snapshot, return snap_id = 0
snapshotArr.set(0,6);
snapshotArr.get(0,0);  // Get the value of array[0] with snap_id = 0, return 5


Constraints:

1 <= length <= 50000
At most 50000 calls will be made to set, snap, and get.
0 <= index < length
0 <= snap_id < (the total number of times we call snap())
0 <= val <= 10^9
"""
import bisect


# TLE
# class SnapshotArray:
#
#     def __init__(self, length: int):
#         self.data = [[0] for _ in range(length)]
#         self.current_snapshot_id = 0
#
#     def set(self, index: int, val: int) -> None:
#         self.data[index][self.current_snapshot_id] = val
#
#     def snap(self) -> int:
#         self.current_snapshot_id += 1
#         for i in range(len(self.data)):
#             val = self.data[i][-1]
#             self.data[i].append(val)
#
#         return self.current_snapshot_id-1
#
#     def get(self, index: int, snap_id: int) -> int:
#         return self.data[index][snap_id]


# Runtime: 524 ms, faster than 32.32% of Python3 online submissions for Snapshot Array.
# Memory Usage: 48.4 MB, less than 20.01% of Python3 online submissions for Snapshot Array.
class SnapshotArray:

    def __init__(self, length: int):
        self.data = [[[0, 0]] for _ in range(length)]
        self.current_snapshot_id = 0

    def set(self, index: int, val: int) -> None:
        if self.data[index][-1][0] != self.current_snapshot_id:
            self.data[index].append([self.current_snapshot_id, val])
        else:
            self.data[index][-1][1] = val

    def snap(self) -> int:
        self.current_snapshot_id += 1
        return self.current_snapshot_id-1

    def get(self, index: int, snap_id: int) -> int:
        idx = bisect.bisect_left(self.data[index], [snap_id, 0])
        if idx < len(self.data[index]) and self.data[index][idx][0] > snap_id:
            idx -= 1
        return self.data[index][idx][1] if idx < len(self.data[index]) else self.data[index][-1][1]

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)

null = None

tests = [
    (
        ["SnapshotArray","set","snap","snap","set","set","get","get","get"],
        [[3],[1,6],[],[],[1,19],[0,4],[2,1],[2,0],[0,1]],
        [null,null,0,1,null,null,0,0,0]
    ),
    (
        ["SnapshotArray","snap","get","get","set","get","set","get","set"],
        [[2],[],[1,0],[0,0],[1,8],[1,0],[0,20],[0,0],[0,7]],
        [null,0,0,0,null,0,null,0,null]
    ),
    (
        ["SnapshotArray","snap","snap","get","set","snap","set"],
        [[4],[],[],[3,1],[2,4],[],[1,4]],
        [null,0,1,0,null,2,null]
    ),
    (
        ["SnapshotArray","set","snap","set","get"],
        [[3],[0,5],[],[0,6],[0,0]],
        [null,null,0,null,5]
    )
]

def call_method(o, name, *args, **kwargs):
    # print("*** Calling " + name + " with " + str(args) + " and " + str(kwargs))
    return getattr(o, name)(*args, **kwargs)


for test in tests:
    methods = test[0]
    arguments = test[1]
    expected = test[2]
    n = len(methods)
    object = SnapshotArray(arguments[0][0])
    fail = False
    for i in range(1, n):
        output = call_method(object, methods[i], *arguments[i])
        if output != expected[i]:
            fail = True
            print("FAIL: " + str(output) + " != " + str(expected[i]))
            break
    if not fail:
        print("PASS")