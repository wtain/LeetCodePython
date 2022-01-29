"""
https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

Given an integer array nums, return the maximum result of nums[i] XOR nums[j], where 0 <= i <= j < n.



Example 1:

Input: nums = [3,10,5,25,2,8]
Output: 28
Explanation: The maximum result is 5 XOR 25 = 28.
Example 2:

Input: nums = [14,70,53,83,49,91,36,80,92,51,66,70]
Output: 127


Constraints:

1 <= nums.length <= 2 * 105
0 <= nums[i] <= 231 - 1
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 728 ms, faster than 93.80% of Python3 online submissions for Maximum XOR of Two Numbers in an Array.
# Memory Usage: 33.7 MB, less than 75.54% of Python3 online submissions for Maximum XOR of Two Numbers in an Array.
# https://leetcode.com/submissions/detail/192266786/
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:

        def impl(l: List[int], r: List[int], bit: int) -> int:
            if len(l) == 1 and len(r) == 1:
                return l[0] ^ r[0]
            if len(l) == 1 and len(r) == 0:
                return 0
            if len(l) == 0 and len(r) == 1:
                return 0
            if len(l) == 0 and len(r) == 0:
                return 0
            mask = 1 << bit

            def split_arr(arr: List[int], mask: int) -> (List[int], List[int]):
                al, ar = [], []
                for v in arr:
                    if v & mask:
                        ar.append(v)
                    else:
                        al.append(v)
                return al, ar

            if l and r:
                ll, lr = split_arr(l, mask)
                rl, rr = split_arr(r, mask)
                if not lr and not rr or not ll and not rl:
                    return impl(l, r, bit-1)
                return max(impl(lr, rl, bit-1), impl(ll, rr, bit-1))

            v = r if r else l
            vl, vr = split_arr(v, mask)
            return impl(vl, vr, bit-1)

        l, r = [], []
        seen = set()
        for v in nums:
            if v in seen:
                continue
            seen.add(v)
            l.append(v)
        return impl(l, r, 31)


tests = [
    [[3,10,5,25,2,8], 28],
    [[14,70,53,83,49,91,36,80,92,51,66,70], 127]
]

run_functional_tests(Solution().findMaximumXOR, tests)
