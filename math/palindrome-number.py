class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        list = []
        while x > 0:
            current = x%10
            list.append(current)
            x//=10
        
        while len(list)>1:
            if list[0] != list[-1]:
                return False
            list.pop(0)
            list.pop(-1)
        return True
        