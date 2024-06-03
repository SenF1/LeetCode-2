class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left, right = 0, n-1
        while left < right:
            currentSum = numbers[left] + numbers[right]
            if currentSum == target:
                return [left+1, right+1]
            elif currentSum > target:
                right -= 1
            elif currentSum < target:
                left += 1
        
