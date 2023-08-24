"""
https://leetcode.com/problems/text-justification/description/

Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.


Example 1:

Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Example 2:

Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified because it contains only one word.
Example 3:

Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]


Constraints:

1 <= words.length <= 300
1 <= words[i].length <= 20
words[i] consists of only English letters and symbols.
1 <= maxWidth <= 100
words[i].length <= maxWidth
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# Details
# 38ms
# Beats 83.23%of users with Python3
# Memory
# Details
# 16.27MB
# Beats 93.70%of users with Python3
# https://leetcode.com/problems/text-justification/editorial/
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        def get_words(i):
            current_line = []
            curr_length = 0
            while i < len(words) and curr_length + len(words[i]) <= maxWidth:
                current_line.append(words[i])
                curr_length += len(words[i]) + 1
                i += 1
            return current_line

        def create_line(line, i):
            base_length = -1
            for word in line:
                base_length += len(word) + 1
            extra_spaces = maxWidth - base_length
            if len(line) == 1 or i == len(words):
                return " ".join(line) + " " * extra_spaces
            word_count = len(line) - 1
            spaces_per_word = extra_spaces // word_count
            needs_extra_space = extra_spaces % word_count

            for j in range(needs_extra_space):
                line[j] += ' '

            for j in range(word_count):
                line[j] += " " * spaces_per_word

            return " ".join(line)

        result = []
        i = 0
        while i < len(words):
            current_line = get_words(i)
            i += len(current_line)
            result.append(create_line(current_line, i))
        return result


tests = [
    [
        ["This", "is", "an", "example", "of", "text", "justification."],
        16,
        [
           "This    is    an",
           "example  of text",
           "justification.  "
        ]
     ],
    [
        ["What","must","be","acknowledgment","shall","be"],
        16,
        [
          "What   must   be",
          "acknowledgment  ",
          "shall be        "
        ]
    ],
    [
        ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"],
        20,
        [
          "Science  is  what we",
          "understand      well",
          "enough to explain to",
          "a  computer.  Art is",
          "everything  else  we",
          "do                  "
        ]
    ],
]

run_functional_tests(Solution().fullJustify, tests)
