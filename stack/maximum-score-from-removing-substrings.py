class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_substring(s, sub, score):
            stack = []
            total = 0
            for char in s:
                if stack and stack[-1] + char == sub:
                    stack.pop()
                    total += score
                else:
                    stack.append(char)
            return "".join(stack), total
        
        total = 0
        if x > y:
            s, highTotal = remove_substring(s, "ab", x)
            _, lowTotal = remove_substring(s, "ba", y)
        else:
            s, highTotal = remove_substring(s, "ba", y)
            _, lowTotal = remove_substring(s, "ab", x)
        
        total = highTotal + lowTotal
        return total
