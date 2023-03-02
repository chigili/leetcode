import sys
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        new_product = []
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if i != j:
                    product *= nums[j]
            new_product.append(product)

        return new_product

    def productExceptSelf_fast(self, nums: List[int]) -> List[int]:

        product = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            product[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            product[i] *= postfix
            postfix *= nums[i]

        return product


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    sol = Solution()
    print(sol.productExceptSelf_fast(data))
