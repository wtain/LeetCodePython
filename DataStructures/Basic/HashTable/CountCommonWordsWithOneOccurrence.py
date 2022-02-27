"""
https://leetcode.com/problems/count-common-words-with-one-occurrence/

Given two string arrays words1 and words2, return the number of strings that appear exactly once in each of the two arrays.



Example 1:

Input: words1 = ["leetcode","is","amazing","as","is"], words2 = ["amazing","leetcode","is"]
Output: 2
Explanation:
- "leetcode" appears exactly once in each of the two arrays. We count this string.
- "amazing" appears exactly once in each of the two arrays. We count this string.
- "is" appears in each of the two arrays, but there are 2 occurrences of it in words1. We do not count this string.
- "as" appears once in words1, but does not appear in words2. We do not count this string.
Thus, there are 2 strings that appear exactly once in each of the two arrays.
Example 2:

Input: words1 = ["b","bb","bbb"], words2 = ["a","aa","aaa"]
Output: 0
Explanation: There are no strings that appear in each of the two arrays.
Example 3:

Input: words1 = ["a","ab"], words2 = ["a","a","a","ab"]
Output: 1
Explanation: The only string that appears exactly once in each of the two arrays is "ab".


Constraints:

1 <= words1.length, words2.length <= 1000
1 <= words1[i].length, words2[j].length <= 30
words1[i] and words2[j] consists only of lowercase English letters.
"""
from collections import Counter
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 68 ms, faster than 89.82% of Python3 online submissions for Count Common Words With One Occurrence.
# Memory Usage: 14.5 MB, less than 79.21% of Python3 online submissions for Count Common Words With One Occurrence.
# class Solution:
#     def countWords(self, words1: List[str], words2: List[str]) -> int:
#         c1, c2 = Counter(words1), Counter(words2)
#         result = 0
#         for w in c1:
#             if c1[w] > 1:
#                 continue
#             if w not in c2:
#                 continue
#             if c2[w] == 1:
#                 result += 1
#         return result

# Runtime: 120 ms, faster than 43.98% of Python3 online submissions for Count Common Words With One Occurrence.
# Memory Usage: 14.5 MB, less than 79.21% of Python3 online submissions for Count Common Words With One Occurrence.
class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        c1, c2 = Counter(words1), Counter(words2)
        return sum(1 for w in c1 if c1[w] == 1 and c2[w] == 1)


tests = [
    [["leetcode","is","amazing","as","is"], ["amazing","leetcode","is"], 2],
    [["b","bb","bbb"], ["a","aa","aaa"], 0],
    [["a","ab"], ["a","a","a","ab"], 1]
]

run_functional_tests(Solution().countWords, tests)

