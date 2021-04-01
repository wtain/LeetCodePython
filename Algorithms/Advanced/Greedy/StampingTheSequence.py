"""
https://leetcode.com/explore/featured/card/march-leetcoding-challenge-2021/592/week-5-march-29th-march-31st/3691/
https://leetcode.com/problems/stamping-the-sequence/

You want to form a target string of lowercase letters.

At the beginning, your sequence is target.length '?' marks.  You also have a stamp of lowercase letters.

On each turn, you may place the stamp over the sequence, and replace every letter in the sequence with the corresponding letter from the stamp.  You can make up to 10 * target.length turns.

For example, if the initial sequence is "?????", and your stamp is "abc",  then you may make "abc??", "?abc?", "??abc" in the first turn.  (Note that the stamp must be fully contained in the boundaries of the sequence in order to stamp.)

If the sequence is possible to stamp, then return an array of the index of the left-most letter being stamped at each turn.  If the sequence is not possible to stamp, return an empty array.

For example, if the sequence is "ababc", and the stamp is "abc", then we could return the answer [0, 2], corresponding to the moves "?????" -> "abc??" -> "ababc".

Also, if the sequence is possible to stamp, it is guaranteed it is possible to stamp within 10 * target.length moves.  Any answers specifying more than this number of moves will not be accepted.



Example 1:

Input: stamp = "abc", target = "ababc"
Output: [0,2]
([1,0,2] would also be accepted as an answer, as well as some other answers.)
Example 2:

Input: stamp = "abca", target = "aabcaca"
Output: [3,0,1]


Note:

1 <= stamp.length <= target.length <= 1000
stamp and target only contain lowercase letters.
"""
import collections
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 2196 ms, faster than 9.00% of Python3 online submissions for Stamping The Sequence.
# Memory Usage: 14.7 MB, less than 37.00% of Python3 online submissions for Stamping The Sequence.
# class Solution:
#     def movesToStamp(self, stamp: str, target: str) -> List[int]:
#         result = []
#         n = len(target)
#         m = len(stamp)
#         t = [ci for ci in target]
#         covered = 0
#         num_stamps = 0
#         num_stamps_max = 10 * n
#         while covered < n:
#             if num_stamps == num_stamps_max:
#                 return []
#             covered_prev = covered
#             for i in range(n-m+1):
#                 match = True
#                 eliminating = 0
#                 for j in range(m):
#                     if t[i+j] != '?' and t[i+j] != stamp[j]:
#                         match = False
#                         break
#                     if t[i+j] != '?':
#                         eliminating += 1
#                 if match and eliminating > 0:
#                     result.append(i)
#                     for j in range(m):
#                         if t[i+j] != '?':
#                             t[i+j] = '?'
#                             covered += 1
#                     # print(t)
#                     num_stamps += 1
#                     break
#             if covered_prev == covered:
#                 return []
#         return [r for r in reversed(result)]


# Runtime: 196 ms, faster than 73.00% of Python3 online submissions for Stamping The Sequence.
# Memory Usage: 18.2 MB, less than 9.00% of Python3 online submissions for Stamping The Sequence.
class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        result = []
        n = len(target)
        m = len(stamp)
        q = collections.deque()
        done = [False] * n
        A = []
        for i in range(n - m + 1):
            made, todo = set(), set()
            for j, c in enumerate(stamp):
                a = target[i+j]
                if a == c:
                    made.add(i+j)
                else:
                    todo.add(i+j)
            A.append((made, todo))

            if not todo:
                result.append(i)
                for j in range(i, i+m):
                    if not done[j]:
                        q.append(j)
                        done[j] = True

        while q:
            i = q.popleft()
            for j in range(max(0, i-m+1), min(n-m, i) + 1):
                if i in A[j][1]:
                    A[j][1].discard(i)
                    if not A[j][1]:
                        result.append(j)
                        for x in A[j][0]:
                            if not done[x]:
                                q.append(x)
                                done[x] = True

        return result[::-1] if all(done) else []



tests = [
    ("aye", "eyeye", []),
    ("abc", "ababc", [0, 2]), # [1, 0, 2]
    ("abca", "aabcaca", [3,0,1])
]

run_functional_tests(Solution().movesToStamp, tests)