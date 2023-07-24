# Find the first non-repeating element in a given array arr of N integers.

#User function Template for python3


from collections import Counter
class Solution:
    def firstNonRepeating(self, arr, n): 
        # Complete the function
        
        l=Counter(arr)
        for num in arr:
            if l[num]==1:
                return num
       
        return 0
        
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