"""
https://leetcode.com/problems/robot-bounded-in-circle/

On an infinite plane, a robot initially stands at (0, 0) and faces north. The robot can receive one of three instructions:

"G": go straight 1 unit;
"L": turn 90 degrees to the left;
"R": turn 90 degrees to the right.
The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.



Example 1:

Input: instructions = "GGLLGG"
Output: true
Explanation: The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.
Example 2:

Input: instructions = "GG"
Output: false
Explanation: The robot moves north indefinitely.
Example 3:

Input: instructions = "GL"
Output: true
Explanation: The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...


Constraints:

1 <= instructions.length <= 100
instructions[i] is 'G', 'L' or, 'R'.

Calculate the final vector of how the robot travels after executing all instructions once - it consists of a change in position plus a change in direction.

The robot stays in the circle if and only if (looking at the final vector) it changes direction (ie. doesn't stay pointing north), or it moves 0.
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 51 ms, faster than 11.62% of Python3 online submissions for Robot Bounded In Circle.
# Memory Usage: 14.3 MB, less than 49.85% of Python3 online submissions for Robot Bounded In Circle.
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        directions = [[0, -1], [1, 0], [0, 1], [-1, 0]]
        cur_dir = 0
        position = [0, 0]
        for c in instructions:
            if c == "G":
                position[0] += directions[cur_dir][0]
                position[1] += directions[cur_dir][1]
            elif c == "L":
                cur_dir = (cur_dir + 3) % 4
            elif c == "R":
                cur_dir = (cur_dir + 1) % 4
        return cur_dir != 0 or position == [0, 0]


tests = [
    ["GLRLLGLL", True],
    ["GGLLGG", True],
    ["GG", False],
    ["GL", True]
]

run_functional_tests(Solution().isRobotBounded, tests)
