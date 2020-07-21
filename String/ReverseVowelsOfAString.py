"""
https://leetcode.com/problems/reverse-vowels-of-a-string/
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"
Note:
The vowels does not include the letter "y".
"""

"""
class Solution:
    def reverseVowels(self, s: str) -> str:
        n = len(s)
        vowels = {'a', 'o', 'i', 'u', 'e', 'A', 'O', 'I', 'U', 'E'}
        head = ""
        tail = ""

        l = 0
        r = n - 1

        def isVowel(c: chr) -> bool:
            return c in vowels

        def nextVovel(i: int, d: int) -> (int, str):
            res = ""
            while l <= i <= r and not isVowel(s[i]):
                res += s[i]
                i += d
            return i, res

        while l <= r:
            l, resl = nextVovel(l, 1)
            head += resl

            f = l < r

            r, resr = nextVovel(r, -1)
            tail += resr

            if l >= r:
                if f:
                    head += s[l]
                    l += 1
                break
            # t = s[l]
            # s[l] = s[r]
            # s[r] = t
            tail += s[l]
            l += 1
            head += s[r]
            r -= 1
        return head + tail[::-1]
"""

"""
Runtime: 92 ms, faster than 25.32% of Python3 online submissions for Reverse Vowels of a String.
Memory Usage: 14.8 MB, less than 52.46% of Python3 online submissions for Reverse Vowels of a String.
"""
class Solution:
    def reverseVowels(self, s: str) -> str:
        n = len(s)
        vowels = {'a', 'o', 'i', 'u', 'e', 'A', 'O', 'I', 'U', 'E'}
        head = ""
        tail = ""

        arr = list(s)

        l = 0
        r = n - 1

        def isVowel(c: chr) -> bool:
            return c in vowels

        def nextVovel(i: int, d: int) -> int:
            while l <= i <= r and not isVowel(arr[i]):
                i += d
            return i

        while l <= r:
            l = nextVovel(l, 1)
            r = nextVovel(r, -1)
            if l > r:
                break
            t = arr[l]
            arr[l] = arr[r]
            arr[r] = t
            l += 1
            r -= 1
        return "".join(arr)


print(Solution().reverseVowels(".a"))  # ".a"
print(Solution().reverseVowels("a."))  # "a."
print(Solution().reverseVowels(" "))  # " "
print(Solution().reverseVowels("hello"))  # "holle"
print(Solution().reverseVowels("leetcode"))  # "leotcede"

