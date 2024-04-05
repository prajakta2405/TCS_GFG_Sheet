
    
    
#User function Template for python3

def minAnd2ndMin( a, n):
    #code here
    s=list(set(a))
    s.sort()
    n1=len(s)
    if n1 >=2:
        return s[0],s[1]
    else:
        return -1,-1
 
    






#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        
        product = minAnd2ndMin(a, n)
        if product[0]==-1:
            print(product[0])
        else:
            print(product[0], end=" ")
            print(product[1])

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends