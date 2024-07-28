# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
                
        ## Function to check if current path has a permutation that's a palindrome
        def isPalindromicPath(palinArr: [int]) -> bool:
            hasSeenFirstOdd: bool = False
            for i in range(0, len(palinArr)):
                if(palinArr[i] % 2 == 1):
                    if hasSeenFirstOdd: return False
                    hasSeenFirstOdd = True
            return True
    
        ## Wrapper for function that calculates the number of pseudo palindromic paths
        def calcPalindromicPaths(root: Optional[TreeNode], arr: [int]) -> int:
            
            count: int = 0
            if root == None: return 0
            arr[root.val] += 1
            
            ## Leaf Node: No children
            if(root.left == None and root.right == None):
                if(isPalindromicPath(arr)): count = 1
            
            if(root.left != None): count += calcPalindromicPaths(root.left, arr)
            if(root.right != None): count += calcPalindromicPaths(root.right, arr)
                
            arr[root.val] -= 1
            return count; 
        
        
        dparr: [int] = [0] * 10
        return calcPalindromicPaths(root, dparr)
        