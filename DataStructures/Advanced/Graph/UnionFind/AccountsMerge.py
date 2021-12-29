"""
https://leetcode.com/problems/accounts-merge/

Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.



Example 1:

Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
Explanation:
The first and second John's are the same person as they have the common email "johnsmith@mail.com".
The third John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'],
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
Example 2:

Input: accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
Output: [["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]


Constraints:

1 <= accounts.length <= 1000
2 <= accounts[i].length <= 10
1 <= accounts[i][j] <= 30
accounts[i][0] consists of English letters.
accounts[i][j] (for j > 0) is a valid email.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests
from Common.ResultComparators import compareSets


# WRONG
# class Solution:
#     def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
#         emails = dict()
#         n = len(accounts)
#         p = [i for i in range(n)]
#         result = [set() for _ in range(n)]
#         for nameid, account in enumerate(accounts):
#             name = account[0]
#             for email in account[1:]:
#                 if email in emails:
#                     p[nameid] = emails[email]
#                 else:
#                     emails[email] = nameid
#                 result[p[nameid]].add(email)
#         for i in range(n):
#             parent = p[i]
#             emails = result[i]
#             result[i] = set()
#             while parent != p[parent]:
#                 emails = emails.union(result[p[parent]])
#                 parent = p[parent]
#             result[i] = emails
#             p[i] = parent
#         rv = []
#         for i in range(n):
#             if result[i]:
#                 rv.append([accounts[i][0]] + sorted(list(result[i])))
#         return rv


# Runtime: 272 ms, faster than 36.19% of Python3 online submissions for Accounts Merge.
# Memory Usage: 18.4 MB, less than 68.22% of Python3 online submissions for Accounts Merge.
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_owners = dict()
        n = len(accounts)
        p = [i for i in range(n)]
        result = [set() for _ in range(n)]

        def get(owner):
            while owner != p[owner]:
                owner = p[owner]
            return owner

        def connect(owner1, owner2):
            owner1 = get(owner1)
            owner2 = get(owner2)
            if owner1 == owner2:
                return
            owner1, owner2 = sorted([owner1, owner2])
            result[owner1] = result[owner1].union(result[owner2])
            result[owner2] = set()
            p[owner2] = owner1

        for nameid, account in enumerate(accounts):
            result[nameid] = set(account[1:])
            for email in account[1:]:
                if email not in email_owners:
                    email_owners[email] = nameid
            for email in account[1:]:
                if email in email_owners:
                    connect(nameid, email_owners[email])

        def transform_result(result):
            rv = []
            for i in range(n):
                if result[i]:
                    rv.append([accounts[i][0]] + sorted(list(result[i])))
            return rv

        return transform_result(result)


tests = [
    [
        [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]],
        [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
    ],
    [
        [["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe1@m.co"], ["Kevin", "Kevin3@m.co", "Kevin5@m.co", "Kevin0@m.co"], ["Ethan", "Ethan5@m.co", "Ethan4@m.co", "Ethan0@m.co"], ["Hanzo", "Hanzo3@m.co", "Hanzo1@m.co", "Hanzo0@m.co"],
         ["Fern", "Fern5@m.co", "Fern1@m.co", "Fern0@m.co"]],
        [["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]
    ],
    [
        [["David","David0@m.co","David4@m.co","David3@m.co"],["David","David5@m.co","David5@m.co","David0@m.co"],["David","David1@m.co","David4@m.co","David0@m.co"],["David","David0@m.co","David1@m.co","David3@m.co"],["David","David4@m.co","David1@m.co","David3@m.co"]],
        [["David","David0@m.co","David1@m.co","David3@m.co","David4@m.co","David5@m.co"]]
    ]
]

run_functional_tests(Solution().accountsMerge, tests, custom_check=compareSets)
