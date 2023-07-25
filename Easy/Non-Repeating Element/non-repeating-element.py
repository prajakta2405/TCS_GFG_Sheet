#User function Template for python3

#User function Template for python3

class Solution:
    def firstNonRepeating(self, arr, n): 
        # Complete the function
        hash={}
        for i in arr:
            if i in hash:
                hash[i]+=1
            else:
                hash[i]=1
                
        for i,j in enumerate(arr):
            if hash[j]==1:
                return arr[i]
        





#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import defaultdict 

for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    print(ob.firstNonRepeating(arr, n))
    
# } Driver Code Ends