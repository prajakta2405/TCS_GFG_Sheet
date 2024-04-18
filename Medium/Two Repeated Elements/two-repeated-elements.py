#User function Template for python3

class Solution:
    
    #Function to find two repeated elements.
    def twoRepeated(self, arr , n):
        nums=set()
        res=[]
        for i in arr:
            if i in nums:
                res.append(i)
            else:
                nums.add(i)
        return res
        
       

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            obj = Solution()
            ans = obj.twoRepeated(A,N)
            print(ans[0], ans[1])
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends