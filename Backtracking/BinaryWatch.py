"""
https://leetcode.com/problems/binary-watch/
A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).

Each LED represents a zero or one, with the least significant bit on the right.


For example, the above binary watch reads "3:25".

Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the watch could represent.

Example:

Input: n = 1
Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
Note:
The order of output does not matter.
The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid, it should be "10:02".
"""
from typing import List

"""
Runtime: 32 ms, faster than 75.95% of Python3 online submissions for Binary Watch.
Memory Usage: 13.9 MB, less than 35.35% of Python3 online submissions for Binary Watch.
"""
class Solution:

    def bitcount(self, n: int) -> int:
        result = 0
        mask = 1
        for i in range(8):
            if n & mask:
                result += 1
            mask <<= 1
        return result

    def readBinaryWatch(self, num: int) -> List[str]:
        result = []
        for h in range(12):
            bh = self.bitcount(h)
            if num - bh < 0:
                continue
            for m in range(60):
                bm = self.bitcount(m)
                if bh + bm == num:
                    result.append(f'{h}:{m:02}')
        return result


print(Solution().readBinaryWatch(1))  # ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
