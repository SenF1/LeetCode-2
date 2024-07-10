class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = set(nums)
        return sum(seen) * 2 - sum(nums)
        
  

        