"""
https://leetcode.com/explore/featured/card/may-leetcoding-challenge-2021/602/week-5-may-29th-may-31st/3762/
https://leetcode.com/problems/search-suggestions-system/

Given an array of strings products and a string searchWord. We want to design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with the searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

Return list of lists of the suggested products after each character of searchWord is typed.



Example 1:

Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
["mouse","mousepad"],
["mouse","mousepad"],
["mouse","mousepad"]
]
Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
After typing mou, mous and mouse the system suggests ["mouse","mousepad"]
Example 2:

Input: products = ["havana"], searchWord = "havana"
Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
Example 3:

Input: products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"
Output: [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]
Example 4:

Input: products = ["havana"], searchWord = "tatiana"
Output: [[],[],[],[],[],[],[]]


Constraints:

1 <= products.length <= 1000
There are no repeated elements in products.
1 <= Σ products[i].length <= 2 * 10^4
All characters of products[i] are lower-case English letters.
1 <= searchWord.length <= 1000
All characters of searchWord are lower-case English letters.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 752 ms, faster than 15.63% of Python3 online submissions for Search Suggestions System.
# Memory Usage: 21.9 MB, less than 14.24% of Python3 online submissions for Search Suggestions System.
# class Solution:
#     def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
#         Trie = lambda: collections.defaultdict(Trie)
#         trie = Trie()
#
#         def addWord(w: str):
#             nonlocal trie
#             cur = trie
#             for c in w:
#                 cur = cur[c]
#             cur['$'] = Trie()  # end
#
#         for w in products:
#             addWord(w)
#
#         result = []
#
#         def traverse(prefix: str, cur: Trie, res: List[str]):
#             if '$' in cur:
#                 res.append(prefix)
#                 if len(res) == 3:
#                     return
#             for c in sorted(cur.keys()):
#                 if c == '$':
#                     continue
#                 traverse(prefix + c, cur[c], res)
#                 if len(res) == 3:
#                     return
#
#         prefix = ""
#         cur = trie
#         ok = True
#         for c in searchWord:
#             res = []
#             prefix += c
#             if ok and c in cur:
#                 cur = cur[c]
#                 traverse(prefix, cur, res)
#             else:
#                 ok = False
#             result.append(res)
#
#         return result

# Runtime: 792 ms, faster than 14.77% of Python3 online submissions for Search Suggestions System.
# Memory Usage: 22 MB, less than 14.24% of Python3 online submissions for Search Suggestions System.
# class Solution:
#     def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
#         Trie = lambda: collections.defaultdict(Trie)
#         trie = Trie()
#
#         def addWord(w: str):
#             nonlocal trie
#             cur = trie
#             for c in w:
#                 cur = cur[c]
#             cur['$'] = Trie()  # end
#
#         for w in products:
#             addWord(w)
#
#         def traverse(prefix: str, cur: Trie, res: List[str]):
#             if '$' in cur:
#                 res.append(prefix)
#                 if len(res) == 3:
#                     return
#             for c in sorted(cur.keys()):
#                 if c == '$':
#                     continue
#                 traverse(prefix + c, cur[c], res)
#                 if len(res) == 3:
#                     return
#
#         def check(w: str, i: int, cur: Trie) -> bool:
#             if i == len(w):
#                 return True
#             if w[i] not in cur:
#                 return False
#             return check(w, i+1, cur[w[i]])
#
#         prefix = ""
#         cur = trie
#         ok = True
#         l, r = 0, len(searchWord)
#         while l < r:
#             # print(l, r)
#             m = l + (r-l) // 2
#             w = searchWord[:m+1]
#             # print(w)
#             if check(w, 0, trie):
#                 l = m+1
#             else:
#                 r = m
#
#         result = []
#
#         # print(l)
#         for c in searchWord[:l]:
#             res = []
#             prefix += c
#             if ok and c in cur:
#                 cur = cur[c]
#                 traverse(prefix, cur, res)
#             else:
#                 ok = False
#             result.append(res)
#
#         for i in range(l+1, len(searchWord)+1):
#             result.append([])
#
#         return result

# Runtime: 128 ms, faster than 68.52% of Python3 online submissions for Search Suggestions System.
# Memory Usage: 17.1 MB, less than 73.34% of Python3 online submissions for Search Suggestions System.
# class Solution:
#     def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
#
#         products = sorted(products)
#
#         result = []
#         l, r = 0, len(products)
#
#         prefix = ""
#         for c in searchWord:
#             prefix += c
#             l, r = 0, len(products)
#             while l < r:
#                 m = l + (r - l) // 2
#                 if prefix > products[m]:
#                     l = m + 1
#                 else:
#                     r = m
#             if l <= r:
#                 res = []
#                 for i in range(3):
#                     if l + i >= len(products):
#                         break
#                     if prefix != products[l+i][:len(prefix)]:
#                         break
#                     res.append(products[l+i])
#                 result.append(res)
#
#         m = len(result)
#         for i in range(len(searchWord) - m):
#             result.append([])
#
#         return result


# Runtime: 120 ms, faster than 69.81% of Python3 online submissions for Search Suggestions System.
# Memory Usage: 17.1 MB, less than 55.25% of Python3 online submissions for Search Suggestions System.
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:

        products = sorted(products)

        result = []
        l0, r0 = 0, len(products)

        prefix = ""
        for c in searchWord:
            prefix += c
            l, r = l0, r0
            while l < r:
                m = l + (r - l) // 2
                if prefix > products[m]:
                    l = m + 1
                else:
                    r = m
            l0 = l
            if l <= r:
                res = []
                for i in range(3):
                    if l + i >= len(products):
                        break
                    if prefix != products[l+i][:len(prefix)]:
                        break
                    res.append(products[l+i])
                result.append(res)

        m = len(result)
        for i in range(len(searchWord) - m):
            result.append([])

        return result


tests = [
    [
        ["enmjzunulkrjyxfugrpvkwoiwyxwgrweakhbswllbyziranhxkleggegegdailjgyteaghdqnjqdjfhyrapqmckvxgxmasnweej"],
        "yrnqunojmtporeofgldjntqv",
        [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    ],
    [["mobile","mouse","moneypot","monitor","mousepad"], "mouse", [
            ["mobile","moneypot","monitor"],
            ["mobile","moneypot","monitor"],
            ["mouse","mousepad"],
            ["mouse","mousepad"],
            ["mouse","mousepad"]
            ]
    ],
    [
        ["havana"], "havana",
        [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
    ],
    [
        ["bags","baggage","banner","box","cloths"], "bags",
        [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]
    ],
    [
        ["havana"], "tatiana",
        [[],[],[],[],[],[],[]]
    ]
]

run_functional_tests(Solution().suggestedProducts, tests)