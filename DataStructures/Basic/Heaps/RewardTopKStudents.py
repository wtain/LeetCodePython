"""
https://leetcode.com/problems/reward-top-k-students/

You are given two string arrays positive_feedback and negative_feedback, containing the words denoting positive and negative feedback, respectively. Note that no word is both positive and negative.

Initially every student has 0 points. Each positive word in a feedback report increases the points of a student by 3, whereas each negative word decreases the points by 1.

You are given n feedback reports, represented by a 0-indexed string array report and a 0-indexed integer array student_id, where student_id[i] represents the ID of the student who has received the feedback report report[i]. The ID of each student is unique.

Given an integer k, return the top k students after ranking them in non-increasing order by their points. In case more than one student has the same points, the one with the lower ID ranks higher.



Example 1:

Input: positive_feedback = ["smart","brilliant","studious"], negative_feedback = ["not"], report = ["this student is studious","the student is smart"], student_id = [1,2], k = 2
Output: [1,2]
Explanation:
Both the students have 1 positive feedback and 3 points but since student 1 has a lower ID he ranks higher.
Example 2:

Input: positive_feedback = ["smart","brilliant","studious"], negative_feedback = ["not"], report = ["this student is not studious","the student is smart"], student_id = [1,2], k = 2
Output: [2,1]
Explanation:
- The student with ID 1 has 1 positive feedback and 1 negative feedback, so he has 3-1=2 points.
- The student with ID 2 has 1 positive feedback, so he has 3 points.
Since student 2 has more points, [2,1] is returned.


Constraints:

1 <= positive_feedback.length, negative_feedback.length <= 104
1 <= positive_feedback[i].length, negative_feedback[j].length <= 100
Both positive_feedback[i] and negative_feedback[j] consists of lowercase English letters.
No word is present in both positive_feedback and negative_feedback.
n == report.length == student_id.length
1 <= n <= 104
report[i] consists of lowercase English letters and spaces ' '.
There is a single space between consecutive words of report[i].
1 <= report[i].length <= 100
1 <= student_id[i] <= 109
All the values of student_id[i] are unique.
1 <= k <= n
"""
import heapq
from typing import List

from Common.ObjectTestingUtils import run_functional_tests

# Runtime
# 343 ms
# Beats
# 76.15%
# Memory
# 23.6 MB
# Beats
# 52.60%
class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        positive_words, negative_words = set(positive_feedback), set(negative_feedback)

        def calculate_student_score(report: str) -> int:
            nonlocal positive_words, negative_words
            score = 0
            for word in report.split(" "):
                if word in positive_words:
                    score += 3
                elif word in negative_words:
                    score -= 1
            return score

        heap = []
        for id, student_report in zip(student_id, report):
            score = calculate_student_score(student_report)
            heapq.heappush(heap, (-score, id))

        return [heapq.heappop(heap)[1] for _ in range(k)]


tests = [
    [["fkeofjpc","qq","iio"], ["jdh","khj","eget","rjstbhe","yzyoatfyx","wlinrrgcm"], ["rjstbhe eget kctxcoub urrmkhlmi yniqafy fkeofjpc iio yzyoatfyx khj iio","gpnhgabl qq qq fkeofjpc dflidshdb qq iio khj qq yzyoatfyx","tizpzhlbyb eget z rjstbhe iio jdh jdh iptxh qq rjstbhe","jtlghe wlinrrgcm jnkdbd k iio et rjstbhe iio qq jdh","yp fkeofjpc lkhypcebox rjstbhe ewwykishv egzhne jdh y qq qq","fu ql iio fkeofjpc jdh luspuy yzyoatfyx li qq v","wlinrrgcm iio qq omnc sgkt tzgev iio iio qq qq","d vhg qlj khj wlinrrgcm qq f jp zsmhkjokmb rjstbhe"], [96537918,589204657,765963609,613766496,43871615,189209587,239084671,908938263], 3, [239084671,589204657,43871615]],
    [["smart","brilliant","studious"], ["not"], ["this student is studious","the student is smart"], [1,2], 2, [1,2]],
    [["smart","brilliant","studious"], ["not"], ["this student is not studious","the student is smart"], [1,2], 2, [2,1]],
]

run_functional_tests(Solution().topStudents, tests)
