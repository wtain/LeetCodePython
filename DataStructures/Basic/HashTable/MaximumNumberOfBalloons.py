"""
https://leetcode.com/explore/featured/card/september-leetcoding-challenge-2021/637/week-2-september-8th-september-14th/3973/
https://leetcode.com/problems/maximum-number-of-balloons/

Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.



Example 1:



Input: text = "nlaebolko"
Output: 1
Example 2:



Input: text = "loonbalxballpoon"
Output: 2
Example 3:

Input: text = "leetcode"
Output: 0


Constraints:

1 <= text.length <= 104
text consists of lower case English letters only.
"""
from collections import Counter

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 36 ms, faster than 50.71% of Python3 online submissions for Maximum Number of Balloons.
# Memory Usage: 14.5 MB, less than 20.82% of Python3 online submissions for Maximum Number of Balloons.
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        letters = Counter(text)
        target = Counter("balloon")
        cnt = None
        for c in target:
            wcnt = letters[c] // target[c]
            if cnt is None or wcnt < cnt:
                cnt = wcnt
        return cnt if cnt is not None else 0


tests = [
    ["nlaebolko", 1],
    ["loonbalxballpoon", 2],
    ["leetcode", 0]
]

run_functional_tests(Solution().maxNumberOfBalloons, tests)