"""
https://leetcode.com/problems/crawler-log-folder/

The Leetcode file system keeps a log each time some user performs a change folder operation.

The operations are described below:

"../" : Move to the parent folder of the current folder. (If you are already in the main folder, remain in the same folder).
"./" : Remain in the same folder.
"x/" : Move to the child folder named x (This folder is guaranteed to always exist).
You are given a list of strings logs where logs[i] is the operation performed by the user at the ith step.

The file system starts in the main folder, then the operations in logs are performed.

Return the minimum number of operations needed to go back to the main folder after the change folder operations.



Example 1:



Input: logs = ["d1/","d2/","../","d21/","./"]
Output: 2
Explanation: Use this change folder operation "../" 2 times and go back to the main folder.
Example 2:



Input: logs = ["d1/","d2/","./","d3/","../","d31/"]
Output: 3
Example 3:

Input: logs = ["d1/","../","../","../"]
Output: 0


Constraints:

1 <= logs.length <= 103
2 <= logs[i].length <= 10
logs[i] contains lowercase English letters, digits, '.', and '/'.
logs[i] follows the format described in the statement.
Folder names consist of lowercase English letters and digits.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 40 ms, faster than 92.75% of Python3 online submissions for Crawler Log Folder.
# Memory Usage: 14.4 MB, less than 52.89% of Python3 online submissions for Crawler Log Folder.
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        cnt = 0
        for l in logs:
            if l == "../":
                if cnt > 0:
                    cnt -= 1
            elif l == "./":
                pass
            else:
                cnt += 1
        return cnt


tests = [
    [["d1/","d2/","../","d21/","./"], 2],
    [["d1/","d2/","./","d3/","../","d31/"], 3],
    [["d1/","../","../","../"], 0]
]

run_functional_tests(Solution().minOperations, tests)