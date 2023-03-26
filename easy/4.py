from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for string in strs:
            while string[:len(prefix)] != prefix and prefix:
                prefix = prefix[:len(prefix) - 1]
        return prefix
                    

if __name__ == "__main__":
    assert Solution().longestCommonPrefix(strs=["flower", "flow", "flight"]) == "fl"
    assert Solution().longestCommonPrefix(strs=["dog","racecar","car"]) == ""
