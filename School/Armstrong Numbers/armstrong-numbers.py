#User function Template for python3

#User function Template for python3
class Solution:
    def armstrongNumber (self, n):
        # code here 
        s=str(n)
        di=len(s)
        sum1=0
        n1=n
        while n>0:
            d=n%10
            sum1+=(d**di)
            n=n//10
            
        if n1==sum1:
            return "Yes"
        else:
            return "No"
            
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = input()
        n=int(n)
        ob = Solution()
        print(ob.armstrongNumber(n))
# } Driver Code Ends