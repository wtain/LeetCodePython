"""
https://leetcode.com/problems/image-smoother/description/?envType=daily-question&envId=2023-12-19

An image smoother is a filter of the size 3 x 3 that can be applied to each cell of an image by rounding down the average of the cell and the eight surrounding cells (i.e., the average of the nine cells in the blue smoother). If one or more of the surrounding cells of a cell is not present, we do not consider it in the average (i.e., the average of the four cells in the red smoother).


Given an m x n integer matrix img representing the grayscale of an image, return the image after applying the smoother on each cell of it.



Example 1:


Input: img = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[0,0,0],[0,0,0],[0,0,0]]
Explanation:
For the points (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the points (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
For the point (1,1): floor(8/9) = floor(0.88888889) = 0
Example 2:


Input: img = [[100,200,100],[200,50,200],[100,200,100]]
Output: [[137,141,137],[141,138,141],[137,141,137]]
Explanation:
For the points (0,0), (0,2), (2,0), (2,2): floor((100+200+200+50)/4) = floor(137.5) = 137
For the points (0,1), (1,0), (1,2), (2,1): floor((200+200+50+200+100+100)/6) = floor(141.666667) = 141
For the point (1,1): floor((50+200+200+200+200+100+100+100+100)/9) = floor(138.888889) = 138


Constraints:

m == img.length
n == img[i].length
1 <= m, n <= 200
0 <= img[i][j] <= 255
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 486
# ms
# Beats
# 62.23%
# of users with Python3
# Memory
# 17.00
# MB
# Beats
# 84.82%
# of users with Python3
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        n, m = len(img), len(img[0])
        result = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                sum, cnt = 0, 0
                for a in range(-1, 2):
                    i1 = i + a
                    if i1 < 0 or i1 >= n:
                        continue
                    for b in range(-1, 2):
                        j1 = j + b
                        if j1 < 0 or j1 >= m:
                            continue
                        sum += img[i1][j1]
                        cnt += 1
                result[i][j] = sum // cnt
        return result


tests = [
    [[[1,1,1],[1,0,1],[1,1,1]], [[0,0,0],[0,0,0],[0,0,0]]],
    [[[100,200,100],[200,50,200],[100,200,100]], [[137,141,137],[141,138,141],[137,141,137]]],
]

run_functional_tests(Solution().imageSmoother, tests)
