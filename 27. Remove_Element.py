import sys
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    nums = data[:-1]
    val = data[-1]
    sol = Solution()
    print(sol.removeElement(nums, val))
