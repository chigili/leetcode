import sys
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        self.nums_dict = {}

        if nums is not None:
            for i in range(len(nums)):
                if nums[i] not in self.nums_dict:
                    self.nums_dict[nums[i]] = 1
                else:
                    return True
            return False


if __name__ == "__main__":
    input = sys.stdin.read()
    nums = list(map(int, input.split()))
    sol = Solution()
    print(sol.containsDuplicate(nums))
