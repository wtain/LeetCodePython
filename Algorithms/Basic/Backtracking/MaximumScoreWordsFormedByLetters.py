"""
https://leetcode.com/problems/maximum-score-words-formed-by-letters/description/?envType=daily-question&envId=2024-05-24

Given a list of words, list of  single letters (might be repeating) and score of every character.

Return the maximum score of any valid set of words formed by using the given letters (words[i] cannot be used two or more times).

It is not necessary to use all characters in letters and each letter can only be used once. Score of letters 'a', 'b', 'c', ... ,'z' is given by score[0], score[1], ... , score[25] respectively.



Example 1:

Input: words = ["dog","cat","dad","good"], letters = ["a","a","c","d","d","d","g","o","o"], score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
Output: 23
Explanation:
Score  a=1, c=9, d=5, g=3, o=2
Given letters, we can form the words "dad" (5+1+5) and "good" (3+2+2+5) with a score of 23.
Words "dad" and "dog" only get a score of 21.
Example 2:

Input: words = ["xxxz","ax","bx","cx"], letters = ["z","a","b","c","x","x","x"], score = [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]
Output: 27
Explanation:
Score  a=4, b=4, c=4, x=5, z=10
Given letters, we can form the words "ax" (4+5), "bx" (4+5) and "cx" (4+5) with a score of 27.
Word "xxxz" only get a score of 25.
Example 3:

Input: words = ["leetcode"], letters = ["l","e","t","c","o","d"], score = [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]
Output: 0
Explanation:
Letter "e" can only be used once.


Constraints:

1 <= words.length <= 14
1 <= words[i].length <= 15
1 <= letters.length <= 100
letters[i].length == 1
score.length == 26
0 <= score[i] <= 10
words[i], letters[i] contains only lower case English letters.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 347
# ms
# Beats
# 6.12%
# of users with Python3
# Memory
# 16.47
# MB
# Beats
# 99.55%
# of users with Python3
# https://leetcode.com/problems/maximum-score-words-formed-by-letters/editorial/?envType=daily-question&envId=2024-05-24
# class Solution:
#     def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
#         w = len(words)
#         freq = [0] * 26
#         for c in letters:
#             freq[ord(c) - ord('a')] += 1
#
#         def subset_score(subset_letters):
#             total_score = 0
#             for c in range(26):
#                 total_score += subset_letters[c] * score[c]
#                 if subset_letters[c] > freq[c]:
#                     return 0
#             return total_score
#
#         max_score = 0
#         for mask in range(1 << w):
#             subset_letters = [0] * 26
#             for i in range(w):
#                 if (mask & (1 << i)) > 0:
#                     L = len(words[i])
#                     for j in range(L):
#                         subset_letters[ord(words[i][j]) - ord('a')] += 1
#             max_score = max(max_score, subset_score(subset_letters))
#         return max_score


# Runtime
# 48
# ms
# Beats
# 70.07%
# of users with Python3
# Memory
# 16.72
# MB
# Beats
# 53.06%
# of users with Python3
# https://leetcode.com/problems/maximum-score-words-formed-by-letters/editorial/?envType=daily-question&envId=2024-05-24
class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        w = len(words)
        max_score = 0
        freq = [0] * 26
        subset_letters = [0] * 26
        for c in letters:
            freq[ord(c) - ord('a')] += 1

        def is_valid_word(subset_letters):
            for c in range(26):
                if freq[c] < subset_letters[c]:
                    return False
            return True

        def check(w, subset_letters, total_score):
            nonlocal max_score
            if w == -1:
                max_score = max(max_score, total_score)
                return
            check(w-1, subset_letters, total_score)
            L = len(words[w])
            for i in range(L):
                c = ord(words[w][i]) - ord('a')
                subset_letters[c] += 1
                total_score += score[c]

            if is_valid_word(subset_letters):
                check(w-1, subset_letters, total_score)

            for i in range(L):
                c = ord(words[w][i]) - ord('a')
                subset_letters[c] -= 1
                total_score -= score[c]

        check(w-1, subset_letters, 0)
        return max_score


tests = [
    [["dog","cat","dad","good"], ["a","a","c","d","d","d","g","o","o"], [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0], 23],
    [["xxxz","ax","bx","cx"], ["z","a","b","c","x","x","x"], [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10], 27],
    [["leetcode"], ["l","e","t","c","o","d"], [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0], 0],
]

run_functional_tests(Solution().maxScoreWords, tests)
