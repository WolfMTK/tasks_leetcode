class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


if __name__ == '__main__':
    assert Solution().strStr("sadbutsad", "sad") == 0
    assert Solution().strStr("leetcode", "leeto") == -1