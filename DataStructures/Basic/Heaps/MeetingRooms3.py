"""
https://leetcode.com/problems/meeting-rooms-iii/description/?envType=daily-question&envId=2024-02-18

You are given an integer n. There are n rooms numbered from 0 to n - 1.

You are given a 2D integer array meetings where meetings[i] = [starti, endi] means that a meeting will be held during the half-closed time interval [starti, endi). All the values of starti are unique.

Meetings are allocated to rooms in the following manner:

Each meeting will take place in the unused room with the lowest number.
If there are no available rooms, the meeting will be delayed until a room becomes free. The delayed meeting should have the same duration as the original meeting.
When a room becomes unused, meetings that have an earlier original start time should be given the room.
Return the number of the room that held the most meetings. If there are multiple rooms, return the room with the lowest number.

A half-closed interval [a, b) is the interval between a and b including a and not including b.



Example 1:

Input: n = 2, meetings = [[0,10],[1,5],[2,7],[3,4]]
Output: 0
Explanation:
- At time 0, both rooms are not being used. The first meeting starts in room 0.
- At time 1, only room 1 is not being used. The second meeting starts in room 1.
- At time 2, both rooms are being used. The third meeting is delayed.
- At time 3, both rooms are being used. The fourth meeting is delayed.
- At time 5, the meeting in room 1 finishes. The third meeting starts in room 1 for the time period [5,10).
- At time 10, the meetings in both rooms finish. The fourth meeting starts in room 0 for the time period [10,11).
Both rooms 0 and 1 held 2 meetings, so we return 0.
Example 2:

Input: n = 3, meetings = [[1,20],[2,10],[3,5],[4,9],[6,8]]
Output: 1
Explanation:
- At time 1, all three rooms are not being used. The first meeting starts in room 0.
- At time 2, rooms 1 and 2 are not being used. The second meeting starts in room 1.
- At time 3, only room 2 is not being used. The third meeting starts in room 2.
- At time 4, all three rooms are being used. The fourth meeting is delayed.
- At time 5, the meeting in room 2 finishes. The fourth meeting starts in room 2 for the time period [5,10).
- At time 6, all three rooms are being used. The fifth meeting is delayed.
- At time 10, the meetings in rooms 1 and 2 finish. The fifth meeting starts in room 1 for the time period [10,12).
Room 0 held 1 meeting while rooms 1 and 2 each held 2 meetings, so we return 1.


Constraints:

1 <= n <= 100
1 <= meetings.length <= 105
meetings[i].length == 2
0 <= starti < endi <= 5 * 105
All the values of starti are unique.
"""
import heapq
from math import inf
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 1760
# ms
# Beats
# 20.81%
# of users with Python3
# Memory
# 62.95
# MB
# Beats
# 53.40%
# of users with Python3
# https://leetcode.com/problems/meeting-rooms-iii/editorial/?envType=daily-question&envId=2024-02-18
# class Solution:
#     def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
#         room_availability_time = [0] * n
#         meeting_count = [0] * n
#         for start, end in sorted(meetings):
#             min_room_availability_time = inf
#             min_availabile_time_room = 0
#             found_unused_room = False
#             for i in range(n):
#                 if room_availability_time[i] <= start:
#                     found_unused_room = True
#                     meeting_count[i] += 1
#                     room_availability_time[i] = end
#                     break
#                 if min_room_availability_time > room_availability_time[i]:
#                     min_room_availability_time = room_availability_time[i]
#                     min_availabile_time_room = i
#             if not found_unused_room:
#                 room_availability_time[min_availabile_time_room] += end - start
#                 meeting_count[min_availabile_time_room] += 1
#         return meeting_count.index(max(meeting_count))


# Runtime
# 1129
# ms
# Beats
# 97.34%
# of users with Python3
# Memory
# 62.48
# MB
# Beats
# 78.07%
# of users with Python3
# https://leetcode.com/problems/meeting-rooms-iii/editorial/?envType=daily-question&envId=2024-02-18
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        unused_rooms, used_rooms = list(range(n)), []
        heapq.heapify(unused_rooms)
        meeting_count = [0] * n
        for start, end in sorted(meetings):
            while used_rooms and used_rooms[0][0] <= start:
                _, room = heapq.heappop(used_rooms)
                heapq.heappush(unused_rooms, room)
            if unused_rooms:
                room = heapq.heappop(unused_rooms)
                heapq.heappush(used_rooms, [end, room])
            else:
                room_availability_time, room = heapq.heappop(used_rooms)
                heapq.heappush(used_rooms, [room_availability_time + end - start, room])
            meeting_count[room] += 1
        return meeting_count.index(max(meeting_count))


tests = [
    [2, [[0,10],[1,5],[2,7],[3,4]], 0],
    [3, [[1,20],[2,10],[3,5],[4,9],[6,8]], 1],
    [4, [[18,19],[3,12],[17,19],[2,13],[7,10]], 0],
]

run_functional_tests(Solution().mostBooked, tests)
