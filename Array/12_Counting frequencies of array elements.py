'''
Given an array A[] of N positive integers which can contain integers from 1 to P where elements can be repeated or can be absent from the array. Your task is to count the frequency of all elements from 1 to N.
Note: The elements greater than N in the array can be ignored for counting and do modify the array in-place.


Example 1:

Input:
N = 5
arr[] = {2, 3, 2, 3, 5}
P = 5
Output:
0 2 2 0 1
Explanation: 
Counting frequencies of each array element
We have:
1 occurring 0 times.
2 occurring 2 times.
3 occurring 2 times.
4 occurring 0 times.
5 occurring 1 time.
'''


    
def frequencyCount( arr, N, P):
    # code here
    
    hash={}
    for i in range(1,N+1):
        hash[i]=0
    
    for num in arr:
        if num in hash:
            hash[num]+=1
            
    #return list(hash.keys())
    return list(hash.values())

'''dict=Counter(arr)
        for i in range(1,N+1):
            if i in dict:
                arr[i-1]=dict[i]
            else:
                arr[i-1]=0
        return arr'''
def main():
    N = 5
    arr= [2, 3, 2, 3, 5]
    P = 5
    res=frequencyCount(arr,N,P)
    print(res)
    
if __name__=="__main__":
    main()
                    
            
            
            



