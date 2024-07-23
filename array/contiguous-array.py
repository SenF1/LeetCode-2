class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        partial_sum = 0
        table = { 0: -1}
        
        max_length = 0
        
        for idx, number in enumerate( nums ):
            if number:
                partial_sum += 1
            else:
                partial_sum -= 1
                
            if partial_sum in table:
                max_length = max( max_length, ( idx - table[partial_sum] ) )
                
            else:
                table[ partial_sum ] = idx
                
        return max_length