"""
https://leetcode.com/problems/count-pairs-of-similar-strings/

You are given a 0-indexed string array words.

Two strings are similar if they consist of the same characters.

For example, "abca" and "cba" are similar since both consist of characters 'a', 'b', and 'c'.
However, "abacba" and "bcfd" are not similar since they do not consist of the same characters.
Return the number of pairs (i, j) such that 0 <= i < j <= word.length - 1 and the two strings words[i] and words[j] are similar.



Example 1:

Input: words = ["aba","aabb","abcd","bac","aabc"]
Output: 2
Explanation: There are 2 pairs that satisfy the conditions:
- i = 0 and j = 1 : both words[0] and words[1] only consist of characters 'a' and 'b'.
- i = 3 and j = 4 : both words[3] and words[4] only consist of characters 'a', 'b', and 'c'.
Example 2:

Input: words = ["aabb","ab","ba"]
Output: 3
Explanation: There are 3 pairs that satisfy the conditions:
- i = 0 and j = 1 : both words[0] and words[1] only consist of characters 'a' and 'b'.
- i = 0 and j = 2 : both words[0] and words[2] only consist of characters 'a' and 'b'.
- i = 1 and j = 2 : both words[1] and words[2] only consist of characters 'a' and 'b'.
Example 3:

Input: words = ["nba","cba","dba"]
Output: 0
Explanation: Since there does not exist any pair that satisfies the conditions, we return 0.


Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consist of only lowercase English letters.
"""
from collections import Counter
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 59 ms
# Beats
# 90.29%
# Memory
# 13.9 MB
# Beats
# 64.62%
class Solution:
    def similarPairs(self, words: List[str]) -> int:
        c = Counter("".join(sorted(set(w))) for w in words)
        return sum(c[k]*(c[k]-1)//2 for k in c)


tests = [
    [["ofwqemdbhrcckcnqvovyjwnbqxckhfohlripwumugcirazdtwo","hsrmuokwhksqkkjblkomibcifqilkwobwcpwwkjlzohffsajrt","uzvsxxbdwfohaujijxmeijbwyydgjiifcqvxfzmkqgwnkpxlpp","ksdoiwhffhymsxebloadgyigkveizbahnbmvmxsuuxaaegxmpe","fcsjnezuizcnfsuaxpmxpdivamaijvvyyqlsjsqlkifahjuanb","odfwurhxumkpwndsppoflaualeghyscdqqwpntxokxviqmjhyq","jbahicbweamnlfbljwyloparlmgqlwiootzoeqovytpapzjezn","vsjxngyknxpkjfexdvmoikjaiccplcwtxcfrljqavatpcoeaqe","lxiztvpppvsjmnnuunvdxalvzuvxlxbdnipexklmgsssyzlesb","kbmiambdsahiptndziqysctinvdekysrsslssusqwhshpwehco","wuwkvgrrshrmbtpyozgzzwiyflpiuklsepljvthmxnppaspuqt","lkajvmdzpsxoaqzrgrhuhhmwlgwfnruxsrjolnielwcyjvvhaa","imvgnslsxyqfshgmgecdrignarewusftipgjpteocnlqsfkdcy"], 1],
    [["aba","aabb","abcd","bac","aabc"], 2],
    [["aabb","ab","ba"], 3],
    [["nba","cba","dba"], 0],
]

run_functional_tests(Solution().similarPairs, tests)
