from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = 0
        key = True
        while key:
            for i in range(count, len(nums)):
                if not count:
                    continue
                if nums[i - count] + nums[i] == target:
                    key = False
                    list_num = [i - count, i]
            count += 1
        for index, value in enumerate(list_num):
            if value == -1:
                list_num[index] = len(nums) - 1
        return list_num


if __name__ == "__main__":
    print(Solution().twoSum(nums=[3, 2, 3], target=6))
    print(Solution().twoSum(nums=[2, 7, 11, 15], target=9))
    print(Solution().twoSum(nums=[3, 3], target=6))
    print(Solution().twoSum([-3,4,3,90], target=0))
    print(Solution().twoSum([3,2,3], target=6))
