class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {'{': '}', '(': ')', '[': ']'}
        for val in s:
            if val in d:
                stack.append(val)
            elif not stack or d[stack.pop()] != val:
                return False

        return not stack
        