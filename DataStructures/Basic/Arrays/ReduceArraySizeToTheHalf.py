"""
https://leetcode.com/explore/featured/card/july-leetcoding-challenge-2021/608/week-1-july-1st-july-7th/3804/
https://leetcode.com/problems/reduce-array-size-to-the-half/

Given an array arr.  You can choose a set of integers and remove all the occurrences of these integers in the array.

Return the minimum size of the set so that at least half of the integers of the array are removed.



Example 1:

Input: arr = [3,3,3,3,5,5,5,2,2,7]
Output: 2
Explanation: Choosing {3,7} will make the new array [5,5,5,2,2] which has size 5 (i.e equal to half of the size of the old array).
Possible sets of size 2 are {3,5},{3,2},{5,2}.
Choosing set {2,7} is not possible as it will make the new array [3,3,3,3,5,5,5] which has size greater than half of the size of the old array.
Example 2:

Input: arr = [7,7,7,7,7,7]
Output: 1
Explanation: The only possible set you can choose is {7}. This will make the new array empty.
Example 3:

Input: arr = [1,9]
Output: 1
Example 4:

Input: arr = [1000,1000,3,7]
Output: 1
Example 5:

Input: arr = [1,2,3,4,5,6,7,8,9,10]
Output: 5


Constraints:

1 <= arr.length <= 10^5
arr.length is even.
1 <= arr[i] <= 10^5
"""
from collections import Counter
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 680 ms, faster than 27.51% of Python3 online submissions for Reduce Array Size to The Half.
# Memory Usage: 50.1 MB, less than 5.73% of Python3 online submissions for Reduce Array Size to The Half.
# class Solution:
#     def minSetSize(self, arr: List[int]) -> int:
#         n = len(arr)
#         n2 = n // 2
#         c = Counter(arr)
#         c = [-v for v in cumsum(sorted([-c[k] for k in c.keys()]))]
#         return bisect.bisect_left(c, n2) + 1


# Runtime: 532 ms, faster than 98.17% of Python3 online submissions for Reduce Array Size to The Half.
# Memory Usage: 30.6 MB, less than 94.65% of Python3 online submissions for Reduce Array Size to The Half.
# https://leetcode.com/problems/reduce-array-size-to-the-half/discuss/1319416/C%2B%2BJavaPython-HashMap-and-Sort-then-Bucket-Sort-O(N)-Clean-and-Concise
# class Solution:
#     def minSetSize(self, arr: List[int]) -> int:
#         n = len(arr)
#         n2 = n // 2
#         c = Counter(arr)
#         freqs = sorted(list(c.values()))
#         result, removed = 0, 0
#         while removed < n2:
#             result += 1
#             removed += freqs.pop()
#         return result


# Runtime: 568 ms, faster than 82.54% of Python3 online submissions for Reduce Array Size to The Half.
# Memory Usage: 31.3 MB, less than 49.44% of Python3 online submissions for Reduce Array Size to The Half.
# https://leetcode.com/problems/reduce-array-size-to-the-half/discuss/1319416/C%2B%2BJavaPython-HashMap-and-Sort-then-Bucket-Sort-O(N)-Clean-and-Concise
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        n2 = n // 2
        c = Counter(arr)
        freqs = list(c.values())
        max_freq = max(freqs)
        bucket = [0] * (max_freq+1)
        for freq in freqs:
            bucket[freq] += 1

        result, removed = 0, 0
        fr = max_freq
        while removed < n2:
            result += 1
            while bucket[fr] == 0:
                fr -= 1
            removed += fr
            bucket[fr] -= 1
        return result


tests = [
    [[3,3,3,3,5,5,5,2,2,7], 2],
    [[7,7,7,7,7,7], 1],
    [[1,9], 1],
    [[1000,1000,3,7], 1],
    [[1,2,3,4,5,6,7,8,9,10], 5]
]

run_functional_tests(Solution().minSetSize, tests)