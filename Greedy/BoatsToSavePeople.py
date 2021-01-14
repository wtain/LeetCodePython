"""
https://leetcode.com/problems/boats-to-save-people/
https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/580/week-2-january-8th-january-14th/3602/
"""
from typing import List


# Runtime: 480 ms, faster than 26.78% of Python3 online submissions for Boats to Save People.
# Memory Usage: 21 MB, less than 49.42% of Python3 online submissions for Boats to Save People.
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        i = 0
        j = len(people) - 1
        cnt = 0
        while i <= j:
            weight = people[j]
            j -= 1
            if i <= j and weight + people[i] <= limit:
                i += 1
            cnt += 1
        return cnt


tests = [
    ([5,1,7,4,2,4], 7, 4),

    ([1,2], 3, 1),
    ([3,2,2,1], 3, 3),
    ([3,5,3,4], 5, 4)
]

for test in tests:
    result = Solution().numRescueBoats(test[0], test[1])
    if result == test[2]:
        print("PASS")
    else:
        print("FAIL - " + str(result))