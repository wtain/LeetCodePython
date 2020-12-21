"""
https://leetcode.com/problems/walking-robot-simulation/
A robot on an infinite grid starts at point (0, 0) and faces north.  The robot can receive one of three possible types of commands:

-2: turn left 90 degrees
-1: turn right 90 degrees
1 <= x <= 9: move forward x units
Some of the grid squares are obstacles.

The i-th obstacle is at grid point (obstacles[i][0], obstacles[i][1])

If the robot would try to move onto them, the robot stays on the previous grid square instead (but still continues following the rest of the route.)

Return the square of the maximum Euclidean distance that the robot will be from the origin.



Example 1:

Input: commands = [4,-1,3], obstacles = []
Output: 25
Explanation: robot will go to (3, 4)
Example 2:

Input: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
Output: 65
Explanation: robot will be stuck at (1, 4) before turning left and going to (1, 8)


Note:

0 <= commands.length <= 10000
0 <= obstacles.length <= 10000
-30000 <= obstacle[i][0] <= 30000
-30000 <= obstacle[i][1] <= 30000
The answer is guaranteed to be less than 2 ^ 31.

Runtime: 420 ms, faster than 20.54% of Python3 online submissions for Walking Robot Simulation.
Memory Usage: 19.9 MB, less than 85.55% of Python3 online submissions for Walking Robot Simulation.
"""
from typing import List, Dict


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x = 0
        y = 0
        direction = 2
        obs: Dict[int, set[int]] = {}
        for o in obstacles:
            ox = o[0]
            oy = o[1]
            if ox not in obs:
                obs[ox] = set()
            obs[ox].add(oy)

        def vectors() -> (int, int):
            nonlocal direction
            if direction == 0:  # South, down
                return 0, -1
            elif direction == 1: # West, left
                return -1, 0
            elif direction == 2: # North, up
                return 0, 1
            elif direction == 3: # East, right
                return 1, 0

        maxdist2 = 0
        for command in commands:
            if command < 0:
                if command == -1:
                    direction = (direction + 1) % 4
                elif command == -2:
                    direction = (direction + 3) % 4
            else:
                dx, dy = vectors()
                for i in range(command):
                    x1 = x + dx
                    y1 = y + dy
                    if x1 in obs and y1 in obs[x1]:
                        break
                    x = x1
                    y = y1
                    dist2 = x**2 + y**2
                    maxdist2 = max(dist2, maxdist2)
        return maxdist2


tests = [
    ([4,-1,3], [], 25),
    ([4,-1,4,-2,4], [[2,4]], 65)
]

for test in tests:
    result = Solution().robotSim(test[0], test[1])
    if result == test[2]:
        print("PASS")
    else:
        print ("FAIL: returned " + str(result) + ", expected " + str(test[2]))