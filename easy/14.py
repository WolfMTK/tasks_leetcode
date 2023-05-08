from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        return (nums == sorted(nums)) or (nums == sorted(nums, reverse=True))


if __name__ == "__main__":
    assert Solution().isMonotonic([1,2,2,3]) == True
    assert Solution().isMonotonic([6,5,4,4]) == True
    assert Solution().isMonotonic([1,3,2]) == False
