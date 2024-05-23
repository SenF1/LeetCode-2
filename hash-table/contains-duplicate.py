class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        lst = set()
        for num in nums:
            if num in lst:
                return True
            lst.add(num)

        return False
        