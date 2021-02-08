"""
https://leetcode.com/explore/featured/card/february-leetcoding-challenge-2021/585/week-2-february-8th-february-14th/3633/
https://leetcode.com/problems/peeking-iterator/
Given an Iterator class interface with methods: next() and hasNext(), design and implement a PeekingIterator that support the peek() operation -- it essentially peek() at the element that will be returned by the next call to next().

Example:

Assume that the iterator is initialized to the beginning of the list: [1,2,3].

Call next() gets you 1, the first element in the list.
Now you call peek() and it returns 2, the next element. Calling next() after that still return 2.
You call next() the final time and it returns 3, the last element.
Calling hasNext() after that should return false.
Follow up: How would you extend your design to be generic and work with all types, not just integer?
"""


# Below is the interface for Iterator, which is already defined for you.
#
class Iterator:
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """
        self.nums = nums
        self.next_i = 0

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """
        return self.next_i < len(self.nums)

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """
        n = self.next_i
        self.next_i += 1
        return self.nums[n]


# Runtime: 28 ms, faster than 88.74% of Python3 online submissions for Peeking Iterator.
# Memory Usage: 14.6 MB, less than 36.42% of Python3 online submissions for Peeking Iterator.
class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.has_next = self.iterator.hasNext()
        self.curr = iterator.next() if self.has_next else 0

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.curr

    def next(self):
        """
        :rtype: int
        """
        rv = self.curr
        if self.has_next:
            self.curr = self.iterator.next()
            self.has_next = self.iterator.hasNext()
        else:
            self.curr = None
        return rv

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.curr is not None

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].


nums = [1,2,3]
it = PeekingIterator(Iterator(nums))
print(it.next())  # 1
print(it.peek())  # 2
print(it.next())  # 2
print(it.next())  # 3
print(it.hasNext())  # False

print("--")

nums = [1,2,3,4]
it = PeekingIterator(Iterator(nums))
print(it.hasNext())  # True
print(it.peek())  # 1
print(it.peek())  # 1
print(it.next())  # 1
print(it.next())  # 2
print(it.peek())  # 3
print(it.peek())  # 3
print(it.next())  # 3
print(it.hasNext())  # True
print(it.peek())  # 4
print(it.hasNext())  # True
print(it.next())  # 4
print(it.hasNext())  # False

# ["PeekingIterator","hasNext","peek","peek","next","next","peek","peek","next","hasNext","peek","hasNext","next","hasNext"]
# [[[1,2,3,4]],[],[],[],[],[],[],[],[],[],[],[],[],[]]
# [null,true,1,1,1,2,3,3,3,true,4,true,4,false]