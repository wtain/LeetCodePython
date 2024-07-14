"""
https://leetcode.com/problems/number-of-atoms/description/?envType=daily-question&envId=2024-07-14

Given a string formula representing a chemical formula, return the count of each atom.

The atomic element always starts with an uppercase character, then zero or more lowercase letters, representing the name.

One or more digits representing that element's count may follow if the count is greater than 1. If the count is 1, no digits will follow.

For example, "H2O" and "H2O2" are possible, but "H1O2" is impossible.
Two formulas are concatenated together to produce another formula.

For example, "H2O2He3Mg4" is also a formula.
A formula placed in parentheses, and a count (optionally added) is also a formula.

For example, "(H2O2)" and "(H2O2)3" are formulas.
Return the count of all elements as a string in the following form: the first name (in sorted order), followed by its count (if that count is more than 1), followed by the second name (in sorted order), followed by its count (if that count is more than 1), and so on.

The test cases are generated so that all the values in the output fit in a 32-bit integer.



Example 1:

Input: formula = "H2O"
Output: "H2O"
Explanation: The count of elements are {'H': 2, 'O': 1}.
Example 2:

Input: formula = "Mg(OH)2"
Output: "H2MgO2"
Explanation: The count of elements are {'H': 2, 'Mg': 1, 'O': 2}.
Example 3:

Input: formula = "K4(ON(SO3)2)2"
Output: "K4N2O14S4"
Explanation: The count of elements are {'K': 4, 'N': 2, 'O': 14, 'S': 4}.


Constraints:

1 <= formula.length <= 1000
formula consists of English letters, digits, '(', and ')'.
formula is always valid.
"""
import re
from collections import defaultdict

from Common.ObjectTestingUtils import run_functional_tests


# WRONG
# class Solution:
#     def countOfAtoms(self, formula: str) -> str:
#         tokens = []
#         n = len(formula)
#         i = 0
#         while i < n:
#             if 'A' <= formula[i] <= 'Z':
#                 current = formula[i]
#                 i += 1
#                 while i < n and 'a' <= formula[i] <= 'z':
#                     current += formula[i]
#                     i += 1
#                 tokens.append(current)
#             elif formula[i] in {'(', ')'}:
#                 tokens.append(formula[i])
#                 i += 1
#             elif str.isdigit(formula[i]):
#                 current = formula[i]
#                 i += 1
#                 while i < n and 'a' <= formula[i] <= 'z':
#                     current += formula[i]
#                     i += 1
#                 tokens.append(current)
#
#         counts = defaultdict(int)
#         n = len(tokens)
#         i = n-1
#         multipliers = [1]
#         while i >= 0:
#             if str.isdigit(tokens[i][0]):
#                 multipliers.append(int(tokens[i]) * multipliers[-1])
#             elif tokens[i] == ')':
#                 pass
#             elif tokens[i] == '(':
#                 multipliers.pop()
#             else:
#                 counts[tokens[i]] += multipliers[-1]
#             i -= 1
#
#         return "".join({ (k + str(counts[k]) if counts[k] > 1 else k) for k in reversed(sorted(counts.keys()))})


# Runtime
# 43
# ms
# Beats
# 14.25%
# Analyze Complexity
# Memory
# 16.75
# MB
# Beats
# 9.50%
# https://leetcode.com/problems/number-of-atoms/editorial/?envType=daily-question&envId=2024-07-14
# class Solution:
#     def countOfAtoms(self, formula: str) -> str:
#         n = len(formula)
#
#         self.index = 0
#
#         def parse_formula():
#             curr_map = defaultdict(int)
#
#             while self.index < n and formula[self.index] != ")":
#                 if formula[self.index] == "(":
#                     self.index += 1
#                     nested_map = parse_formula()
#                     for atom in nested_map:
#                         curr_map[atom] += nested_map[atom]
#                 else:
#                     curr_atom = formula[self.index]
#                     self.index += 1
#                     while self.index < n and formula[self.index].islower():
#                         curr_atom += formula[self.index]
#                         self.index += 1
#
#                     curr_count = ""
#                     while self.index < n and formula[self.index].isdigit():
#                         curr_count += formula[self.index]
#                         self.index += 1
#
#                     if curr_count == "":
#                         curr_map[curr_atom] += 1
#                     else:
#                         curr_map[curr_atom] += int(curr_count)
#             self.index += 1
#             multiplier = ""
#             while self.index < n and formula[self.index].isdigit():
#                 multiplier += formula[self.index]
#                 self.index += 1
#
#             if multiplier:
#                 multiplier = int(multiplier)
#                 for atom in curr_map:
#                     curr_map[atom] *= multiplier
#
#             return curr_map
#
#         final_map = parse_formula()
#
#         final_map = dict(sorted(final_map.items()))
#
#         result = ""
#         for atom in final_map:
#             result += atom
#             if final_map[atom] > 1:
#                 result += str(final_map[atom])
#
#         return result


# Runtime
# 35
# ms
# Beats
# 66.98%
# Analyze Complexity
# Memory
# 16.68
# MB
# Beats
# 28.74%
# https://leetcode.com/problems/number-of-atoms/editorial/?envType=daily-question&envId=2024-07-14
# class Solution:
#     def countOfAtoms(self, formula: str) -> str:
#         st = [defaultdict(int)]
#         index = 0
#
#         while index < len(formula):
#             if formula[index] == "(":
#                 st.append(defaultdict(int))
#                 index += 1
#             elif formula[index] == ")":
#                 curr_map = st.pop()
#                 index += 1
#                 multiplier = ""
#                 while index < len(formula) and formula[index].isdigit():
#                     multiplier += formula[index]
#                     index += 1
#                 if multiplier:
#                     multiplier = int(multiplier)
#                     for atom in curr_map:
#                         curr_map[atom] *= multiplier
#                 for atom in curr_map:
#                     st[-1][atom] += curr_map[atom]
#             else:
#                 curr_atom = formula[index]
#                 index += 1
#                 while index < len(formula) and formula[index].islower():
#                     curr_atom += formula[index]
#                     index += 1
#
#                 curr_count = ""
#                 while index < len(formula) and formula[index].isdigit():
#                     curr_count += formula[index]
#                     index += 1
#
#                 if curr_count == "":
#                     st[-1][curr_atom] += 1
#                 else:
#                     st[-1][curr_atom] += int(curr_count)
#         final_map = dict(sorted(st[0].items()))
#
#         result = ""
#         for atom in final_map:
#             result += atom
#             if final_map[atom] > 1:
#                 result += str(final_map[atom])
#         return result


# Runtime
# 35
# ms
# Beats
# 66.98%
# Analyze Complexity
# Memory
# 16.72
# MB
# Beats
# 9.50%
# https://leetcode.com/problems/number-of-atoms/editorial/?envType=daily-question&envId=2024-07-14
# class Solution:
#     def countOfAtoms(self, formula: str) -> str:
#         regex = r"([A-Z][a-z]*)(\d*)|(\()|(\))(\d*)"
#         matcher = re.findall(regex, formula)
#
#         st = [defaultdict(int)]
#
#         for atom, count, left, right, multiplier in matcher:
#             if atom:
#                 st[-1][atom] += int(count) if count else 1
#             elif left:
#                 st.append(defaultdict(int))
#             elif right:
#                 curr_map = st.pop()
#                 if multiplier:
#                     multiplier = int(multiplier)
#                     for atom in curr_map:
#                         curr_map[atom] *= multiplier
#                 for atom in curr_map:
#                     st[-1][atom] += curr_map[atom]
#
#         final_map = dict(sorted(st[0].items()))
#
#         result = ""
#         for atom in final_map:
#             result += atom
#             if final_map[atom] > 1:
#                 result += str(final_map[atom])
#
#         return result


# Runtime
# 42
# ms
# Beats
# 17.58%
# Analyze Complexity
# Memory
# 16.64
# MB
# Beats
# 28.74%
# https://leetcode.com/problems/number-of-atoms/editorial/?envType=daily-question&envId=2024-07-14
# class Solution:
#     def countOfAtoms(self, formula: str) -> str:
#         running_mul = 1
#         st = [1]
#         final_map = defaultdict(int)
#
#         curr_atom = ""
#         curr_count = ""
#
#         index = len(formula) - 1
#
#         while index >= 0:
#             if formula[index].isdigit():
#                 curr_count = formula[index] + curr_count
#             elif formula[index].islower():
#                 curr_atom = formula[index] + curr_atom
#             elif formula[index].isupper():
#                 curr_atom = formula[index] + curr_atom
#                 if curr_count:
#                     final_map[curr_atom] += int(curr_count) * running_mul
#                 else:
#                     final_map[curr_atom] += 1 * running_mul
#
#                 curr_atom = ""
#                 curr_count = ""
#             elif formula[index] == ")":
#                 curr_multiplier = int(curr_count) if curr_count else 1
#                 st.append(curr_multiplier)
#                 running_mul *= curr_multiplier
#                 curr_count = ""
#             elif formula[index] == "(":
#                 running_mul //= st.pop()
#
#             index -= 1
#
#         final_map = dict(sorted(final_map.items()))
#
#         result = ""
#         for atom in final_map:
#             result += atom
#             if final_map[atom] > 1:
#                 result += str(final_map[atom])
#
#         return result


# Runtime
# 34
# ms
# Beats
# 73.63%
# Analyze Complexity
# Memory
# 16.68
# MB
# Beats
# 28.74%
# https://leetcode.com/problems/number-of-atoms/editorial/?envType=daily-question&envId=2024-07-14
# class Solution:
#     def countOfAtoms(self, formula: str) -> str:
#         muls = []
#         running_mul = 1
#         st = [1]
#
#         index = len(formula) - 1
#         curr_number = ""
#         while index >= 0:
#             if formula[index].isdigit():
#                 curr_number += formula[index]
#             elif formula[index].isalpha():
#                 curr_number = ""
#             elif formula[index] == ")":
#                 curr_multiplier = int(curr_number[::-1] if curr_number else 1)
#                 running_mul *= curr_multiplier
#                 st.append(curr_multiplier)
#                 curr_number = ""
#             elif formula[index] == "(":
#                 running_mul //= st.pop()
#                 curr_number = ""
#
#             muls.append(running_mul)
#             index -= 1
#
#         muls = muls[::-1]
#
#         final_map = defaultdict(int)
#
#         index = 0
#         while index < len(formula):
#             if formula[index].isupper():
#                 curr_atom = formula[index]
#                 curr_count = ""
#                 index += 1
#                 while index < len(formula) and formula[index].islower():
#                     curr_atom += formula[index]
#                     index += 1
#
#                 while index < len(formula) and formula[index].isdigit():
#                     curr_count += formula[index]
#                     index += 1
#
#                 if curr_count:
#                     final_map[curr_atom] += int(curr_count) * muls[index-1]
#                 else:
#                     final_map[curr_atom] += 1 * muls[index-1]
#             else:
#                 index += 1
#         final_map = dict(sorted(final_map.items()))
#
#         result = ""
#         for atom in final_map:
#             result += atom
#             if final_map[atom] > 1:
#                 result += str(final_map[atom])
#
#         return result


# Runtime
# 27
# ms
# Beats
# 96.91%
# Analyze Complexity
# Memory
# 16.55
# MB
# Beats
# 63.66%
# https://leetcode.com/problems/number-of-atoms/editorial/?envType=daily-question&envId=2024-07-14
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        matcher = re.findall(r"([A-Z][a-z]*)(\d*)|(\()|(\))(\d*)", formula)
        matcher.reverse()

        final_map = defaultdict(int)

        st = [1]

        running_mul = 1

        for atom, count, left, right, multiplier in matcher:
            if atom:
                if count:
                    final_map[atom] += int(count) * running_mul
                else:
                    final_map[atom] += 1 * running_mul
            elif right:
                if not multiplier:
                    multiplier = 1
                else:
                    multiplier = int(multiplier)
                running_mul *= multiplier
                st.append(multiplier)
            elif left:
                running_mul //= st.pop()
        final_map = dict(sorted(final_map.items()))

        result = ""
        for atom in final_map:
            result += atom
            if final_map[atom] > 1:
                result += str(final_map[atom])

        return result



tests = [
    ["H2O", "H2O"],
    ["Mg(OH)2", "H2MgO2"],
    ["K4(ON(SO3)2)2", "K4N2O14S4"],
]

run_functional_tests(Solution().countOfAtoms, tests)
