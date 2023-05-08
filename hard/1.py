from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)
        length = len(nums)
        if length % 2 == 0:
            return (nums[length // 2] + nums[length // 2 - 1]) / 2
        else:
            return nums[length // 2]


if __name__ == '__main__':
    assert Solution().findMedianSortedArrays([1, 3], [2]) == 2.0
    assert Solution().findMedianSortedArrays([1, 2], [3, 4]) == 2.5
    assert Solution().findMedianSortedArrays([], [1]) == 1.0
