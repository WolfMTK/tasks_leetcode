from typing import List


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        count = arr[1] - arr[0]
        for i in range(1, len(arr) - 1):
            if arr[i+1] - arr[i] != count:
                return False
        return True


if __name__ == "__main__":
    assert Solution().canMakeArithmeticProgression([3, 5, 1]) == True
    assert Solution().canMakeArithmeticProgression([1, 2, 4]) == False
