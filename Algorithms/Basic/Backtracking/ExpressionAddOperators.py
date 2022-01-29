"""
https://leetcode.com/explore/featured/card/september-leetcoding-challenge-2021/638/week-3-september-15th-september-21st/3979/
https://leetcode.com/problems/expression-add-operators/

Given a string num that contains only digits and an integer target, return all possibilities to add the binary operators '+', '-', or '*' between the digits of num so that the resultant expression evaluates to the target value.



Example 1:

Input: num = "123", target = 6
Output: ["1*2*3","1+2+3"]
Example 2:

Input: num = "232", target = 8
Output: ["2*3+2","2+3*2"]
Example 3:

Input: num = "105", target = 5
Output: ["1*0+5","10-5"]
Example 4:

Input: num = "00", target = 0
Output: ["0*0","0+0","0-0"]
Example 5:

Input: num = "3456237490", target = 9191
Output: []


Constraints:

1 <= num.length <= 10
num consists of only digits.
-231 <= target <= 231 - 1
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# class Solution:
#     def addOperators(self, num: str, target: int) -> List[str]:
#
#         result = []
#         n = len(num)
#
#         def impl(i0: int, value0: int, mul0: int, current: int, sign: chr, output0: str):
#             nonlocal num, target, result
#             value = value0
#             if sign == '+':
#                 value += current
#             elif sign == '-':
#                 value -= current
#             elif sign == '*':
#                 value *= mul0
#             if output0:
#                 output = output0 + sign + str(current)
#             else:
#                 output = str(current)
#             if i0 == n:
#                 print(output, value)
#                 if value == target:
#                     result.append(output)
#                 return
#             impl(i0+1, value0, mul0, current*10+int(num[i0]), sign, output0)
#             impl(i0 + 1, value, current, 0, '+', output)
#             impl(i0 + 1, value, current, 0, '-', output)
#             impl(i0 + 1, value0, mul0*current, 0, '*', output)
#
#         impl(1, 0, 0, int(num[0]), '+', '')
#         return result


# WRONG
from Common.Helpers.ResultComparators import compareSets


# Runtime: 946 ms, faster than 35.75% of Python3 online submissions for Expression Add Operators.
# Memory Usage: 14.9 MB, less than 15.15% of Python3 online submissions for Expression Add Operators.
# https://leetcode.com/problems/expression-add-operators/solution/
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:

        result = []
        n = len(num)

        def impl(i: int, value: int, prev: int, current: int, output: List[str]):
            nonlocal num, target, result

            if i == n:
                if value == target and current == 0:
                    result.append("".join(output[1:]))
                return

            current = 10 * current + int(num[i])
            if current > 0:
                impl(i + 1, value, prev, current, output)

            output.append('+')
            output.append(str(current))
            impl(i + 1, value + current, current, 0, output)
            output.pop()
            output.pop()

            if output:
                output.append('-')
                output.append(str(current))
                impl(i + 1, value - current, -current, 0, output)
                output.pop()
                output.pop()

                output.append('*')
                output.append(str(current))
                impl(i + 1, value - prev + current * prev, prev*current, 0, output)
                output.pop()
                output.pop()

        impl(0, 0, 0, 0, [])
        return result


# https://leetcode.com/problems/expression-add-operators/solution/
# class Solution:
#     def addOperators(self, num: str, target: int) -> List[str]:


tests = [
    ["123", 6, ["1*2*3", "1+2+3"]],
    ["232", 8, ["2*3+2","2+3*2"]],
    ["105", 5, ["1*0+5","10-5"]],
    ["00", 0, ["0*0","0+0","0-0"]],
    ["3456237490", 9191, []]
]

run_functional_tests(Solution().addOperators, tests, custom_check=compareSets)
