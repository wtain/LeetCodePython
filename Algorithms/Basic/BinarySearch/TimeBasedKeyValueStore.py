"""
https://leetcode.com/problems/time-based-key-value-store/

Create a timebased key-value store class TimeMap, that supports two operations.

1. set(string key, string value, int timestamp)

Stores the key and value, along with the given timestamp.
2. get(string key, int timestamp)

Returns a value such that set(key, value, timestamp_prev) was called previously, with timestamp_prev <= timestamp.
If there are multiple such values, it returns the one with the largest timestamp_prev.
If there are no values, it returns the empty string ("").


Example 1:

Input: inputs = ["TimeMap","set","get","get","set","get","get"], inputs = [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]
Output: [null,null,"bar","bar",null,"bar2","bar2"]
Explanation:
TimeMap kv;
kv.set("foo", "bar", 1); // store the key "foo" and value "bar" along with timestamp = 1
kv.get("foo", 1);  // output "bar"
kv.get("foo", 3); // output "bar" since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 ie "bar"
kv.set("foo", "bar2", 4);
kv.get("foo", 4); // output "bar2"
kv.get("foo", 5); //output "bar2"

Example 2:

Input: inputs = ["TimeMap","set","set","get","get","get","get","get"], inputs = [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]
Output: [null,null,null,"","high","high","low","low"]


Note:

All key/value strings are lowercase.
All key/value strings have length in the range [1, 100]
The timestamps for all TimeMap.set operations are strictly increasing.
1 <= timestamp <= 10^7
TimeMap.set and TimeMap.get functions will be called a total of 120000 times (combined) per test case.
"""
#from bisect import bisect, bisect_left, bisect_right
import bisect
from sortedcontainers import SortedDict


# Runtime: 724 ms, faster than 57.13% of Python3 online submissions for Time Based Key-Value Store.
# Memory Usage: 71.3 MB, less than 13.03% of Python3 online submissions for Time Based Key-Value Store.
class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # print("*** set: key=" + key + ", timestamp=" + str(timestamp) + ", value="+str(value))
        if not self.data.get(key):
            self.data[key] = []
        self.data[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        # print("*** get: key=" + key + ", timestamp=" + str(timestamp), self.data[key])
        if not self.data.get(key):
            return ""
        index = bisect.bisect(self.data[key], [timestamp, ''])
        #k = self.data[key].bisect(timestamp)
        #k = self.data[key].iloc[k]
        #print(index)
        if index >= len(self.data[key]):
            index = -1
        if self.data[key][index][0] > timestamp:
            if index == 0:
                return ""
            else:
                index -= 1
        # elif self.data[key][index][0] < timestamp:
        #     index -= 1
        # print(index, len(self.data[key]))
        return self.data[key][index][1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

null = None
tests = [
    (
        ["TimeMap","set","get","get","set","get","get"],
        [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]],
        [null,null,"bar","bar",null,"bar2","bar2"]
    ),
    (
        ["TimeMap","set","set","get","get","get","get","get"],
        [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]],
        [null,null,null,"","high","high","low","low"]
    )
]


def call_method(o, name, *args, **kwargs):
    # print("*** Calling " + name + " with " + str(args) + " and " + str(kwargs))
    return getattr(o, name)(*args, **kwargs)


for test in tests:
    methods = test[0]
    arguments = test[1]
    expected = test[2]
    n = len(methods)
    object = TimeMap()
    fail = False
    for i in range(1, n):
        output = call_method(object, methods[i], *arguments[i])
        if output != expected[i]:
            fail = True
            print("FAIL: " + str(output) + " != " + str(expected[i]))
            break
    if not fail:
        print("PASS")
