import sys


class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x

        while left <= right:

            middle = (left + right) // 2

            if middle * middle <= x < (middle + 1) * (middle + 1):
                return middle

            elif x < middle * middle:
                right = middle - 1

            else:
                left = middle + 1


if __name__ == "__main__":
    input = int(sys.stdin.read())
    sol = Solution()
    print(sol.mySqrt(input))
