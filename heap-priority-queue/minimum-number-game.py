class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        i = 0
        res = []
        while i < len(nums):
            res.append(nums[i+1])
            res.append(nums[i])
            i+=2
        return res
        