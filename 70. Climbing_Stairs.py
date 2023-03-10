import sys


class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for i in range(n - 1):
            one, two = one + two, one

        return one


if __name__ == "__main__":
    input = int(sys.stdin.read())
    sol = Solution()
    print(sol.climbStairs(input))
