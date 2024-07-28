class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        m,n = len(arr),len(arr[0])
        if m==0 or n==0:return 0
        dp = [[None]*n for r in range(m)]
        
        for i in range(m):
            for j in range(n):
				#base case
                if i==0:dp[i][j] = arr[i][j]
				#when there is only one column
                elif j==0 and j==n-1:dp[i][j] = arr[i][j]+dp[i-1][j]
				#when it is first column, (column-1) will out of bound
                elif j==0:dp[i][j] = min(dp[i-1][j],dp[i-1][j+1])+arr[i][j]
				#when it is last column, (column+1) will out of bound
                elif j==n-1:dp[i][j] = min(dp[i-1][j],dp[i-1][j-1])+arr[i][j]
				#choose min from all of three
                else:dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i-1][j+1])+arr[i][j]
		#atlast return minimum from last row
        return min(dp[-1])
        