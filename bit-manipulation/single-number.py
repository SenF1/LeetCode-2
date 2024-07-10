class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # set(nums)
        seen = set()
        for e in nums:
            if e in seen:
                seen.remove(e)
            else:
                seen.add(e)
        return seen.pop()
        
  

        