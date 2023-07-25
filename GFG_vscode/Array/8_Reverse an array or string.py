def reverseWord(s):
    
    i=len(s)-1
    
    res=[]
    while  i>=0:
        
        res.append(s[i])
        i-=1
       
        
    return ''.join(res)
def main():
    s='Geeks'
    a=reverseWord(s)
    print(a)
    
if __name__=="__main__":
    main()