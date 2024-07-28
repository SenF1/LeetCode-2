class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in range(len(nums)):
            idx = 0
            while nums[i] in res[idx]:
                idx+=1
            if not res[idx]:
                res.append([])
            res[idx].append(nums[i])
        res.pop()
        return res
        