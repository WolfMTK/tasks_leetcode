class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        return str_x == str_x[::-1]


if __name__ == "__main__":
    assert Solution().isPalindrome(121) == True
    assert Solution().isPalindrome(-121) == False
    assert Solution().isPalindrome(10) == False
