#User function Template for python3
import math
class Solution:
    def countFactors (self, N):
        # code here
        fact=[]
        for i in range(1,int(math.sqrt(N))+1):
            if N%i==0:
                if N//i==i:
                    fact.append(i)
                else:
                    fact.append(i)
                    fact.append(N//i)
        return len(fact)


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.countFactors(N))
# } Driver Code Ends