from typing import List
import sys


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        shortest_str = min(strs, key=len)
        for i, char in enumerate(shortest_str):
            for s in strs:
                if s[i] != char:
                    return shortest_str[:i]
        return shortest_str


if __name__ == "__main__":
    input = sys.stdin.read()
    strs = list(map(str, input.split()))
    print(Solution().longestCommonPrefix(strs))
