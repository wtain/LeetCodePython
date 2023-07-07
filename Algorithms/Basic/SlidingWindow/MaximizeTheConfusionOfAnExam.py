"""
https://leetcode.com/problems/maximize-the-confusion-of-an-exam/description/

A teacher is writing a test with n true/false questions, with 'T' denoting true and 'F' denoting false. He wants to confuse the students by maximizing the number of consecutive questions with the same answer (multiple trues or multiple falses in a row).

You are given a string answerKey, where answerKey[i] is the original answer to the ith question. In addition, you are given an integer k, the maximum number of times you may perform the following operation:

Change the answer key for any question to 'T' or 'F' (i.e., set answerKey[i] to 'T' or 'F').
Return the maximum number of consecutive 'T's or 'F's in the answer key after performing the operation at most k times.



Example 1:

Input: answerKey = "TTFF", k = 2
Output: 4
Explanation: We can replace both the 'F's with 'T's to make answerKey = "TTTT".
There are four consecutive 'T's.
Example 2:

Input: answerKey = "TFFT", k = 1
Output: 3
Explanation: We can replace the first 'T' with an 'F' to make answerKey = "FFFT".
Alternatively, we can replace the second 'T' with an 'F' to make answerKey = "TFFF".
In both cases, there are three consecutive 'F's.
Example 3:

Input: answerKey = "TTFTTFTT", k = 1
Output: 5
Explanation: We can replace the first 'F' to make answerKey = "TTTTTFTT"
Alternatively, we can replace the second 'F' to make answerKey = "TTFTTTTT".
In both cases, there are five consecutive 'T's.


Constraints:

n == answerKey.length
1 <= n <= 5 * 104
answerKey[i] is either 'T' or 'F'
1 <= k <= n
"""
from collections import Counter

from Common.ObjectTestingUtils import run_functional_tests


# class Solution:
#     def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
#         lf, lt = 0, 0
#         cf, ct = 0, 0
#         changes_f, changes_t = 0, 0
#         return max(lf, lt)


# Runtime
# 423 ms
# Beats
# 64.63%
# Memory
# 16.9 MB
# Beats
# 19.82%
# https://leetcode.com/problems/maximize-the-confusion-of-an-exam/editorial/
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        result = k
        count = Counter(answerKey[:k])
        left = 0
        for right in range(k, len(answerKey)):
            count[answerKey[right]] += 1
            while min(count['T'], count['F']) > k:
                count[answerKey[left]] -= 1
                left += 1
            result = max(result, right - left + 1)
        return result


tests = [
    ["TTFF", 2, 4],
    ["TFFT", 1, 3],
    ["TTFTTFTT", 1, 5],
    ["F", 1, 1],
]

run_functional_tests(Solution().maxConsecutiveAnswers, tests)
