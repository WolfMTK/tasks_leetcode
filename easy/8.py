class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for i in set(s + t):
            if s.count(i) != t.count(i):
                return False
        return True


if __name__ == '__main__':
    Solution().isAnagram('anagram', 'nagaram')
    assert Solution().isAnagram('anagram', 'nagaram') == True
    assert Solution().isAnagram('rat', 'car') == False
