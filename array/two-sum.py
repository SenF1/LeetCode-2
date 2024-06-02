class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        if len(nums) == 0: return []

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in seen:
                return [seen[complement], i]
            seen[nums[i]] = i
        return []
        
