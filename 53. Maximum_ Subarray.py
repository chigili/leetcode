import sys
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        curSum = 0

        for i in nums:
            if curSum < 0:
                curSum = 0
            curSum += i
            maxSub = max(maxSub, curSum)
        return maxSub


if __name__ == "__main__":
    input = sys.stdin.read()
    nums = list(map(int, input.split()))
    sol = Solution()
    print(sol.maxSubArray(nums))
