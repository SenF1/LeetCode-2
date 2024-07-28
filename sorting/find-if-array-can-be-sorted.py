class Solution:
    def countSetBit(self, n):
        res = bin(n)
        return res.count("1")
    
    def canSortArray(self, nums: List[int]) -> bool:
        s = sorted(nums)
        segments = []
        currSegment = [nums[0]]
        currBitCount = self.countSetBit(nums[0])
        i = 1
        while i < len(nums):
            c = self.countSetBit(nums[i]) 
            if c == currBitCount:
                currSegment.append(nums[i])
            else:
                if sorted(currSegment) != s[i-len(currSegment):i]:
                    return False
                segments.append(currSegment)
                currSegment = [nums[i]]
                currBitCount = c
            i+=1
        segments.append(currSegment)
        if sorted(currSegment) != s[i-len(currSegment):i]:
            return False

        return True
            
        