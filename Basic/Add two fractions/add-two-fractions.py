#Your task is to complete this function
#Your shouldn't return any thing it should print the required output
def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
def addFraction(num1, den1, num2, den2):
    #Code here
    num=(num1*den2)+(num2*den1)
    den=den1*den2
    gcf=gcd(num,den)
    num/=gcf
    den/=gcf
    fra=str(int(num))+"/"+str(int(den))
    print(fra)
#{ 
 # Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        arr = list(map(int, input().strip().split(' ')))
        addFraction(arr[0], arr[1], arr[2], arr[3])

# } Driver Code Ends