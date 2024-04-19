# User function Template for Python3

class Solution:
    def leftSmaller(self, n, arr):
        stack=[]
        res=[]
        for i in range(n):
            if not stack:
                res.append(-1)
            elif stack and stack[-1]<arr[i]:
                res.append(stack[-1])
            elif stack and stack[-1]>=arr[i]:
                while (stack and stack[-1]>=arr[i]):
                    stack.pop()
                if not stack:
                    res.append(-1)
                else:
                    res.append(stack[-1])
            stack.append(arr[i])
        return res


#{ 
 # Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = input().split()
        for i in range(n):
            a[i] = int(a[i])
        
        ob = Solution()
        ans = ob.leftSmaller(n, a)
        for u in(ans):
            print(u,end = " ")
        print()
# } Driver Code Ends