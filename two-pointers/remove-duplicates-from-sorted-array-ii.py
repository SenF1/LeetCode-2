class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        if len(nums) <= 2:
            return len(nums)
        
        k = 0
        for i in range(len(nums)-2):
            if nums[i] == nums[i+1] and nums[i] == nums[i+2]:
                continue
            else:
                nums[k] = nums[i]
                k+=1
        nums[k] = nums[-2]
        k += 1
        nums[k] = nums[-1]
        k += 1
        return k