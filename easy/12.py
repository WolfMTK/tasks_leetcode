from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        count = 1
        for i in nums:
            count *= i
        return 1 if count > 0 else -1 if count < 0 else count


if __name__ == '__main__':
    assert Solution().arraySign([-1, -2, -3, -4, 3, 2, 1]) == 1
    assert Solution().arraySign([1, 5, 0, 2, -3]) == 0
    assert Solution().arraySign([-1, 1, -1, 1, -1]) == -1
