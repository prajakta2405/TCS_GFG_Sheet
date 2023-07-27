'''
Given a string, find lexicographically next string.

Examples: 

Input : geeks
Output : geekt
The last character 's' is changed to 't'.

Input : raavz
Output : raawz
Since we can't increase last character, 
we increment previous character.

Input :  zzz
Output : zzza
If string is empty, we return ‘a’. If string contains all characters as ‘z’, 
we append ‘a’ at the end. Otherwise we find first character from end which is not z and increment it.
'''

def lexicographiclly(str):
    if str=="":
        return 'a'
    if str:
        n=len(str)
        count=0
        for i in str:
            if i=='z':
                count+=1
        if n==count:
            return str+'a'
        
        elif str[-1]=='z':
           s=str[:-2]+chr(ord(str[-2])+1)+str[-1]  
           return s
        else:
            s=str[:-1]+chr(ord(str[-1])+1)
            return s             
def main():
    s=""
    res=lexicographiclly(s)
    print(res)
    
if __name__=="__main__":
    main()