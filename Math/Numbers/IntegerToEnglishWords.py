"""
https://leetcode.com/problems/integer-to-english-words/description/?envType=daily-question&envId=2024-08-07

Convert a non-negative integer num to its English words representation.



Example 1:

Input: num = 123
Output: "One Hundred Twenty Three"
Example 2:

Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"


Constraints:

0 <= num <= 231 - 1
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 43
# ms
# Beats
# 16.42%
# Analyze Complexity
# Memory
# 16.62
# MB
# Beats
# 47.47%
class Solution:
    def numberToWords(self, num: int) -> str:
        DIV9 = 10 ** 9
        DIV6 = 10 ** 6
        DIV3 = 10 ** 3
        ones = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        # hundreds_names = ["Hundred", "Hundreds"]
        hundreds_names = ["Hundred", "Hundred"]

        def part_to_string(number, names = []):
            if not number:
                return ""
            result = ""
            n1 = number // 100
            number -= 100 * n1
            n2 = number // 10
            number -= 10 * n2
            if n1:
                result += ones[n1]
                result += " "
                result += hundreds_names[1] if n1 > 1 else hundreds_names[0]
            if n2 == 1:
                if result:
                    result += " "
                result += teens[number]
            else:
                if n2 > 0:
                    if result:
                        result += " "
                    result += tens[n2-1]
                if number > 0:
                    if result:
                        result += " "
                    result += ones[number]
            if names:
                result += " "
                result += names[1] if number > 1 else names[0]
            return result

        # thousands_names = ["Thousand", "Thousands"]
        thousands_names = ["Thousand", "Thousand"]
        # million_names = ["Million", "Millions"]
        million_names = ["Million", "Million"]
        # billion_names = ["Billion", "Billions"]
        billion_names = ["Billion", "Billion"]

        billions = num // DIV9
        num -= DIV9 * billions
        millions = num // DIV6
        num -= DIV6 * millions
        thousands = num // DIV3
        num -= DIV3 * thousands

        billions_part = part_to_string(billions, billion_names)
        millions_part = part_to_string(millions, million_names)
        thousands_part = part_to_string(thousands, thousands_names)
        ones_part = part_to_string(num)

        result = ""
        if billions_part:
            result += billions_part
        if millions_part:
            if result:
                result += " "
            result += millions_part
        if thousands_part:
            if result:
                result += " "
            result += thousands_part
        if ones_part:
            if result:
                result += " "
            result += ones_part
        if not result:
            result = "Zero"
        return result


tests = [
    [0, "Zero"],
    [100, "One Hundred"],

    [123, "One Hundred Twenty Three"],
    [12345, "Twelve Thousand Three Hundred Forty Five"],
    [1234567, "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"],
]

run_functional_tests(Solution().numberToWords, tests)
