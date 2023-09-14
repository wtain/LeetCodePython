"""
https://leetcode.com/problems/reconstruct-itinerary/description/?envType=daily-question&envId=2023-09-14

You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.



Example 1:


Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output: ["JFK","MUC","LHR","SFO","SJC"]
Example 2:


Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.


Constraints:

1 <= tickets.length <= 300
tickets[i].length == 2
fromi.length == 3
toi.length == 3
fromi and toi consist of uppercase English letters.
fromi != toi
"""
from collections import defaultdict
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# https://leetcode.com/problems/reconstruct-itinerary/submissions/359394155/?envType=daily-question&envId=2023-09-14
# Runtime
# Details
# 87ms
# Beats 68.52%of users with Python3
# Memory
# Details
# 16.95MB
# Beats 66.53%of users with Python3
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        def get_tickets():
            tmap = defaultdict(lambda: defaultdict(int))
            for src, dst in tickets:
                tmap[src][dst] += 1
            return tmap

        current = "JFK"
        result = [current]
        tmap = get_tickets()

        def impl():
            if len(result) == len(tickets) + 1:
                return True
            current = result[-1]
            for dst in sorted(tmap[current]):
                if tmap[current][dst] == 0:
                    continue
                result.append(dst)
                tmap[current][dst] -= 1
                if impl():
                    return True
                tmap[current][dst] += 1
                result.pop()
            return False

        impl()

        return result
    
    
tests = [
    [[["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]], ["JFK","MUC","LHR","SFO","SJC"]],
    [[["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]], ["JFK","ATL","JFK","SFO","ATL","SFO"]],
]

run_functional_tests(Solution().findItinerary, tests)
