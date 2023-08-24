#User function Template for python3

class Solution: 
    def select(self, arr, i):
    
        min_index=i
        for j in range(i,len(arr)):
            if arr[min_index]>arr[j]:
                min_index=j
                
        return min_index
            
        # code here 
    
    def selectionSort(self, arr,n):
        #code 
        for i in range(len(arr)):
            k=self.select(arr,i)
            arr[i],arr[k]=arr[k],arr[i]

        return arr
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends