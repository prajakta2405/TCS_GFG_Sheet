'''
Given a string, remove the vowels from the string.

Example 1:

Input: S = "welcome to geeksforgeeks"
Output: wlcm t gksfrgks
Explanation: Ignore vowels and print other
characters 
'''
#User function Template for python3
class Solution:
	def removeVowels(self, S):
		# code here
		res=""
		vowels=['a','e','i','o','u','A','E','I','O','U']
		for i in S:
		    if i not in vowels:
		        res+=i
		return res
		        
		        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		
		ob = Solution()	
		answer = ob.removeVowels(s)
		
		print(answer)


# } Driver Code Ends