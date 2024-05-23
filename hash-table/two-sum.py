class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        n = len(nums)

        for i in range(n):
            complement = target - nums[i]

            if complement in seen :
                return [i, seen[complement]]
            
            seen[nums[i]] = i
        
        return []
        
