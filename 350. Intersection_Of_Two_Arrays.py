import sys
from typing import List
from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counts = Counter(nums1)
        result = []

        for i in nums2:
            if counts[i] > 0:
                result.append(i)
                counts[i] -= 1

        return result


if __name__ == "__main__":
    input1 = sys.stdin.read()
    nums1 = list(map(int, input1.split()))
    input2 = sys.stdin.read()
    nums2 = list(map(int, input2.split()))
    sol = Solution()
    print(sol.intersect(nums1, nums2))
