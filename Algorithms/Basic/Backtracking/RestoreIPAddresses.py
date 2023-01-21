"""
https://leetcode.com/problems/restore-ip-addresses/description/

A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s. You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.



Example 1:

Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]
Example 2:

Input: s = "0000"
Output: ["0.0.0.0"]
Example 3:

Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]


Constraints:

1 <= s.length <= 20
s consists of digits only.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 28 ms
# Beats
# 97.86%
# Memory
# 13.8 MB
# Beats
# 99.19%
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        results = []

        def is_valid_component(s: str) -> bool:
            if not s:
                return False
            if s[0] == '0' and len(s) > 1:
                return False
            return 0 <= int(s) <= 255

        def impl(s: str, dots: int, prefix: str):
            nonlocal results
            if not dots:
                if is_valid_component(s):
                    results.append(prefix + s)
                return
            for i in range(1, len(s)+1):
                s1 = s[:i]
                if not is_valid_component(s1):
                    break
                impl(s[i:], dots-1, prefix + s1 + '.')

        impl(s, 3, "")

        return results


tests = [
    ["25525511135", ["255.255.11.135","255.255.111.35"]],
    ["0000", ["0.0.0.0"]],
    ["101023", ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]],
]

run_functional_tests(Solution().restoreIpAddresses, tests)
