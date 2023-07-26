'''
Given the string, the task is to capitalise the first and last character of each word in a string.
Examples: 
 

Input: Geeks for geeks
Output: GeekS FoR GeekS

Input: Geeksforgeeks is best
Output: GeeksforgeekS IS BesT
'''
'''def cpitalize(s):
    res=s.split()
    res1=[]
    for i in res:
        n=len(i)
        if n==1:
            x=i[0].upper()
        else:
            x=i[0].upper()+i[1:-1]+i[-1].upper()
        res1.append(x)
    res1=''.join(res1)
    print(res1)
        
        
        
    
cpitalize("Geeks for geeks")'''
s = "welcome to geeksforgeeks"
print("String before:", s)
a = s.split()
res = []
for i in a:
    if len(i)==1:
        x=i[0].upper()
    else:
        x = i[0].upper()+i[1:-1]+i[-1].upper()
    res.append(x)
res = " ".join(res)
print("String after:", res)

