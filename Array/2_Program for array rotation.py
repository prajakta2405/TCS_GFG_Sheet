#Given an unsorted array arr[] of size N. Rotate the array to the left 
#(counter-clockwise direction) by D steps, where D is a positive integer. 
#User function Template for python3

class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self,A,D,N):
        #Your code here
        p=1
        
        while (p<=D):
            last=A[0]
            for i in range(N-1):
                A[i]=A[i+1]
            A[N-1]=last
            p+=1
        return A
       
        
        



#second approach
#User function Template for python3
from collections import deque
class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self,A,D,N):
        #Your code here
        '''D=D%N
        A[:]=A[D:N]+A[0:D]
        return A'''
        d=deque(A)
        d.rotate(-D)
        for i in range(N):
            A[i]=d[i]
        return A
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
def main():
    T=int(input())
    
    while(T>0):
        nd=[int(x) for x in input().strip().split()]
        N=nd[0]
        D=nd[1]
        A=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.rotateArr(A,D,N)
        
        for i in A:
            print(i,end=" ")
            
        print()
       
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends