'''
You are given a string s. You need to reverse the string.

Example 1:

Input:
s = Geeks
Output: skeeG
'''
i=len(s)-1
    
    res=[]
    while  i>=0:
        
        res.append(s[i])
        i-=1
        
        
    return ''.join(res)
        