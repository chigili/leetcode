import sys


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x < 10:
            return True
        else:
            x_str = str(x)
            if x_str == x_str[::-1]:
                return True
            else:
                return False


if __name__ == "__main__":
    x = sys.stdin.read()
    print(Solution().isPalindrome(int(x)))
