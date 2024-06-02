class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        slow = 0
        current_sum = 0
        min_length = float('inf')

        for fast in range(n):
            current_sum += nums[fast]

            while current_sum >= target:
                min_length = min(min_length, fast - slow + 1)
                current_sum -= nums[slow]
                slow += 1

        return 0 if min_length == float('inf') else min_length


        