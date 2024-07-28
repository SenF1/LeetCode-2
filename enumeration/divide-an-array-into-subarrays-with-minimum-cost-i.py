class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        first = nums[0]
        nums_r = nums[1:]
        nums_r.sort()
        return sum(nums_r[:2]) + first
        