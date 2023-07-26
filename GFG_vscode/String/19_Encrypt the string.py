'''
Bingu was testing all the strings he had at his place and found that most of them were prone to a vicious attack by Banju, his arch-enemy. Bingu decided to encrypt all the strings he had, by the following method. Every substring of identical letters is replaced by a single instance of that letter followed by the number of occurrences of that letter. Then, the string thus obtained is further encrypted by reversing it.

Example 1:

Input:
s = "aabc"
Output: 1c1b2a
Explanation: aabc
Step1: a2b1c1
Step2: 1c1b2a
'''
#User function Template for python3
from collections import Counter
class Solution:

    def encryptString(self, s):
        # code here
        res=[]
        s=Counter(s)
        for i ,j in s.items():
            res.append(i)
            res.append(str(j))
        s1=''.join(res)
            
        return s1[::-1]
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    
        s = "aabc"

        solObj = Solution()

        print(solObj.encryptString(s))
# } Driver Code Ends