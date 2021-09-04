"""
https://leetcode.com/problems/reverse-string/
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.



Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""
from typing import List


"""
Runtime: 308 ms, faster than 11.99% of Python3 online submissions for Reverse Strings.
Memory Usage: 18.3 MB, less than 52.77% of Python3 online submissions for Reverse Strings.
"""
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        l = 0
        r = n-1
        while l < r:
            t = s[l]
            s[l] = s[r]
            s[r] = t
            l += 1
            r -= 1


s1 = ["h","e","l","l","o"]
Solution().reverseString(s1)
print(s1)

s2 = ["H","a","n","n","a","h"]
Solution().reverseString(s2)
print(s2)
