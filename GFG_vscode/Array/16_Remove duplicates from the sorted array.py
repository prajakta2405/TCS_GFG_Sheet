'''

'''
#User function template for Python

class Solution:	
	def remove_duplicate(self, A, N):
		# code here
		i=0
		j=1
		while j<len(A):
		    if A[i]==A[j]:
		        A.pop(j)
	        else:
	            j+=1
	            i+=1
	    return len(A)
		


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        N = int(input())
        A = list(map(int, input().strip().split()))
        ob = Solution()
        n = ob.remove_duplicate(A,N)
        for i in range(n):
            print(A[i], end=" ")
        print()


# } Driver Code Ends#User function template for Python

class Solution:	
	def remove_duplicate(self, A, N):
		# code here
		i=0
		j=1
		while j<len(A):
		    if A[i]==A[j]:
		        A.pop(j)
	        else:
	            j+=1
	            i+=1
	    return len(A)
		


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        N = int(input())
        A = list(map(int, input().strip().split()))
        ob = Solution()
        n = ob.remove_duplicate(A,N)
        for i in range(n):
            print(A[i], end=" ")
        print()


# } Driver Code Ends