class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        b=s.count('1')
        c=s.count('0')
        s1=""
        for i in range(b-1):
            s1+='1'
        for i in range(c):
            s1+='0'
        s1+='1'
        return s1