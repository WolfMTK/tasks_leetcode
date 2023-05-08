class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s + s)[1:-1]


if __name__ == "__main__":
    assert Solution().repeatedSubstringPattern("abab") == True
    assert Solution().repeatedSubstringPattern("aba") == False
    assert Solution().repeatedSubstringPattern("abcabcabcabc") == True
