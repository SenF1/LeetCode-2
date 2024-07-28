class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        preSum = nums[0]
        i = 1
        while i < len(nums) and nums[i] == nums[i-1] + 1:
            preSum += nums[i]
            i += 1
        while preSum in nums:
            preSum += 1
        return preSum
        