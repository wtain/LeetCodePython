"""
https://leetcode.com/problems/stream-of-characters/

Design an algorithm that accepts a stream of characters and checks if a suffix of these characters is a string of a given array of strings words.

For example, if words = ["abc", "xyz"] and the stream added the four characters (one by one) 'a', 'x', 'y', and 'z', your algorithm should detect that the suffix "xyz" of the characters "axyz" matches "xyz" from words.

Implement the StreamChecker class:

StreamChecker(String[] words) Initializes the object with the strings array words.
boolean query(char letter) Accepts a new character from the stream and returns true if any non-empty suffix from the stream forms a word that is in words.


Example 1:

Input
["StreamChecker", "query", "query", "query", "query", "query", "query", "query", "query", "query", "query", "query", "query"]
[[["cd", "f", "kl"]], ["a"], ["b"], ["c"], ["d"], ["e"], ["f"], ["g"], ["h"], ["i"], ["j"], ["k"], ["l"]]
Output
[null, false, false, false, true, false, true, false, false, false, false, false, true]

Explanation
StreamChecker streamChecker = new StreamChecker(["cd", "f", "kl"]);
streamChecker.query("a"); // return False
streamChecker.query("b"); // return False
streamChecker.query("c"); // return False
streamChecker.query("d"); // return True, because 'cd' is in the wordlist
streamChecker.query("e"); // return False
streamChecker.query("f"); // return True, because 'f' is in the wordlist
streamChecker.query("g"); // return False
streamChecker.query("h"); // return False
streamChecker.query("i"); // return False
streamChecker.query("j"); // return False
streamChecker.query("k"); // return False
streamChecker.query("l"); // return True, because 'kl' is in the wordlist


Constraints:

1 <= words.length <= 2000
1 <= words[i].length <= 2000
words[i] consists of lowercase English letters.
letter is a lowercase English letter.
At most 4 * 104 calls will be made to query.
"""
from collections import defaultdict
from functools import reduce
from typing import List

from Common.Constants import true, false, null
from Common.ObjectTestingUtils import run_object_tests


# Runtime: 5684 ms, faster than 11.23% of Python3 online submissions for Stream of Characters.
# Memory Usage: 38.7 MB, less than 50.45% of Python3 online submissions for Stream of Characters.
class StreamChecker:

    def __init__(self, words: List[str]):
        Trie = lambda: defaultdict(Trie)

        def build_trie(words: List[str]):
            trie = Trie()
            for w in words:
                w += '#'
                reduce(lambda cur, c: cur[c], w, trie)
            return trie

        self.trie = build_trie(words)
        self.pointers = []

    def query(self, letter: str) -> bool:
        result = False
        self.pointers.append(self.trie)
        new_pointers = []
        for pointer in self.pointers:
            pointer = pointer[letter]
            if pointer:
                result = result or ('#' in pointer)
                new_pointers.append(pointer)
        self.pointers = new_pointers
        return result

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

tests = [
    [
        ["StreamChecker", "query", "query", "query", "query", "query", "query", "query", "query", "query", "query", "query", "query"],
        [[["cd", "f", "kl"]], ["a"], ["b"], ["c"], ["d"], ["e"], ["f"], ["g"], ["h"], ["i"], ["j"], ["k"], ["l"]],
        [null, false, false, false, true, false, true, false, false, false, false, false, true]
    ],
    [
        ["StreamChecker","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query"],
        [[["ab","ba","aaab","abab","baa"]],["a"],["a"],["a"],["a"],["a"],["b"],["a"],["b"],["a"],["b"],["b"],["b"],["a"],["b"],["a"],["b"],["b"],["b"],["b"],["a"],["b"],["a"],["b"],["a"],["a"],["a"],["b"],["a"],["a"],["a"]],
        [null,false,false,false,false,false,true,true,true,true,true,false,false,true,true,true,true,false,false,false,true,true,true,true,true,true,false,true,true,true,false]
    ]
]

run_object_tests(tests, cls=StreamChecker)
