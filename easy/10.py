from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = nums.count(0)
        new_nums = [i for i in nums if i != 0]
        for i in range(count):
            new_nums.append(0)
        nums[:] = new_nums
        return nums

if __name__ == '__main__':
    assert Solution().moveZeroes([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]
    assert Solution().moveZeroes([0]) == [0]
