"""
https://leetcode.com/problems/determine-color-of-a-chessboard-square/

You are given coordinates, a string that represents the coordinates of a square of the chessboard. Below is a chessboard for your reference.



Return true if the square is white, and false if the square is black.

The coordinate will always represent a valid chessboard square. The coordinate will always have the letter first, and the number second.



Example 1:

Input: coordinates = "a1"
Output: false
Explanation: From the chessboard above, the square with coordinates "a1" is black, so return false.
Example 2:

Input: coordinates = "h3"
Output: true
Explanation: From the chessboard above, the square with coordinates "h3" is white, so return true.
Example 3:

Input: coordinates = "c7"
Output: false


Constraints:

coordinates.length == 2
'a' <= coordinates[0] <= 'h'
'1' <= coordinates[1] <= '8'
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 32 ms, faster than 54.06% of Python3 online submissions for Determine Color of a Chessboard Square.
# Memory Usage: 14.1 MB, less than 87.91% of Python3 online submissions for Determine Color of a Chessboard Square.
class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        return (ord(coordinates[0]) - ord('a') + ord(coordinates[1]) - ord('1')) % 2 == 1


tests = [
    ["a1", False],
    ["h3", True],
    ["c7", False]
]

run_functional_tests(Solution().squareIsWhite, tests)