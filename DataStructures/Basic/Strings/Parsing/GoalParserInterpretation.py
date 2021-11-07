"""
https://leetcode.com/problems/goal-parser-interpretation/

You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", "()" and/or "(al)" in some order. The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". The interpreted strings are then concatenated in the original order.

Given the string command, return the Goal Parser's interpretation of command.



Example 1:

Input: command = "G()(al)"
Output: "Goal"
Explanation: The Goal Parser interprets the command as follows:
G -> G
() -> o
(al) -> al
The final concatenated result is "Goal".
Example 2:

Input: command = "G()()()()(al)"
Output: "Gooooal"
Example 3:

Input: command = "(al)G(al)()()G"
Output: "alGalooG"


Constraints:

1 <= command.length <= 100
command consists of "G", "()", and/or "(al)" in some order.
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 32 ms, faster than 55.57% of Python3 online submissions for Goal Parser Interpretation.
# Memory Usage: 14.2 MB, less than 38.40% of Python3 online submissions for Goal Parser Interpretation.
class Solution:
    def interpret(self, command: str) -> str:
        return command.replace("()", "o").replace("(al)", "al")


tests = [
    ["G()(al)", "Goal"],
    ["G()()()()(al)", "Gooooal"],
    ["(al)G(al)()()G", "alGalooG"]
]

run_functional_tests(Solution().interpret, tests)