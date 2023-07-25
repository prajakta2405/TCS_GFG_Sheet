'''
Given a string S, remove all the characters other than the alphabets.

Example 1:

Input: S = "$Gee*k;s..fo, r'Ge^eks?"
Output: GeeksforGeeks
Explanation: Removed charcters other than
alphabets. 
'''
class Solution:
    def removeSpecialCharacter (self, S):
		#code here
		res=""
		for i in S:
		    if 65<= ord(i) <=90 or 97 <= ord(i) <=122:
		        res+=i
		if len(res)>0:
		    return res
		else:
		    return -1