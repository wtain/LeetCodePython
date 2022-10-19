"""
https://leetcode.com/problems/top-k-frequent-words/description/

Given an array of strings words and an integer k, return the k most frequent strings.

Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.



Example 1:

Input: words = ["i","love","leetcode","i","love","coding"], k = 2
Output: ["i","love"]
Explanation: "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.
Example 2:

Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
Output: ["the","is","sunny","day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words, with the number of occurrence being 4, 3, 2 and 1 respectively.


Constraints:

1 <= words.length <= 500
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
k is in the range [1, The number of unique words[i]]


Follow-up: Could you solve it in O(n log(k)) time and O(n) extra space?
"""
from collections import Counter
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 68 ms
# Beats
# 84%
# Memory
# 13.9 MB
# Beats
# 94.22%
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # Count all words
        counts = Counter(words)
        # Sort by count in descending order, and lexicographically for
        # words with the same count
        words_and_counts = sorted([(-counts[word], word) for word in counts])
        # Cut first k entries
        first_k_words_and_counts = words_and_counts[:k]
        # Take words from the tuples
        words_result = [word for count, word in first_k_words_and_counts]
        return words_result


tests = [
    [["i","love","leetcode","i","love","coding"], 2, ["i","love"]],
    [["the","day","is","sunny","the","the","the","sunny","is","is"], 4, ["the","is","sunny","day"]]
]

run_functional_tests(Solution().topKFrequent, tests)
