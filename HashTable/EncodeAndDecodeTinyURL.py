"""
https://leetcode.com/explore/featured/card/march-leetcoding-challenge-2021/590/week-3-march-15th-march-21st/3673/
https://leetcode.com/problems/encode-and-decode-tinyurl/

Note: This is a companion problem to the System Design problem: Design TinyURL.
TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.
"""
import hashlib


# Runtime: 28 ms, faster than 91.48% of Python3 online submissions for Encode and Decode TinyURL.
# Memory Usage: 14.2 MB, less than 59.29% of Python3 online submissions for Encode and Decode TinyURL.
class Codec:

    def __init__(self):
        self.base = "http://tinyurl.com/"
        self.hash_table = {}

    def hash(self, longUrl: str) -> str:
        return str(hash(longUrl))
        #hash_object = hashlib.sha256(longUrl)
        # return str(hash_object.hexdigest())

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        shortUrl = self.base + self.hash(longUrl)
        self.hash_table[shortUrl] = longUrl
        return shortUrl

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.hash_table.get(shortUrl)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))


url = "https://leetcode.com/problems/encode-and-decode-tinyurl/"

codec = Codec()
print(codec.decode(codec.encode(url)))