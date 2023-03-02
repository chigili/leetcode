import sys
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        sum = 0
        rev_digits = digits[::-1]

        for i, digit in enumerate(rev_digits):
            powwe = pow(10, i) * digit
            sum += powwe

        new_sum = sum + 1

        return list(map(int, str(new_sum)))


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    sol = Solution()
    print(sol.plusOne(data))
