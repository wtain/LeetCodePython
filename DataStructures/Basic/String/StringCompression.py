"""
https://leetcode.com/problems/string-compression/
Given an array of characters, compress it in-place.

The length after compression must always be smaller than or equal to the original array.

Every element of the array should be a character (not int) of length 1.

After you are done modifying the input array in-place, return the new length of the array.


Follow up:
Could you solve it using only O(1) extra space?


Example 1:

Input:
["a","a","b","b","c","c","c"]

Output:
Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]

Explanation:
"aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".


Example 2:

Input:
["a"]

Output:
Return 1, and the first 1 characters of the input array should be: ["a"]

Explanation:
Nothing is replaced.


Example 3:

Input:
["a","b","b","b","b","b","b","b","b","b","b","b","b"]

Output:
Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].

Explanation:
Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb" is replaced by "b12".
Notice each digit has it's own entry in the array.


Note:

All characters have an ASCII value in [35, 126].
1 <= len(chars) <= 1000.
"""
from typing import List


"""
Runtime: 60 ms, faster than 74.33% of Python3 online submissions for Strings Compression.
Memory Usage: 13.8 MB, less than 83.58% of Python3 online submissions for Strings Compression.
"""
class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        i = 0
        j = 0
        while i < n:
            i0 = i
            while i < n and chars[i] == chars[i0]:
                i += 1
            cnt = i - i0
            chars[j] = chars[i0]
            j += 1
            if cnt > 1:
                cnts = str(cnt)
                for c in cnts:
                    chars[j] = c
                    j += 1
        return j


l1 = ["a","a","b","b","c","c","c"]
del l1[Solution().compress(l1):]
print(l1)  # ["a","2","b","2","c","3"]

l2 = ["a"]
del l2[Solution().compress(l2):]
print(l2)  # ["a"]

l3 = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
del l3[Solution().compress(l3):]
print(l3)  # ["a","b","1","2"]
