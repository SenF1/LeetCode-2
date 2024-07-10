class Solution:
    def minOperations(self, logs: List[str]) -> int:
        steps = 0
        for op in logs:
            if op == "../":
                steps = max(steps-1, 0)
            elif op == "./":
                continue
            else:
                steps += 1
        return steps
