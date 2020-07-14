"""
https://leetcode.com/problems/angle-between-hands-of-a-clock/
Given two numbers, hour and minutes. Return the smaller angle (in degrees) formed between the hour and the minute hand.



Example 1:



Input: hour = 12, minutes = 30
Output: 165
Example 2:



Input: hour = 3, minutes = 30
Output: 75
Example 3:



Input: hour = 3, minutes = 15
Output: 7.5
Example 4:

Input: hour = 4, minutes = 50
Output: 155
Example 5:

Input: hour = 12, minutes = 0
Output: 0


Constraints:

1 <= hour <= 12
0 <= minutes <= 59
Answers within 10^-5 of the actual value will be accepted as correct.
"""

"""
Runtime: 48 ms, faster than 11.92% of Python3 online submissions for Angle Between Hands of a Clock.
Memory Usage: 13.7 MB, less than 84.65% of Python3 online submissions for Angle Between Hands of a Clock.
"""
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        ma = minutes * 6.0
        ha = (hour + minutes / 60.0) * 30.0
        angle = abs(ma - ha)
        return min(angle, 360 - angle)


print(Solution().angleClock(12, 30))  # 165
print(Solution().angleClock(3, 30))  # 75
print(Solution().angleClock(3, 15))  # 7.5
print(Solution().angleClock(4, 50))  # 155
print(Solution().angleClock(12, 0))  # 0
