
class Solution:
    
    #Function to calculate sum of all numbers present in a string.
    def findSum(self,s):
        #code here
        num=0
        sum1=0
        for i in range(len(s)):
            
            if 48 <= ord(s[i])  <=57:
                num= num*10 +(ord(s[i])-48)
                
            elif num !=0:
                sum1+=num
                num=0
                 
        sum1+=num   
            
        return sum1
