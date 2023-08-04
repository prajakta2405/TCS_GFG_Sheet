#User function Template for python3

class Solution:
    def shouldPunish (self, roll, marks, n, avg):
        #  your code here
        swap=0
        for  i in range(n):
            
            for j in range(i+1,n):
                if roll[j]<roll[i]:
                    roll[i],roll[j]=roll[j],roll[i]
                    swap+=2
                   
        sum_mark=sum(marks)
        avgg=(sum_mark-swap)/n
        if avgg>avg:
            return 1
        else:
            return 0

#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    n, avg = input ().split ()
    n = int (n)
    avg = float (avg)
    roll = list(map(int, input().split()))
    marks = list(map(int, input().split()))
    ob=Solution()
    print (ob.shouldPunish (roll, marks, n, avg))
# } Driver Code Ends