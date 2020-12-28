"""
https://leetcode.com/problems/reorder-data-in-log-files/
You have an array of logs.  Each log is a space delimited string of words.

For each log, the first word in each log is an alphanumeric identifier.  Then, either:

Each word after the identifier will consist only of lowercase letters, or;
Each word after the identifier will consist only of digits.
We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at least one word after its identifier.

Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  The digit-logs should be put in their original order.

Return the final order of the logs.



Example 1:

Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]


Constraints:

0 <= logs.length <= 100
3 <= logs[i].length <= 100
logs[i] is guaranteed to have an identifier, and a word after the identifier.

Runtime: 40 ms, faster than 33.38% of Python3 online submissions for Reorder Data in Log Files.
Memory Usage: 14.6 MB, less than 6.78% of Python3 online submissions for Reorder Data in Log Files.

Runtime: 28 ms, faster than 97.39% of Python3 online submissions for Reorder Data in Log Files.
Memory Usage: 14.3 MB, less than 74.47% of Python3 online submissions for Reorder Data in Log Files.
"""
import functools
from typing import List


# class Solution:
#     def reorderLogFiles(self, logs: List[str]) -> List[str]:
#         records1 = []
#         records2 = []
#         for log in logs:
#             words = log.split(" ")
#             if words[1].isalpha():
#                 records1.append(words)
#             else:
#                 records2.append(words)
#
#         def compare(a, b) -> int:
#             def cmpimpl(s1: str, s2: str) -> int:
#                 if s1 == s2:
#                     return 0
#                 if s1 < s2:
#                     return -1
#                 return 1
#             n1 = len(a)
#             n2 = len(b)
#             i = 1
#             while i < n1 and i < n2 and a[i] == b[i]:
#                 i += 1
#             if i == n1 and i == n2:
#                 return cmpimpl(a[0], b[0])
#             if i == n1:
#                 return -1
#             if i == n2:
#                 return 1
#             return cmpimpl(a[i], b[i])
#         records1 = sorted(records1, key=functools.cmp_to_key(compare))
#         return [" ".join(record) for record in records1 + records2]

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        def get_key(log: str):
            id, rest = log.split(" ", maxsplit=1)
            return (0, rest, id) if rest[0].isalpha() else (1,)

        return sorted(logs, key=get_key)

tests = [
    (["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"],
     ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"])
]

for test in tests:
    logs = test[0]
    expected = test[1]
    result = Solution().reorderLogFiles(logs)
    if expected == result:
        print("PASS")
    else:
        print("FAIL - " + str(result))