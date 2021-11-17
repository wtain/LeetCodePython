"""
https://leetcode.com/problems/iterator-for-combination/

Design the CombinationIterator class:

CombinationIterator(string characters, int combinationLength) Initializes the object with a string characters of sorted distinct lowercase English letters and a number combinationLength as arguments.
next() Returns the next combination of length combinationLength in lexicographical order.
hasNext() Returns true if and only if there exists a next combination.


Example 1:

Input
["CombinationIterator", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[["abc", 2], [], [], [], [], [], []]
Output
[null, "ab", true, "ac", true, "bc", false]

Explanation
CombinationIterator itr = new CombinationIterator("abc", 2);
itr.next();    // return "ab"
itr.hasNext(); // return True
itr.next();    // return "ac"
itr.hasNext(); // return True
itr.next();    // return "bc"
itr.hasNext(); // return False


Constraints:

1 <= combinationLength <= characters.length <= 15
All the characters of characters are unique.
At most 104 calls will be made to next and hasNext.
It's guaranteed that all calls of the function next are valid.
"""
from Common.Constants import false, true, null
from Common.ObjectTestingUtils import run_object_tests


# Runtime: 64 ms, faster than 40.80% of Python3 online submissions for Iterator for Combination.
# Memory Usage: 16.2 MB, less than 77.61% of Python3 online submissions for Iterator for Combination.
class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.characters = characters
        self.mask = [True] * combinationLength + [False] * (len(characters)-combinationLength)
        self.has_next = combinationLength > 0
        self.has_current = self.has_next

    def check_can_move_mask(self) -> bool:
        i = 0
        while i < len(self.mask) and not self.mask[i]:
            i += 1
        while i < len(self.mask) and self.mask[i]:
            i += 1
        return i < len(self.mask)

    def move_mask(self):
        if not self.has_next:
            self.has_current = False
            return
        zero_pos = -1
        cnt1 = 0
        for i in range(len(self.mask)-1, -1, -1):
            if not self.mask[i]:
                zero_pos = i
            elif zero_pos != -1:
                self.mask[i] = False
                break
            else:
                cnt1 += 1
                self.mask[i] = False
        self.mask[zero_pos] = True
        for j in range(zero_pos+1, len(self.mask)):
            if cnt1 == 0:
                break
            self.mask[j] = True
            cnt1 -= 1
        self.has_next = self.check_can_move_mask()

    def build_combination(self) -> str:
        return "".join(c for c, m in zip(self.characters, self.mask) if m)

    def next(self) -> str:
        result = self.build_combination()
        self.move_mask()
        return result

    def hasNext(self) -> bool:
        return self.has_current

# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()


tests = [
    [
        ["CombinationIterator", "next", "hasNext", "next", "hasNext", "next", "hasNext"],
        [["abc", 2], [], [], [], [], [], []],
        [null, "ab", true, "ac", true, "bc", false]
    ]
]

# c = CombinationIterator("abc", 2)
# while c.hasNext():
#     print(c.next())

run_object_tests(tests, cls=CombinationIterator)
