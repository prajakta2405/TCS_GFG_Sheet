#User function Template for python3

class Solution:
    #Function to sort a list using quick sort algorithm.
    def quickSort(self,arr,low,high):
        if low<high:
            p=self.partition(arr,low,high)
            self.quickSort(arr,low,p-1)
            self.quickSort(arr,p+1,high)
        return arr
        # code here
    
    def partition(self,arr,low,high):
        # code here
        pindex=low
        pivot=arr[pindex]
        while low<high:
            while low<len(arr) and arr[low]<=pivot:
                low+=1
            while arr[high]>pivot:
                high-=1
            if low<high:
                arr[low],arr[high]=arr[high],arr[low]
        arr[pindex],arr[high]=arr[high],arr[pindex]
        
        return high
        
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().quickSort(arr,0,n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()

# } Driver Code Ends