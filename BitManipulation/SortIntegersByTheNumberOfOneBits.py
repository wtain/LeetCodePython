"""
https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/

Given an integer array arr. You have to sort the integers in the array in ascending order by the number of 1's in their binary representation and in case of two or more integers have the same number of 1's you have to sort them in ascending order.

Return the sorted array.



Example 1:

Input: arr = [0,1,2,3,4,5,6,7,8]
Output: [0,1,2,4,8,3,5,6,7]
Explantion: [0] is the only integer with 0 bits.
[1,2,4,8] all have 1 bit.
[3,5,6] have 2 bits.
[7] has 3 bits.
The sorted array by bits is [0,1,2,4,8,3,5,6,7]
Example 2:

Input: arr = [1024,512,256,128,64,32,16,8,4,2,1]
Output: [1,2,4,8,16,32,64,128,256,512,1024]
Explantion: All integers have 1 bit in the binary representation, you should just sort them in ascending order.
Example 3:

Input: arr = [10000,10000]
Output: [10000,10000]
Example 4:

Input: arr = [2,3,5,7,11,13,17,19]
Output: [2,3,5,17,7,11,13,19]
Example 5:

Input: arr = [10,100,1000,10000]
Output: [10,100,10000,1000]


Constraints:

1 <= arr.length <= 500
0 <= arr[i] <= 10^4
"""
from typing import List


# Runtime: 96 ms, faster than 22.43% of Python3 online submissions for Sort Integers by The Number of 1 Bits.
# Memory Usage: 14.5 MB, less than 52.47% of Python3 online submissions for Sort Integers by The Number of 1 Bits.
# class Solution:
#     def sortByBits(self, arr: List[int]) -> List[int]:
#
#         def countBits(x: int) -> int:
#             cnt = 0
#             while x:
#                 cnt += x & 1
#                 x >>= 1
#             return cnt
#
#         return [x for b, x in sorted([(countBits(x), x) for x in arr])]

"""
10 = 1010
10-1 = 1001
=>
1000
0111

"""

# Runtime: 76 ms, faster than 47.53% of Python3 online submissions for Sort Integers by The Number of 1 Bits.
# Memory Usage: 14.6 MB, less than 19.34% of Python3 online submissions for Sort Integers by The Number of 1 Bits.
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:

        def countBits(x: int) -> int:
            cnt = 0
            while x:
                x &= x-1
                cnt += 1
            return cnt

        return [x for b, x in sorted([(countBits(x), x) for x in arr])]

tests = [
    ([0,1,2,3,4,5,6,7,8], [0,1,2,4,8,3,5,6,7]),
    ([1024,512,256,128,64,32,16,8,4,2,1], [1,2,4,8,16,32,64,128,256,512,1024]),
    ([10000,10000], [10000,10000]),
    ([2,3,5,7,11,13,17,19], [2,3,5,17,7,11,13,19]),
    ([10,100,1000,10000], [10,100,10000,1000])
]

for test in tests:
    result = Solution().sortByBits(test[0])
    if result == test[1]:
        print("PASS")
    else:
        print("FAIL - " + str(result))