import bisect
import sys
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m != len(nums1):
            for i in range(len(nums1) - 1, m - 1, -1):
                nums1.pop(i)

        for i in nums2:
            bisect.insort(nums1, i)

        return nums1

    def merge_m_plus_n(
        self, nums1: List[int], m: int, nums2: List[int], n: int
    ) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums1[m - 1] >= nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1

            if n > 0:
                nums1[:n] = nums2[:n]


if __name__ == "__main__":
    nums1 = [int(i) for i in input().split()]
    m = int(input())
    nums2 = [int(i) for i in input().split()]
    n = int(input())
    sol = Solution()
    print(sol.merge_m_plus_n(nums1, m, nums2, n))
