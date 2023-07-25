#User function Template for python3
class Solution:

	def equilibrium(self,arr, n): 
    	# code here
    	left_sum=0
                
        sum_a=sum(arr)
            
                
        for i in range(n):
            sum_a -=arr[i]
                
                    
            if left_sum == sum_a :
                return 'YES'
            left_sum += arr[i]
                        
        return 'NO'


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

	
	tc=int(input())
	while tc > 0:
	    n=int(input())
	    a=list(map(int , input().strip().split()))
	    ob = Solution()
	    ans=ob.equilibrium(a, n)
	    print(ans)
	    tc=tc-1
# } Driver Code Ends