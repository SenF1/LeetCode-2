class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        s='123456789'
        ans=[]
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                st=int(s[i:j+1])
                if(st>=low and st<=high):
                    ans.append(st)
        ans.sort()            
        return ans       