"""
https://leetcode.com/explore/featured/card/may-leetcoding-challenge-2021/598/week-1-may-1st-may-7th/3729/
https://leetcode.com/problems/course-schedule-iii/

There are n different online courses numbered from 1 to n. You are given an array courses where courses[i] = [durationi, lastDayi] indicate that the ith course should be taken continuously for durationi days and must be finished before or on lastDayi.

You will start on the 1st day and you cannot take two or more courses simultaneously.

Return the maximum number of courses that you can take.



Example 1:

Input: courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]
Output: 3
Explanation:
There are totally 4 courses, but you can take 3 courses at most:
First, take the 1st course, it costs 100 days so you will finish it on the 100th day, and ready to take the next course on the 101st day.
Second, take the 3rd course, it costs 1000 days so you will finish it on the 1100th day, and ready to take the next course on the 1101st day.
Third, take the 2nd course, it costs 200 days so you will finish it on the 1300th day.
The 4th course cannot be taken now, since you will finish it on the 3300th day, which exceeds the closed date.
Example 2:

Input: courses = [[1,2]]
Output: 1
Example 3:

Input: courses = [[3,2],[4,3]]
Output: 0


Constraints:

1 <= courses.length <= 104
1 <= durationi, lastDayi <= 104

"""
import heapq
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# TLE/MLE
# class Solution:
#     def scheduleCourse(self, courses: List[List[int]]) -> int:
#         courses.sort(key=lambda x: x[1])
#         n = len(courses)
#
#         @lru_cache(None)
#         def schedule(i: int, time: int) -> int:
#             nonlocal courses, n
#             if i == n:
#                 return 0
#             taken = 0
#             if time + courses[i][0] <= courses[i][1]:
#                 taken = 1 + schedule(i+1, time + courses[i][0])
#             not_taken = schedule(i+1, time)
#             return max(taken, not_taken)
#
#         return schedule(0, 0)


# TLE
# class Solution:
#     def scheduleCourse(self, courses: List[List[int]]) -> int:
#         courses.sort(key=lambda x: x[1])
#         n = len(courses)
#
#         time, count = 0, 0
#
#         for i in range(n):
#             duration, end = courses[i]
#             if time + duration <= end:
#                 time += duration
#                 count += 1
#             else:
#                 maxi = i
#                 for j in range(i):
#                     duration_j, end_j = courses[j]
#                     if duration_j > courses[maxi][0]:
#                         maxi = j
#                 if courses[maxi][0] > duration:
#                     time += duration - courses[maxi][0]
#                 courses[maxi][0] = -1
#         return count


# Runtime: 664 ms, faster than 97.10% of Python3 online submissions for Course Schedule III.
# Memory Usage: 19.4 MB, less than 50.65% of Python3 online submissions for Course Schedule III.
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        n = len(courses)

        time, count = 0, 0

        prev_courses = []

        for i in range(n):
            duration, end = courses[i]
            if time + duration <= end:
                time += duration
                count += 1
                heapq.heappush(prev_courses, -duration)
            else:
                if prev_courses and -prev_courses[0] > duration:
                    prev_duration = -heapq.heappop(prev_courses)
                    time += duration - prev_duration
                    heapq.heappush(prev_courses, -duration)
        return count


tests = [
    [
        [[1,2],[2,3]], 2
    ],
    [
        [[100,200],[200,1300],[1000,1250],[2000,3200]], 3
    ],
    [
        [[1,2]], 1
    ],
    [
        [[3,2],[4,3]], 0
    ]
]

run_functional_tests(Solution().scheduleCourse, tests)