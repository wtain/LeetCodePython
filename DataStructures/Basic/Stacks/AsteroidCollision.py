"""
https://leetcode.com/problems/asteroid-collision/

We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.



Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
Example 2:

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.
Example 3:

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.


Constraints:

2 <= asteroids.length <= 104
-1000 <= asteroids[i] <= 1000
asteroids[i] != 0
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# WRONG
# class Solution:
#     def asteroidCollision(self, asteroids: List[int]) -> List[int]:
#         left = [asteroid for asteroid in asteroids if asteroid > 0]
#         right = [-asteroid for asteroid in reversed(asteroids) if asteroid < 0]
#         result = []
#         while left and right:
#             l, r = left.pop(), right.pop()
#             if l < r:
#                 result.append(r)
#             elif l > r:
#                 result.append(l)
#         result = left + result
#         result += [-asteroid for asteroid in right]
#         return result

# WRONG
# class Solution:
#     def asteroidCollision(self, asteroids: List[int]) -> List[int]:
#         result = []
#         for asteroid in asteroids:
#             if not result:
#                 result.append(asteroid)
#             else:
#                 if result[-1] * asteroid > 0:
#                     result.append(asteroid)
#                 else:
#                     while result and result[-1] > 0 > asteroid and abs(result[-1]) < abs(asteroid):
#                         result[-1] = asteroid
#                     if result and abs(result[-1]) == abs(asteroid) and asteroid < 0:
#                         result.pop()
#                     else:
#                         result.append(asteroid)
#         return result


# Runtime
# 234 ms
# Beats
# 36.89%
# Memory
# 15.3 MB
# Beats
# 24.66%
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        result = []
        for asteroid in asteroids:
            if not result:                                                 # If there are no asteroids on the left
                result.append(asteroid)                                    # Add current to the result
            else:                                                          # Otherwise we need to check if there is a collision
                if asteroid > 0:                                           # If current asteroid flies to the right
                    result.append(asteroid)                                # it does not collide with the ones on the left, so add it
                else:
                    if result[-1] < 0:                                     # If previous asteroid flies to the left, it can't
                        result.append(asteroid)                            # collide with the current one, so add it
                    else:                                                  # Otherwise previous one flies to the right
                        while result and result[-1] > 0 and abs(result[-1]) < abs(asteroid):  # while current one flies to the left, so there is a collision
                            result.pop()                                   # Let's eliminate all from the left, which fly to the right, and which are strictly smaller
                        if not result or result[-1] < 0:                   # If we removed all from the left, then add current to the result
                            result.append(asteroid)                        # if there are no asteroids flying to the right
                        elif result[-1] > 0 and abs(result[-1]) == abs(asteroid): # If there is a same-size asteroid on the left which is flying to the right,
                            result.pop()                                   # then both current and the left one collide
        return result


tests = [
    [[-2,-2,1,-2], [-2,-2,-2]],
    [[-2,-1,1,2], [-2,-1,1,2]],
    [[5,10,-5], [5,10]],
    [[8,-8], []],
    [[10,2,-5], [10]]
]

run_functional_tests(Solution().asteroidCollision, tests)
