"""
https://leetcode.com/problems/friends-of-appropriate-ages/

Some people will make friend requests. The list of their ages is given and ages[i] is the age of the ith person.

Person A will NOT friend request person B (B != A) if any of the following conditions are true:

age[B] <= 0.5 * age[A] + 7
age[B] > age[A]
age[B] > 100 && age[A] < 100
Otherwise, A will friend request B.

Note that if A requests B, B does not necessarily request A.  Also, people will not friend request themselves.

How many total friend requests are made?

Example 1:

Input: [16,16]
Output: 2
Explanation: 2 people friend request each other.
Example 2:

Input: [16,17,18]
Output: 2
Explanation: Friend requests are made 17 -> 16, 18 -> 17.
Example 3:

Input: [20,30,100,110,120]
Output: 3
Explanation: Friend requests are made 110 -> 100, 120 -> 110, 120 -> 100.


Notes:

1 <= ages.length <= 20000.
1 <= ages[i] <= 120.
"""
from bisect import bisect_left
from collections import Counter
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 296 ms, faster than 64.94% of Python3 online submissions for Friends Of Appropriate Ages.
# Memory Usage: 14.9 MB, less than 36.32% of Python3 online submissions for Friends Of Appropriate Ages.
# class Solution:
#     def numFriendRequests(self, ages: List[int]) -> int:
#         cnt = 0
#         c = Counter(ages)
#         ages = sorted(set(ages))
#         n = len(ages)
#         for i in range(n):
#             ci = c[ages[i]]
#             minage = ages[i] // 2 + 7
#             for j in range(n):
#                 if ages[i] < 100 and ages[j] > 100:
#                     # break
#                     continue
#                 if ages[j] <= minage:
#                     continue
#                 if ages[i] < ages[j]:
#                     continue
#                 cnt += ci * c[ages[j]]
#                 if i == j:
#                     cnt -= ci
#             # cnt += ci * (ci - 1)
#
#         return cnt

# Runtime: 264 ms, faster than 84.75% of Python3 online submissions for Friends Of Appropriate Ages.
# Memory Usage: 14.9 MB, less than 36.32% of Python3 online submissions for Friends Of Appropriate Ages.
# class Solution:
#     def numFriendRequests(self, ages: List[int]) -> int:
#         cnt = 0
#         c = Counter(ages)
#         ages = sorted(set(ages))
#         n = len(ages)
#         left = 0
#         for i in range(n):
#             ci = c[ages[i]]
#             if ci > 1 and ages[i] > ages[i] // 2 + 7:
#                 cnt += ci * (ci - 1)
#             if i == 0:
#                 continue
#             minage = ages[i] // 2 + 7
#             for j in range(left, i):
#                 if ages[j] > minage:
#                     cnt += c[ages[j]] * ci
#                 else:
#                     left += 1
#
#         return cnt


# Runtime: 256 ms, faster than 91.19% of Python3 online submissions for Friends Of Appropriate Ages.
# Memory Usage: 14.7 MB, less than 79.72% of Python3 online submissions for Friends Of Appropriate Ages.
# class Solution:
#     def numFriendRequests(self, ages: List[int]) -> int:
#         cnt = 0
#         c = Counter(ages)
#         ages = sorted(set(ages))
#         n = len(ages)
#         left = 0
#         for i in range(n):
#             ci = c[ages[i]]
#             if ci > 1 and ages[i] > ages[i] // 2 + 7:
#                 cnt += ci * (ci - 1)
#             if i == 0:
#                 continue
#             minage = ages[i] // 2 + 7
#             left = bisect_left(ages, minage, left, i)
#             for j in range(left, i):
#                 if ages[j] > minage:
#                     cnt += c[ages[j]] * ci
#
#         return cnt


# Runtime: 256 ms, faster than 91.19% of Python3 online submissions for Friends Of Appropriate Ages.
# Memory Usage: 14.5 MB, less than 96.07% of Python3 online submissions for Friends Of Appropriate Ages.
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        cnt = 0
        c = Counter(ages)
        ages = sorted(set(ages))
        n = len(ages)
        left = 0
        for i in range(n):
            ci = c[ages[i]]
            minage = ages[i] // 2 + 7
            if ci > 1 and ages[i] > minage:
                cnt += ci * (ci - 1)
            if i == 0:
                continue
            left = bisect_left(ages, minage, left, i)
            for j in range(left, i):
                if ages[j] > minage:
                    cnt += c[ages[j]] * ci

        return cnt


tests = [
    ([16,16], 2),
    ([16,17,18], 2),
    ([20,30,100,110,120], 3)
]

run_functional_tests(Solution().numFriendRequests, tests)