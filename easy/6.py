class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for c in t:
            if t.count(c) != s.count(c):
                return c


if __name__ == "__main__":
    assert Solution().findTheDifference("abcd", "abcde") == "e"
    assert Solution().findTheDifference("", "y") == "y"
    assert Solution().findTheDifference("a", "aa") == "a"
