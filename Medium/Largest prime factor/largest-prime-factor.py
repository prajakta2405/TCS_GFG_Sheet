#User function Template for python3
import math
class Solution:
    def largestPrimeFactor (self, N):
        res=[]
        while N%2==0:
            res.append(2)
            N//=2
            
        for i in range(3,int(math.sqrt(N))+1,2):
            while N%i==0:
                res.append(i)
                N//=i
                
        if N>2:
            return N
        return max(res)
        # code here
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.largestPrimeFactor(N))
# } Driver Code Ends