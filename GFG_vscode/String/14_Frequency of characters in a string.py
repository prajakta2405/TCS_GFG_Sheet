'''
iven a string, The task is to count the number of alphabets present in the string.

Example 1:

Input:
S = "adjfjh23"
Output: 6
Explanation: only last 2 are not 
alphabets.
'''
#User function Template for python3

class Solution:

    def Count(self, S):
        # code here
        count=0
        s=S.lower()
        for i in s:
            if 97 <= ord(i) <= 122:
                count+=1
                
        return count
