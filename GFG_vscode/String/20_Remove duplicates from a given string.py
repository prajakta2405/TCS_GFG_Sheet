'''
Given a string Str which may contains lowercase and uppercase chracters. The task is to remove all duplicate characters from the string and find the resultant string. The order of remaining characters in the output should be same as in the original string.

Example 1:

Input:
Str = geeksforgeeks
Output: geksfor
Explanation: After removing duplicate
characters such as e, k, g, s, we have
string as "geksfor".
'''
#User function Template for python3
from collections import Counter
class Solution:

	def removeDuplicates(self,str):
	    c=Counter(str)
	    s=''.join(c.keys())
	    return s
	    
    def removeDuplicates(self,str):
	    res=""
	    for i in str:
	        if i not in res:
	            res+=i
        return res
	    
	    
	    # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3





if __name__ == '__main__':
    
    str = "geeksforgeeks"
    ob = Solution()
    ans = ob.removeDuplicates(str)
    print(ans)
   

# } Driver Code Ends
