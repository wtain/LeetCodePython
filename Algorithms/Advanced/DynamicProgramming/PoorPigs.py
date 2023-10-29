"""
https://leetcode.com/problems/poor-pigs/

There are buckets buckets of liquid, where exactly one of the buckets is poisonous. To figure out which one is poisonous, you feed some number of (poor) pigs the liquid to see whether they will die or not. Unfortunately, you only have minutesToTest minutes to determine which bucket is poisonous.

You can feed the pigs according to these steps:

Choose some live pigs to feed.
For each pig, choose which buckets to feed it. The pig will consume all the chosen buckets simultaneously and will take no time.
Wait for minutesToDie minutes. You may not feed any other pigs during this time.
After minutesToDie minutes have passed, any pigs that have been fed the poisonous bucket will die, and all others will survive.
Repeat this process until you run out of time.
Given buckets, minutesToDie, and minutesToTest, return the minimum number of pigs needed to figure out which bucket is poisonous within the allotted time.



Example 1:

Input: buckets = 1000, minutesToDie = 15, minutesToTest = 60
Output: 5
Example 2:

Input: buckets = 4, minutesToDie = 15, minutesToTest = 15
Output: 2
Example 3:

Input: buckets = 4, minutesToDie = 15, minutesToTest = 30
Output: 2


Constraints:

1 <= buckets <= 1000
1 <= minutesToDie <= minutesToTest <= 100


What if you only have one shot? Eg. 4 buckets, 15 mins to die, and 15 mins to test.

How many states can we generate with x pigs and T tests?

Find minimum x such that (T+1)^x >= N
"""
import math

from Common.ObjectTestingUtils import run_functional_tests


# WRONG
# Runtime: 33 ms, faster than 90.51% of Python3 online submissions for Poor Pigs.
# Memory Usage: 13.9 MB, less than 74.45% of Python3 online submissions for Poor Pigs.
# https://leetcode.com/problems/poor-pigs/discuss/2386933/one-line-solution
# class Solution:
#     def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
#         return math.ceil(math.log(buckets)/math.log(1+minutesToTest/minutesToDie))


# Runtime
# Details
# 27ms
# Beats 99.20%of users with Python3
# Memory
# Details
# 16.13MB
# Beats 74.40%of users with Python3
# https://leetcode.com/problems/poor-pigs/solutions/4220289/c-log2-1-line/?envType=daily-question&envId=2023-10-29
class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        return math.ceil(math.log2(buckets)/math.log2(1+minutesToTest/minutesToDie))


tests = [
    [1000, 15, 60, 5],
    [4, 15, 15, 2],
    [4, 15, 30, 2],
    [125,1,4,3],
]

run_functional_tests(Solution().poorPigs, tests)
