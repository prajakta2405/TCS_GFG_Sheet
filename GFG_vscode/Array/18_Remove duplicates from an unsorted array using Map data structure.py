#User function Template for python3
from collections import Counter
class Solution:
    def removeDuplicate(self, A, N):
        # code here
        hash={}
        res=[]
        for i in A:
            if i in hash:
                hash[i]+=1
            else:
                hash[i]=1
        for i in A:
            if hash[i]>1:
                res.append(i)
                hash[i]=0
            elif hash[i]==0:
                continue
            else:
                res.append(i)
        return res
    




#{ 
 # Driver Code Starts
#Initial Template for Python 3



def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        getAnswer = ob.removeDuplicate(a, n)
        
        print(*getAnswer)

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends