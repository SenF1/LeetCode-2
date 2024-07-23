class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        new=[]
        co = 0
        for i in nums:
            if nums.count(i) > co:
                new=[]
                new.append(i)
                co=nums.count(i)
                continue
            if nums.count(i) == co:
                new.append(i)
        return len(new)