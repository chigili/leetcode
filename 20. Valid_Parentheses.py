import sys
from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:

        closetoopen = {")": "(", "]": "[", "}": "{"}
        stack = deque()

        for char in s:
            if char in closetoopen:
                if not stack or stack.pop() != closetoopen[char]:
                    return False
            else:
                stack.append(char)

        return True if not stack else False


if __name__ == "__main__":
    input = sys.stdin.read()
    s = map(str, input.strip())
    print(Solution().isValid(s))
