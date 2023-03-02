import sys
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = sorted(set(nums))
        return len(nums)


if __name__ == "__main__":

    input = sys.stdin.read()
    nums = list(map(int, input.split()))
    sol = Solution()
    print(sol.removeDuplicates(nums))
