"""
https://leetcode.com/problems/make-sum-divisible-by-p/

Given an array of positive integers nums, remove the smallest subarray (possibly empty) such that the sum of the remaining elements is divisible by p. It is not allowed to remove the whole array.

Return the length of the smallest subarray that you need to remove, or -1 if it's impossible.

A subarray is defined as a contiguous block of elements in the array.



Example 1:

Input: nums = [3,1,4,2], p = 6
Output: 1
Explanation: The sum of the elements in nums is 10, which is not divisible by 6. We can remove the subarray [4], and the sum of the remaining elements is 6, which is divisible by 6.
Example 2:

Input: nums = [6,3,5,2], p = 9
Output: 2
Explanation: We cannot remove a single element to get a sum divisible by 9. The best way is to remove the subarray [5,2], leaving us with [6,3] with sum 9.
Example 3:

Input: nums = [1,2,3], p = 3
Output: 0
Explanation: Here the sum is 6. which is already divisible by 3. Thus we do not need to remove anything.
Example 4:

Input: nums = [1,2,3], p = 7
Output: -1
Explanation: There is no way to remove a subarray in order to get a sum divisible by 7.
Example 5:

Input: nums = [1000000000,1000000000,1000000000], p = 3
Output: 0


Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
1 <= p <= 109
"""
from typing import List


# Runtime: 608 ms, faster than 19.68% of Python3 online submissions for Make Sum Divisible by P.
# Memory Usage: 32.4 MB, less than 88.95% of Python3 online submissions for Make Sum Divisible by P.
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        S = sum(nums) % p
        # longest = 0
        shortest = n+1
        mods = {0: -1}
        Sp = 0
        for i in range(n):
            nums[i] = nums[i] % p
            Sp += nums[i]
            Sp %= p
            # print(Sp)
            #if Sp == 0:
                #longest = i+1
                #shortest = min(shortest, n - i - 1)

            #if Sp == S:
                #longest = i+1
                #shortest = min(shortest, i)



            # diff = abs(Sp - S)
            # t = (p - diff) % p
            t = (Sp + p - S) % p
            #t = (p + Sp - S) % p
            # t = (Sp - S) % p
            # print(t)
            mods[Sp] = i
            if mods.get(t) is not None:
                idx = mods.get(t)
                # longest = max(longest, n-(i-idx))
                shortest = min(shortest, i - idx)
                # print(t, shortest)

        # return -1 if longest == 0 else n - longest
        return -1 if shortest >= n else shortest


tests = [
    ([1,2,3], 7, -1),

    # (),

    ([19,11,14,18,4,7,1,4,23,19,8,10,6,3], 26, 3),

    # (),

    ([19,21,7], 26, 1),

    ([19,47,7], 26, 1),

    ([19,11,14,18,7], 26, 3),

    # (),

    ([19,11,14,18,4,7,1,4,23,19,8,10,6,3], 26, 3),

    # (),

    ([26,19,11,14,18,4,7,1,30,23,19,8,10,6,26,3], 26, 3),

    ([3,1,4,2], 6, 1),
    ([6,3,5,2], 9, 2),
    ([1,2,3], 3, 0),
    ([1,2,3], 7, -1),
    ([1000000000,1000000000,1000000000], 3, 0)
]

for test in tests:
    if len(test) == 0:
        break
    result = Solution().minSubarray(test[0], test[1])
    if result == test[2]:
        print("PASS")
    else:
        print("FAIL - " + str(result))