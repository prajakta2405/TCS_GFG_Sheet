
#Given two arrays: a1[0..n-1] of size n and a2[0..m-1] of size m. Task is to check whether a2[] is a subset of a1[] or not. Both the arrays can be sorted or unsorted. There can be duplicate elements.

def isSubset( a1, a2, n, m):


#First approach
    '''hash_map=set()
    
    for i in range(0,n):
        hash_map.add(a1[i])
           
    for  i in range(0,m):
        if a2[i] in hash_map:
            continue 
        
        else:
            return ("No")
            
    return("Yes")'''

# second approach
    
    '''frequency={}
    
    for i in range(n):
        if a1[i] in frequency:
            frequency[a1[i]]+=1
        else:
            frequency[a1[i]]=1
            
    for i in range(m):
        if a2[i] in frequency:
            
            frequency[a2[i]]-=1
            
        else:
            return ("No")
            
    return ("Yes")'''
        
    
    for i in range(m):
        if (a2[i] not in a1):
            return "No"
            
        else:
            a1.remove(a2[i])
            
    return "Yes"
    
    
    
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m = sz[0], sz[1]
        a1 = [int(x) for x in input().strip().split()]
        a2 = [int(x) for x in input().strip().split()]
        
        print(isSubset( a1, a2, n, m))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends