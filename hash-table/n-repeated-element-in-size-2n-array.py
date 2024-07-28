class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)//2
        for i in range(len(nums)-n+1):
            curr = nums[i]
            count = 0
            for j in range(n):
                if nums[i+j] == curr:
                    count += 1
            if count == n:
                return curr
            count = 0
        return -1

        