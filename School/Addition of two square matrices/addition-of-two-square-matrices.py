#User function Template for python3

class Solution:
	def Addition(self, matrixA, matrixB):
	    for i in range(len(matrixA[0])):
	        for j in range(len(matrixB[0])):
	            matrixA[i][j]+=matrixB[i][j]
	            
	    return matrixA
	    
		# Code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		matrixA = []
		matrixB = []
		for _ in range(n):
			matrixA.append(list(map(int,input().split())))
		for _ in range(n):
			matrixB.append(list(map(int,input().split())))
		ob = Solution()
		ob.Addition(matrixA, matrixB)
		for i in range(n):
			for j in range(n):
				print(matrixA[i][j], end = " ")
			print()
# } Driver Code Ends