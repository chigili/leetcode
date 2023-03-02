import sys


class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        length = 0
        s = s.strip()

        for i in range(0, len(s)):
            if s[i] == " ":
                length = 0
            else:
                length += 1
        return length


if __name__ == "__main__":
    input = sys.stdin.read()
    sol = Solution()
    print(sol.lengthOfLastWord(input))
