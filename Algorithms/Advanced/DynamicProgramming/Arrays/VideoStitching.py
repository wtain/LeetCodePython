"""
https://leetcode.com/problems/video-stitching/

You are given a series of video clips from a sporting event that lasted time seconds. These video clips can be overlapping with each other and have varying lengths.

Each video clip is described by an array clips where clips[i] = [starti, endi] indicates that the ith clip started at starti and ended at endi.

We can cut these clips into segments freely.

For example, a clip [0, 7] can be cut into segments [0, 1] + [1, 3] + [3, 7].
Return the minimum number of clips needed so that we can cut the clips into segments that cover the entire sporting event [0, time]. If the task is impossible, return -1.



Example 1:

Input: clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], time = 10
Output: 3
Explanation: We take the clips [0,2], [8,10], [1,9]; a total of 3 clips.
Then, we can reconstruct the sporting event as follows:
We cut [1,9] into segments [1,2] + [2,8] + [8,9].
Now we have segments [0,2] + [2,8] + [8,10] which cover the sporting event [0, 10].
Example 2:

Input: clips = [[0,1],[1,2]], time = 5
Output: -1
Explanation: We cannot cover [0,5] with only [0,1] and [1,2].
Example 3:

Input: clips = [[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]], time = 9
Output: 3
Explanation: We can take clips [0,4], [4,7], and [6,9].


Constraints:

1 <= clips.length <= 100
0 <= starti <= endi <= 100
1 <= time <= 100
"""
import bisect
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 37 ms
# Beats
# 75.30%
# Memory
# 13.9 MB
# Beats
# 77.74%
class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clip_count = 0
        end = 0
        clips.sort()
        n = len(clips)
        i = 0
        while i < n and end < time:
            new_end = end
            i0 = i
            while i < n and clips[i][0] <= end:
                new_end = max(new_end, clips[i][1])
                i += 1
            if i == i0:
                return -1
            clip_count += 1
            end = new_end
        return clip_count if end >= time else -1


tests = [
    [[[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], 10, 3],
    [[[0,1],[1,2]], 5, -1],
    [[[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]], 9, 3],
    [[[0,2],[4,8]], 5, -1],
]

run_functional_tests(Solution().videoStitching, tests)
