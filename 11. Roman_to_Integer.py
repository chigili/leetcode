import sys


class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = 0
        i = 0
        n = len(s)
        while i < n:

            if i != n - 1 and roman_dict[s[i]] < roman_dict[s[i + 1]]:
                result += roman_dict[s[i + 1]] - roman_dict[s[i]]
                i += 2
                continue
            else:
                result += roman_dict[s[i]]

            i += 1
        return result


if __name__ == "__main__":
    s = sys.stdin.read().strip("\n")
    print(Solution().romanToInt(str(s)))

