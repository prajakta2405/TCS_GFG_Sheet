#User function Template for python3

class Solution:
    def merge(self,arr, l, mid, r): 
        i,j = l,mid+1
        x=0
        temp=[0]*(r-l+1)
        
        while i<=mid and j<=r:
            if arr[i]>=arr[j]:
                temp[x]=arr[j]
                x+=1
                j+=1
            else:
                temp[x]=arr[i]
                x+=1
                i+=1
        
        while i<=mid:
            temp[x]=arr[i]
            x+=1
            i+=1
        
        while j<=r:
            temp[x]=arr[j]
            x+=1
            j+=1
        
        i=l
        for e in temp:
            arr[i]=e
            i+=1
            
    def mergeSort(self,arr, l, r):
        if l<r:
            m=(l+r)//2
            
            self.mergeSort(arr,l,m)
            #print("mergeSort(arr,l,m): ",l,m,r)
            
            self.mergeSort(arr,m+1,r)  
            #print("mergeSort(arr,m+1,r): ",l,m,r)
            
            self.merge(arr,l,m,r)
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3


import sys
input = sys.stdin.readline
if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().mergeSort(arr, 0, n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends