"""
https://leetcode.com/problems/top-k-frequent-elements/

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.



Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]


Constraints:

1 <= nums.length <= 105
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.


Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""
import heapq
import random
from collections import Counter
from typing import List

from Common.Helpers.ResultComparators import compareSets
from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 122 ms, faster than 68.56% of Python3 online submissions for Top K Frequent Elements.
# Memory Usage: 18.6 MB, less than 68.16% of Python3 online submissions for Top K Frequent Elements.
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         c = Counter(nums)
#         h = []
#         for key in c:
#             heapq.heappush(h, [c[key], key])
#             if len(h) > k:
#                 heapq.heappop(h)
#         return [key for c, key in h]


# Runtime: 173 ms, faster than 27.19% of Python3 online submissions for Top K Frequent Elements.
# Memory Usage: 18.7 MB, less than 40.43% of Python3 online submissions for Top K Frequent Elements.
# https://leetcode.com/problems/top-k-frequent-elements/solution/
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        uniq = list(cnt.keys())

        def partition(l, r, pivot_index) -> int:
            pivot_freq = cnt[uniq[pivot_index]]
            uniq[pivot_index], uniq[r] = uniq[r], uniq[pivot_index]
            store_index = l
            for i in range(l, r):
                if cnt[uniq[i]] < pivot_freq:
                    uniq[store_index], uniq[i] = uniq[i], uniq[store_index]
                    store_index += 1
            uniq[r], uniq[store_index] = uniq[store_index], uniq[r]
            return store_index

        def quickselect(l, r, k_smallest) -> None:
            if l == r:
                return
            pivot_index = random.randint(l, r)
            pivot_index = partition(l, r, pivot_index)
            if k_smallest == pivot_index:
                return
            elif k_smallest < pivot_index:
                quickselect(l, pivot_index-1, k_smallest)
            else:
                quickselect(pivot_index+1, r, k_smallest)

        n = len(uniq)
        quickselect(0, n-1, n-k)
        return uniq[n-k:]


tests = [
    [[1,1,1,2,2,3], 2, [1, 2]],
    [[1], 1, [1]]
]

run_functional_tests(Solution().topKFrequent, tests, custom_check=compareSets)
