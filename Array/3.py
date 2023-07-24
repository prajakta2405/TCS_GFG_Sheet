# Given an array A of n positive numbers. The task is to find the first Equilibrium Point in an array. 
#Equilibrium Point in an array is a position such that the sum of elements before it is equal to the sum of elements after it.

class Solution:
    # Complete this function
    
    #Function to find equilibrium point in the array.
    def equilibriumPoint(self,A, N):
        '''left_sum=0
        right_sum=0
        
        if N==1:
            return N
            
        else:
            for i in range(1,N):
                for j in range(0,i):
                    left_sum +=A[j]
                
                for  k in range(i+1,N):
                    right_sum+=A[k]
                if left_sum ==right_sum:
                    return i+1
                
            
                left_sum=0
            
                right_sum=0
        return -1'''

        #approch second
        left_sum=0
                
        sum_a=sum(A)
            
                
        for i in range(N):
            sum_a -=A[i]
                
                    
            if left_sum == sum_a :
                return i+1
            left_sum += A[i]
                        
            return -1



#{ 
 # Driver Code Starts
# Initial Template for Python 3

import math


def main():

    T = int(input())

    while(T > 0):

        N = int(input())

        A = [int(x) for x in input().strip().split()]
        ob=Solution()

        print(ob.equilibriumPoint(A, N))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends