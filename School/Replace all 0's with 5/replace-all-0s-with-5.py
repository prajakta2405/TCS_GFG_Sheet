#function should return an integer
#your task is to compplete this function
class Solution:
    def convertFive(self,n):
        #Code here
        s=str(n)
        res=[]
        for i in s:
            if i=='0':
                res.append('5')
            else:
                res.append(i)
        return ''.join(res)

#{ 
 # Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n=int(input())
        print(Solution().convertFive(n))
# Contributed by: Harshit sidhwa

# } Driver Code Ends