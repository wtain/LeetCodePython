"""
https://leetcode.com/problems/largest-number-after-digit-swaps-by-parity/

You are given a positive integer num. You may swap any two digits of num that have the same parity (i.e. both odd digits or both even digits).

Return the largest possible value of num after any number of swaps.



Example 1:

Input: num = 1234
Output: 3412
Explanation: Swap the digit 3 with the digit 1, this results in the number 3214.
Swap the digit 2 with the digit 4, this results in the number 3412.
Note that there may be other sequences of swaps but it can be shown that 3412 is the largest possible number.
Also note that we may not swap the digit 4 with the digit 1 since they are of different parities.
Example 2:

Input: num = 65875
Output: 87655
Explanation: Swap the digit 8 with the digit 6, this results in the number 85675.
Swap the first digit 5 with the digit 7, this results in the number 87655.
Note that there may be other sequences of swaps but it can be shown that 87655 is the largest possible number.


Constraints:

1 <= num <= 109
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 42 ms, faster than 54.92% of Python3 online submissions for Largest Number After Digit Swaps by Parity.
# Memory Usage: 13.9 MB, less than 77.62% of Python3 online submissions for Largest Number After Digit Swaps by Parity.
class Solution:
    def largestInteger(self, num: int) -> int:
        even = []
        odd = []
        even_idx = []
        i = 0
        while num:
            d = num % 10
            num //= 10
            if d % 2:
                odd.append(d)
                even_idx.append(False)
            else:
                even.append(d)
                even_idx.append(True)
            i += 1
        even.sort()
        odd.sort()
        result = 0
        i1, i2 = 0, 0
        mul = 1
        for is_even in even_idx:
            if is_even:
                result += mul * even[i1]
                i1 += 1
            else:
                result += mul * odd[i2]
                i2 += 1
            mul *= 10
        return result


tests = [
    [1234, 3412],
    [65875, 87655]
]

run_functional_tests(Solution().largestInteger, tests)
