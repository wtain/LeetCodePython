"""
https://leetcode.com/explore/featured/card/july-leetcoding-challenge-2021/610/week-3-july-15th-july-21st/3815/
https://leetcode.com/problems/valid-triangle-number/

Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.



Example 1:

Input: nums = [2,2,3,4]
Output: 3
Explanation: Valid combinations are:
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3
Example 2:

Input: nums = [4,2,3,4]
Output: 4


Constraints:

1 <= nums.length <= 1000
0 <= nums[i] <= 1000
"""
import bisect
import random
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Trivial
# class Solution:
#     def triangleNumber(self, nums: List[int]) -> int:
#         nums.sort()
#         n = len(nums)
#         cnt = 0
#         for i in range(n):
#             for j in range(i+1, n):
#                 for k in range(j+1, n):
#                     if nums[k] - nums[i] < nums[j] < nums[k] + nums[i]:
#                         cnt += 1
#         return cnt


# Runtime: 4908 ms, faster than 5.52% of Python3 online submissions for Valid Triangle Number.
# Memory Usage: 14.5 MB, less than 30.59% of Python3 online submissions for Valid Triangle Number.
# class Solution:
#     def triangleNumber(self, nums: List[int]) -> int:
#         nums.sort()
#         n = len(nums)
#         cnt = 0
#         for i in range(n):
#             for j in range(i+1, n):
#                 a, b = nums[i], nums[j]
#                 # b - a < c < a + b
#
#                 k1 = bisect.bisect_left(nums, b-a + 1, j+1)
#                 k2 = bisect.bisect_right(nums, b + a - 1, j + 1)
#                 cnt += max(0, k2 - k1)
#                 # print(i, j, k1, k2)
#                 # for k in range(k1, k2):
#                 #     print(nums[i], nums[j], nums[k])
#         return cnt


# Runtime: 1732 ms, faster than 43.24% of Python3 online submissions for Valid Triangle Number.
# Memory Usage: 14.4 MB, less than 62.36% of Python3 online submissions for Valid Triangle Number.
# class Solution:
#     def triangleNumber(self, nums: List[int]) -> int:
#         nums.sort()
#         n = len(nums)
#         cnt = 0
#         for j in range(1, n-1):
#             b = nums[j]
#             k2 = bisect.bisect_right(nums, 2 * b, j+1)
#             for k in range(j+1, k2):
#                 c = nums[k]
#                 # b - a < c < a + b
#
#                 i1 = bisect.bisect_left(nums, c-b + 1, 0, j)
#                 cnt += max(0, j - i1)
#         return cnt


# https://leetcode.com/problems/valid-triangle-number/solution/
# Runtime: 1876 ms, faster than 39.25% of Python3 online submissions for Valid Triangle Number.
# Memory Usage: 14.5 MB, less than 30.59% of Python3 online submissions for Valid Triangle Number.
# class Solution:
#     def triangleNumber(self, nums: List[int]) -> int:
#         nums.sort()
#         n = len(nums)
#         cnt = 0
#         for i in range(n-2):
#             k = i+2
#             if nums[i] == 0:
#                 continue
#             for j in range(i+1, n-1):
#                 while k < n and nums[i] + nums[j] > nums[k]:
#                     k += 1
#                 cnt += k - j - 1
#         return cnt


# Runtime: 1084 ms, faster than 93.20% of Python3 online submissions for Valid Triangle Number.
# Memory Usage: 14.3 MB, less than 84.62% of Python3 online submissions for Valid Triangle Number.
# https://leetcode.com/problems/valid-triangle-number/discuss/1339248/Python-sort-%2B-2-pointers-solution-explained
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        cnt = 0
        for i in range(2, n):
            l, r = 0, i-1
            while l < r:
                if nums[l] + nums[r] > nums[i]:
                    cnt += r - l
                    r -= 1
                else:
                    l += 1
        return cnt


tests = [
    [[2,2,3,4], 3],
    [[4,2,3,4], 4],
    [[926, 349, 382, 910, 64, 684, 834, 401, 736, 234, 912, 337, 976, 405, 630, 391, 154, 440, 566, 989, 341, 293, 720, 382, 893, 110, 519, 808, 302, 991, 461, 354, 257, 85, 994, 648, 426, 906, 915, 356, 258, 833, 437, 709, 855, 203, 606, 846, 744, 206, 602, 508, 565, 599, 866, 573, 209, 895, 661, 75, 268, 447, 876, 274, 843, 258, 167, 739, 629, 16, 173, 224, 512, 867, 705, 867, 858, 675, 979, 280, 305, 576, 272, 586, 742, 263, 207, 900, 788, 620, 103, 653, 888, 688, 314, 182, 82, 468, 163, 463, 220, 141, 875, 565, 515, 80, 672, 711, 467, 940, 123, 652, 515, 702, 79, 746, 717, 84, 59, 793, 512, 288, 430, 998, 757, 533, 501, 561, 410, 186, 246, 362, 981, 438, 793, 793, 120, 447, 559, 734, 324, 985, 802, 597, 480, 844, 815, 360, 588, 666, 792, 699, 715, 33, 703, 606, 58, 482, 332, 928, 319, 742, 130, 744, 589, 720, 251, 267, 407, 578, 40, 928, 97, 703, 358, 747, 786, 227, 817, 284, 49, 20, 378, 82, 873, 381, 913, 242, 99, 664, 772, 393, 656, 589, 465, 368, 970, 948, 746, 3, 771, 355, 744, 303, 497, 724, 389, 362, 870, 83, 110, 338, 80, 218, 225, 258, 636, 993, 292, 867, 637, 626, 815, 109, 448, 458, 542, 58, 587, 879, 104, 147, 123, 850, 510, 344, 273, 373, 196, 654, 767, 476, 650, 77, 125, 502, 978, 805, 200, 424, 972, 413, 867, 783, 502, 397, 780, 709, 992, 182, 350, 190, 114, 997, 823, 58, 939, 571, 581, 846, 742, 554, 320, 263, 711, 562, 508, 399, 458, 523, 335, 589, 169, 929, 995, 503, 869, 280, 372, 480, 632, 196, 49, 717, 826, 192, 130, 423, 352, 265, 478, 842, 560, 280, 320, 327, 606, 941, 807, 786, 183, 555, 327, 197, 456, 939, 608, 595, 777, 289, 830, 383, 963, 589, 522, 468, 573, 123, 501, 260, 448, 579, 518, 439, 828, 887, 785, 124, 48, 187, 730, 917, 473, 122, 747, 333, 971, 159, 302, 332, 164, 118, 719, 128, 413, 797, 912, 474, 693, 409, 694, 361, 461, 641, 508, 941, 204, 78, 164, 748, 295, 27, 865, 847, 479, 604, 279, 66, 587, 103, 706, 471, 804, 133, 619, 399, 925, 357, 744, 710, 720, 486, 50, 311, 241, 404, 304, 395, 713, 185, 732, 525, 59, 964, 493, 26, 421, 7, 339, 885, 129, 337, 412, 665, 567, 554, 621, 906, 135, 635, 579, 563, 133, 871, 925, 323, 18, 263, 614, 766, 408, 68, 902, 378, 925, 942, 666, 90, 549, 268, 430, 200, 806, 152, 713, 85, 147, 433, 572, 57, 8, 104, 438, 163, 201, 988, 901, 729, 260, 415, 947, 23, 315, 261, 937, 44, 330, 685, 613, 809, 950, 107, 790, 910, 780, 146, 71, 960, 985, 413, 453, 731, 766, 393, 565, 666, 596, 569, 817, 940, 121, 446, 842, 47, 34, 31, 511, 183, 336, 869, 810, 426, 480, 518, 18, 733, 695, 829, 970, 520, 115, 970, 787, 920, 731, 972, 406, 204, 882, 275, 486, 125, 657, 543, 630, 230, 450, 252, 176, 812, 387, 992, 487, 268, 516, 993, 516, 926, 189, 521, 149, 231, 871, 902, 336, 410, 459, 953, 869, 628, 403, 379, 62, 907, 86, 199, 15, 115, 475, 581, 807, 666, 284, 34, 632, 752, 956, 169, 33, 666, 927, 659, 747, 416, 317, 251, 363, 891, 486, 944, 369, 525, 812, 253, 291, 949, 492, 961, 184, 341, 888, 302, 936, 224, 152, 274, 534, 877, 663, 935, 730, 758, 522, 39, 932, 952, 566, 491, 376, 882, 486, 278, 684, 838, 417, 520, 356, 21, 265, 776, 423, 760, 36, 332, 458, 998, 632, 443, 493, 475, 398, 972, 391, 12, 686, 192, 73, 638, 737, 581, 650, 222, 694, 680, 388, 978, 204, 850, 710, 628, 227, 977, 846, 851, 799, 557, 707, 764, 893, 624, 603, 201, 151, 639, 889, 538, 577, 607, 696, 780, 441, 209, 190, 910, 6, 256, 856, 909, 722, 598, 177, 904, 547, 43, 538, 316, 132, 997, 627, 625, 941, 429, 837, 135, 568, 124, 257, 129, 234, 670, 637, 520, 794, 895, 993, 759, 230, 581, 83, 383, 939, 933, 447, 706, 497, 79, 190, 511, 703, 965, 36, 386, 665, 107, 900, 339, 212, 482, 429, 455, 162, 935, 684, 803, 958, 767, 27, 986, 37, 733, 377, 204, 286, 812, 246, 330, 724, 570, 624, 612, 721, 883, 65, 742, 750, 246, 530, 102, 528, 843, 20, 390, 90, 435, 645, 219, 979, 151, 830, 147, 376, 54, 239, 342, 160, 933, 999, 5, 122, 367, 974, 75, 494, 806, 178, 999, 938, 615, 884, 809, 744, 801, 425, 718, 424, 467, 500, 253, 765, 870, 679, 954, 663, 1, 641, 936, 569, 30, 630, 395, 296, 435, 180, 722, 760, 36, 677, 992, 13, 503, 836, 990, 446, 483, 370, 691, 56, 485, 680, 492, 935, 345, 429, 385, 262, 794, 679, 409, 332, 29, 492, 449, 446, 518, 38, 595, 537, 20, 455, 310, 547, 90, 990, 623, 207, 108, 764, 633, 794, 648, 88, 749, 703, 360, 391, 486, 911, 607, 348, 517, 966, 492, 272, 75, 400, 206, 789, 784, 936, 102, 841, 488, 993, 459, 272, 787, 914, 341, 87, 298, 121, 995, 355, 61, 895, 350, 146, 299, 912, 984, 319, 606, 665, 673, 463, 110, 572, 988, 371, 347, 475, 887, 460, 245, 531, 85, 19, 79, 377, 14, 50, 754, 589, 314, 810, 192, 589, 306, 487, 114, 364, 669, 433, 101, 886, 697, 399, 929, 943, 28, 530, 463, 438, 65, 677, 544, 889, 825, 731, 740, 665, 369, 789, 689, 66, 516, 766, 871, 317, 508, 721, 595, 667, 274, 287, 851, 725, 262, 13, 545, 62, 440, 480, 241, 317, 392, 413, 562, 870, 782, 596, 355, 768, 140, 521, 522, 811, 609, 452, 661, 82, 971, 416, 701, 750, 671, 993, 681, 61, 55], 87108635]
]

# test = [[random.randrange(1, 1001) for _ in range(1000)], 0]
# test[1] = Solution().triangleNumber(test[0])
#
# print(test)
# tests.append(test)

run_functional_tests(Solution().triangleNumber, tests)