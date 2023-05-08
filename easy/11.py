from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits_int = int(''.join(map(str, digits))) + 1
        return list(map(int, str(digits_int)))


if __name__ == '__main__':
    assert Solution().plusOne([1, 2, 3]) == [1, 2, 4]
    assert Solution().plusOne([4, 3, 2, 1]) == [4, 3, 2, 2]
    assert Solution().plusOne([9]) == [1, 0]
