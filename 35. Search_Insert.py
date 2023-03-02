import sys
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = right + left // 2
            if target == nums[middle]:
                return middle

            elif target > nums[middle]:
                left = middle + 1

            elif target < nums[middle]:
                right = middle - 1

        return left


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    nums = data[:-1]
    val = data[-1]
    sol = Solution()
    print(sol.searchInsert(nums, val))
