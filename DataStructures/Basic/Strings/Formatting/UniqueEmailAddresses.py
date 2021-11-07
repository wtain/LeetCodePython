"""
https://leetcode.com/explore/featured/card/september-leetcoding-challenge-2021/639/week-4-september-22nd-september-28th/3989/
https://leetcode.com/problems/unique-email-addresses/

Every valid email consists of a local name and a domain name, separated by the '@' sign. Besides lowercase letters, the email may contain one or more '.' or '+'.

For example, in "alice@leetcode.com", "alice" is the local name, and "leetcode.com" is the domain name.
If you add periods '.' between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name. Note that this rule does not apply to domain names.

For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.
If you add a plus '+' in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered. Note that this rule does not apply to domain names.

For example, "m.y+name@email.com" will be forwarded to "my@email.com".
It is possible to use both of these rules at the same time.

Given an array of strings emails where we send one email to each email[i], return the number of different addresses that actually receive mails.



Example 1:

Input: emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
Output: 2
Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails.
Example 2:

Input: emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
Output: 3


Constraints:

1 <= emails.length <= 100
1 <= emails[i].length <= 100
email[i] consist of lowercase English letters, '+', '.' and '@'.
Each emails[i] contains exactly one '@' character.
All local and domain names are non-empty.
Local names do not start with a '+' character.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 52 ms, faster than 72.69% of Python3 online submissions for Unique Email Addresses.
# Memory Usage: 14.5 MB, less than 31.63% of Python3 online submissions for Unique Email Addresses.
# class Solution:
#     def numUniqueEmails(self, emails: List[str]) -> int:
#
#         def canonize(email: str) -> str:
#             p = email.find('@')
#             name = email[:p]
#             domain = email[p+1:]
#             pp = name.find('+')
#             if pp >= 0:
#                 name = name[:pp]
#
#             name = name.replace('.', '')
#             return name + '@' + domain
#
#         return len({canonize(eml) for eml in emails})


# Runtime: 44 ms, faster than 95.70% of Python3 online submissions for Unique Email Addresses.
# Memory Usage: 14.4 MB, less than 31.63% of Python3 online submissions for Unique Email Addresses.
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:

        def canonize(email: str) -> str:
            name, domain = email.split('@')
            name = name.split('+')[0].replace('.', '')
            return name + '@' + domain

        return len({canonize(eml) for eml in emails})


tests = [
    [
        ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"],
        2
    ],
    [
        ["a@leetcode.com","b@leetcode.com","c@leetcode.com"],
        3
    ]
]

run_functional_tests(Solution().numUniqueEmails, tests)
