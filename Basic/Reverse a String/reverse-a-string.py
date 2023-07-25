#User function Template for python3

def reverseWord(s):
    #your code here
    i=len(s)-1
    
    res=[]
    while  i>=0:
        
        res.append(s[i])
        i-=1
        
        
    return ''.join(res)
        
    #return(s[::-1])


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while(t>0):
        s = input()
        print(reverseWord(s))
        t = t-1

# } Driver Code Ends