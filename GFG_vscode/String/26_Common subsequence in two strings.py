'''
Given two strings a and b. Check whether they contain any common subsequence (non empty) or not.

Example 1:

Input:
a = "ABEF" b = "CADE"
Output: 1
Explanation: Subsequence "AE" occurs
in both the strings.
'''

#User function Template for python3
class Solution:
	def commonSubseq(self, a, b):
	    for i in a:
	        if i in b :
	            return 1
        return 0
	        
	    
		# your code here
		


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
	t = int (input ())
	for tc in range (t):
		a, b = input().split()
		ob = Solution()
		if ob.commonSubseq (a, b):
			print (1)
		else:
			print (0)

	# Contributed By: Pranay Bansal
# } Driver Code Ends