'''
Write an efficient program to print all the duplicates and their counts in the input string 

Method 1: Using hashing

Algorithm: Let input string be “geeksforgeeks” 

Construct character count array from the input string.
count[‘e’] = 4 
count[‘g’] = 2
count[‘k’] = 2 
……
Print all the indexes from the constructed array which have values greater than 1.
'''
from collections import Counter
def print_duplicate(str):
    s=Counter(str)
    for i,j in s.items():
        if j>1:
            print(f"count['{i}'] = {j}")
    
print_duplicate("geeksforgeeks")