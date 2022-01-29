"""
https://leetcode.com/explore/featured/card/june-leetcoding-challenge-2021/603/week-1-june-1st-june-7th/3767/
https://leetcode.com/problems/open-the-lock/

You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.

The lock initially starts at '0000', a string representing the state of the 4 wheels.

You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.



Example 1:

Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6
Explanation:
A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
because the wheels of the lock become stuck after the display becomes the dead end "0102".
Example 2:

Input: deadends = ["8888"], target = "0009"
Output: 1
Explanation:
We can turn the last wheel in reverse to move from "0000" -> "0009".
Example 3:

Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
Output: -1
Explanation:
We can't reach the target without getting stuck.
Example 4:

Input: deadends = ["0000"], target = "8888"
Output: -1


Constraints:

1 <= deadends.length <= 500
deadends[i].length == 4
target.length == 4
target will not be in the list deadends.
target and deadends[i] consist of digits only.
"""
from collections import deque
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# class Solution:
#     def openLock(self, deadends: List[str], target: str) -> int:
#         deadends = set(deadends)
#         if "0000" in deadends or target in deadends:
#             return -1
#         to_visit = []
#         heapq.heappush(to_visit, (0, "0000"))
#
#         visited = set()
#         while to_visit:
#             d, current = heapq.heappop(to_visit)
#             # print(current)
#             if current == target:
#                 return d
#             visited.add(current)
#             for i in range(4):
#                 current1 = current[:i] + chr(ord('0') + (ord(current[i]) + 1 - ord('0')) % 10) + current[i+1:]
#                 current2 = current[:i] + chr(ord('0') + (ord(current[i]) + 9 - ord('0')) % 10) + current[i + 1:]
#                 if current1 not in visited and current1 not in deadends and current1 not in to_visit:
#                     heapq.heappush(to_visit, (d+1, current1))
#                 if current2 not in visited and current2 not in deadends and current2 not in to_visit:
#                     heapq.heappush(to_visit, (d+1, current2))
#         return -1

# class Solution:
#     def openLock(self, deadends: List[str], target: str) -> int:
#         deadends = set([int(d) for d in deadends])
#         target = int(target)
#         if 0 in deadends or target in deadends:
#             return -1
#         to_visit = []
#         heapq.heappush(to_visit, (0, 0))
#
#         visited = set()
#         while to_visit:
#             d, current = heapq.heappop(to_visit)
#             # print(current)
#             if current == target:
#                 return d
#             visited.add(current)
#             power = 10000
#             for i in range(4):
#                 digit = current % power
#                 power //= 10
#                 digit //= power
#                 digit1 = (digit + 1) % 10
#                 digit2 = (digit + 9) % 10
#                 current0 = current - digit * power
#                 current1 = current0 + digit1 * power
#                 current2 = current0 + digit2 * power
#                 if current1 not in visited and current1 not in deadends and current1 not in to_visit:
#                     heapq.heappush(to_visit, (d+1, current1))
#                 if current2 not in visited and current2 not in deadends and current2 not in to_visit:
#                     heapq.heappush(to_visit, (d+1, current2))
#         return -1

# class Solution:
#     def openLock(self, deadends: List[str], target: str) -> int:
#         deadends = set([int(d) for d in deadends])
#         target = int(target)
#         if 0 in deadends or target in deadends:
#             return -1
#         to_visit1 = []
#         heapq.heappush(to_visit1, (0, 0))
#         to_visit2 = []
#         heapq.heappush(to_visit2, (0, target))
#
#         def step(current, d, to_visit, visited):
#             power = 10000
#             for i in range(4):
#                 digit = current % power
#                 power //= 10
#                 digit //= power
#                 digit1 = (digit + 1) % 10
#                 digit2 = (digit + 9) % 10
#                 current0 = current - digit * power
#                 current1 = current0 + digit1 * power
#                 current2 = current0 + digit2 * power
#                 if current1 not in visited and current1 not in deadends and current1 not in to_visit:
#                     heapq.heappush(to_visit, (d + 1, current1))
#                 if current2 not in visited and current2 not in deadends and current2 not in to_visit:
#                     heapq.heappush(to_visit, (d + 1, current2))
#
#         visited1, visited2 = {}, {}
#         while to_visit1 and to_visit2:
#             d1, current1 = heapq.heappop(to_visit1)
#             d2, current2 = heapq.heappop(to_visit2)
#             if current1 in visited2:
#                 return d1 + visited2[current1]
#             if current2 in visited1:
#                 return d2 + visited1[current2]
#             step(current1, d1, to_visit1, visited1)
#             step(current2, d2, to_visit2, visited2)
#             visited1[current1] = d1
#             visited2[current2] = d2
#
#         return -1


# Runtime: 572 ms, faster than 83.14% of Python3 online submissions for Open the Lock.
# Memory Usage: 14.9 MB, less than 98.56% of Python3 online submissions for Open the Lock.
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set([int(d) for d in deadends])
        target = int(target)
        if 0 in deadends or target in deadends:
            return -1

        def step(current, to_visit, visited):

            def neighbours(current):
                power = 10000
                for i in range(4):
                    digit = current % power
                    power //= 10
                    digit //= power
                    digit1 = (digit + 1) % 10
                    digit2 = (digit + 9) % 10
                    current0 = current - digit * power
                    yield current0 + digit1 * power
                    yield current0 + digit2 * power

            for nx in neighbours(current):
                if nx not in visited and nx not in deadends and nx not in to_visit:
                    to_visit.append(nx)
                    visited.add(nx)

        to_visit1, to_visit2 = deque([0]), deque([target])
        visited1, visited2 = set(), set()
        steps = 0
        while to_visit1 and to_visit2:
            for _ in range(len(to_visit1)):
                current = to_visit1.popleft()
                if current in to_visit2:
                    return steps
                step(current, to_visit1, visited1)
            steps += 1

            for _ in range(len(to_visit2)):
                current = to_visit2.popleft()
                if current in to_visit1:
                    return steps
                step(current, to_visit2, visited2)
            steps += 1

        return -1


tests = [
    [["5557","5553","5575","5535","5755","5355","7555","3555","6655","6455","4655","4455","5665","5445","5645","5465","5566","5544","5564","5546","6565","4545","6545","4565","5656","5454","5654","5456","6556","4554","4556","6554"], "5555", -1],

    [["4515","4184","9093","6799","6594","8484","8048","2886","5609","9801","7845","2631","3962","5601","5049","3916","7222","5699","3980","0814","2386","8880","4524","5329","6242","9184","5357","1288","5446","9771","5492","0361","8679","2808","1184","0228","6448","9083","5730","3379","9890","5713","2642","0772","0141","8765","4448","7356","5382","8138","0272","0802","7944","6245","1345","6805","6945","3377","6741","0945","0925","1471","1118","3708","8332","6887","9130","0851","5177","6032","1906","0767","5974","3592","4967","2620","7959","3805","4836","8641","9805","6141","1023","5291","6808","8466","6259","4084","8880","0043","7394","6369","0313","3293","5254","3827","1728","5495","5927","3680","5454","1305","3366","8174","2717","1069","3785","9181","6171","1462","8859","4333","5795","8883","9881","1287","6416","5760","4390","6260","9788","6191","1510","2553","0222","7214","5214","2943","9615","4492","5632","7093","5869","4177","3542","2433","3518","0105","5266","8033","3094","5221","2240","5874","3742","8687","5202","7932","4512","4106","0234","3863","8154","3076","7452","9081","1189","9847","6463","5475","2125","8509","8193","7885","0611","5479","4371","4168","8870","1871","0248","9145","7032","4093","1429","5415","5261","4482","7241","7373","6043","3156","1828","0741","4792","7642","8921","3979","8445","2710","5027","0658","6168","2434","4568","6790","5356","5643","8948","2831","2411","0043","4042","2651","6041","8557","8253","2634","0559","9254","9501","3215","0234","3108","3363","8688","1513","7747","3846","3542","6671","9677","4598","7304","8313","1036","5811","3279","7115","3157","7761","3256","3379","4807","2475","8576","3612","6157","1266","8635","9429","9897","8048","2654","3145","5204","8731","9154","6673","7213","0608","1045","6692","0452","3947","6488","0525","5531","0312","7363","5876","2713","0484","2299","3052","4392","0464","2755","7416","5527","1276","2077","3723","0142","0653","9606","0916","6882","6575","2024","6250","1711","3381","7703","1626","6859","1526","0514","6271","3438","2880","9874","5837","6547","4960","0712","9390","6207","1437","1131","2253","9308","0665","6334","6648","4997","1583","4590","1032","4791","8445","2328","8440","1369","2595","8853","0797","1989","3119","5246","5964","7501","2464","7716","2772","8257","6181","7195","5138","2185","8121","1753","5144","1776","3221","3883","5573","7268","7162","5602","3035","5843","1417","1823","9366","6477","0108","5719","8666","8901","7289","2498","2219","4520","2951","7929","5504","0797","7586","5306","2656","7479","6606","4227","7727","4449","2299","0142","5099","3898","7005","4275","3692","1905","5540","8365","8971","9541","7449","6146","2844","1026","7639","2614","0796","5920","4633","9839","9761","5748","5524","1332","5586","3026","9057","1498","8197","0692","7714","6334","7656","1649","2989","4393","6227","5183","6328","9864","5972","2203","7032","3643","2429","0981","4729","0501","9624","1464","2619","7712","6739","9171","0899","9731","1058","7006","1859","4002","5325","1039","0466","2060","4203","8816","8867","1797","9832","6489","4771","9789","0271","7684","6345","0825","9022","4285","8081","9435","0946","4466","6551","4722","3580","5484","5191","4582","0220","1580","0045","8701","3895","1795","0614","3118","4836","2101","2072","7090","9275","8715","1303","4864","1116","6102","2818","9196","1222","3481","1709","6145","2349","3395","5314","3404","4626","3770","7762","8413","7310","9659","0892","9920","7195","7049","7443","5505","3400","2275","0669","6024"], "4894", 11],

    [["0201","0101","0102","1212","2002"], "0202", 6],
    [["8888"], "0009", 1],
    [["8887","8889","8878","8898","8788","8988","7888","9888"], "8888", -1],
    [["0000"], "8888", -1]
]

run_functional_tests(Solution().openLock, tests)