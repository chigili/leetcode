from typing import List
from collections import defaultdict


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = defaultdict(int)
        for i, num in enumerate(nums):
            difference = target - num
            if difference in d:
                return [d[difference], i]
            d[num] = i


if __name__ == "__main__":
    nums = [3, 3]
    target = 6
    print(Solution().twoSum(nums, target))
