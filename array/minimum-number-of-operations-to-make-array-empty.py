class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if not nums:
            return -1
        
        operations = 0
        nums.sort()
        currNum = nums[0]
        currCount = 0
        for num in nums:
            if num == currNum:
                currCount += 1
            else:
                if currCount == 1:
                    return -1
                operations += math.ceil(currCount/3)

                currNum = num
                currCount = 1
        if currCount == 1:
            return -1
        operations += math.ceil(currCount/3)
        return operations

        