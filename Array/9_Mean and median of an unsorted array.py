'''
Given an unsorted array a[] of size N, the task is to find its mean and median. 

Mean of an array = (sum of all elements) / (number of elements)

The median of a sorted array of size N is defined as the middle element when N is odd and average of middle two elements when N is even. 
Since the array is not sorted here, we sort the array first, then apply above formula.
'''
def mean_median(a):
    a.sort()
    n=len(a)
    mean=sum(a)/n
    if n%2!=0:
        d=n//2
        median=a[d]
    else:
        d=n//2
        median=(a[d]+a[d-1])/2
    print(f"mean: {mean} and median: {median}")
            
    
mean_median([1, 3, 4, 2, 6, 5, 8, 7])