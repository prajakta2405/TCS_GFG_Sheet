
class Solution:
    def trappingWater(self, arr,n):
        left=[]
        right=[]
        l=arr[0]
        r=arr[n-1]
        for i in arr:
            if i >l:
                l=i
            left.append(l)
       
        
        
        for j in range(n-1,-1,-1):
            if arr[j]>r:
                r=arr[j]
                
            right.append(r)
        right=right[::-1]
       
       
        traprain=0
        for i in range(n):
            t=min(left[i],right[i])-arr[i]
            if t>0:
                traprain+=t
        return traprain
        #Code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            obj = Solution()
            print(obj.trappingWater(arr,n))
            
            
            T-=1


if __name__ == "__main__":
    main()



# } Driver Code Ends