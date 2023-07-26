'''
Given a string, convert the characters of the string into the opposite case,i.e. 
if a character is the lower case then convert it into upper case and vice-versa. 

Examples: 

Input : geeksForgEeks
Output : GEEKSfORGeEKS

Input : hello every one
Output : HELLO EVERY ONE
'''
def change_case(s):
    res=[]
    for i in s:
        if 65 <= ord(i) <=90:
            res.append(i.lower())
        else:
            res.append(i.upper())
    print( ''.join(res))
change_case("eeksForgEeks")
        
