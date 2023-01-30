"""
https://leetcode.com/problems/longest-uploaded-prefix/description/

You are given a stream of n videos, each represented by a distinct number from 1 to n that you need to "upload" to a server. You need to implement a data structure that calculates the length of the longest uploaded prefix at various points in the upload process.

We consider i to be an uploaded prefix if all videos in the range 1 to i (inclusive) have been uploaded to the server. The longest uploaded prefix is the maximum value of i that satisfies this definition.

Implement the LUPrefix class:

LUPrefix(int n) Initializes the object for a stream of n videos.
void upload(int video) Uploads video to the server.
int longest() Returns the length of the longest uploaded prefix defined above.


Example 1:

Input
["LUPrefix", "upload", "longest", "upload", "longest", "upload", "longest"]
[[4], [3], [], [1], [], [2], []]
Output
[null, null, 0, null, 1, null, 3]

Explanation
LUPrefix server = new LUPrefix(4);   // Initialize a stream of 4 videos.
server.upload(3);                    // Upload video 3.
server.longest();                    // Since video 1 has not been uploaded yet, there is no prefix.
                                     // So, we return 0.
server.upload(1);                    // Upload video 1.
server.longest();                    // The prefix [1] is the longest uploaded prefix, so we return 1.
server.upload(2);                    // Upload video 2.
server.longest();                    // The prefix [1,2,3] is the longest uploaded prefix, so we return 3.


Constraints:

1 <= n <= 105
1 <= video <= n
All values of video are distinct.
At most 2 * 105 calls in total will be made to upload and longest.
At least one call will be made to longest.
"""
from sortedcontainers import SortedSet

from Common.Constants import null
from Common.ObjectTestingUtils import run_object_tests


# Runtime
# 616 ms
# Beats
# 88.98%
# Memory
# 76.1 MB
# Beats
# 19.7%
# https://leetcode.com/problems/longest-uploaded-prefix/solutions/2646696/python-elegant-short-amortized-o-1-commented/
# class LUPrefix:
#
#     def __init__(self, n: int):
#         self.nums = set()
#         self.longest_video = 0
#
#     def upload(self, video: int) -> None:
#         self.nums.add(video)
#         while self.longest_video + 1 in self.nums:
#             self.longest_video += 1
#
#     def longest(self) -> int:
#         return self.longest_video


# TLE
# https://leetcode.com/problems/longest-uploaded-prefix/solutions/2646734/disjoint-set-java/
# class LUPrefix:
#
#     class DisjointSet:
#
#         def __init__(self, n: int):
#             self.parent = [-1] * (n+1)
#             self.count = {}
#
#         def make(self, x: int):
#             self.parent[x] = x
#             self.count[x] = 1
#
#         def find(self, x: int) -> int:
#             while x != self.parent[x]:
#                 x = self.parent[x]
#             return x
#
#         def merge(self, x: int, y: int):
#             if self.parent[y] == -1:
#                 self.make(y)
#             if x <= 0 or x >= len(self.parent) or self.parent[x] == -1:
#                 return
#             px, py = self.find(x), self.find(y)
#             if px != py:
#                 self.parent[px] = py
#                 self.count[py] += self.count[px]
#
#     def __init__(self, n: int):
#         self.d = LUPrefix.DisjointSet(n)
#
#     def upload(self, video: int) -> None:
#         self.d.merge(video-1, video)
#         self.d.merge(video+1, video)
#
#     def longest(self) -> int:
#         return self.d.count[self.d.find(1)] if 1 in self.d.count else 0

# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()


# Runtime
# 1109 ms
# Beats
# 28.82%
# Memory
# 74.4 MB
# Beats
# 38.14%
# https://leetcode.com/problems/longest-uploaded-prefix/solutions/2646506/treeset/
class LUPrefix:

    def __init__(self, n: int):
        self.nums = SortedSet()
        for i in range(1, n+2):
            self.nums.add(i)

    def upload(self, video: int) -> None:
        self.nums.remove(video)

    def longest(self) -> int:
        return self.nums[0]-1 if self.nums else 0


tests = [
    [
        ["LUPrefix", "upload", "longest", "upload", "longest", "upload", "longest"],
        [[4], [3], [], [1], [], [2], []],
        [null, null, 0, null, 1, null, 3]
    ]
]

run_object_tests(tests, cls=LUPrefix)
