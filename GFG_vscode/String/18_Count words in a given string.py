'''
Given a string consisting of spaces,\t,\n and lower case  alphabets.Your task is to count the number of words where spaces,\t and \n work as separators.
 

Example 1:

Input: S = "abc def"
Output: 2
Explanation: There is a space at 4th
position which works as a separator
between "abc" and "def"
 
'''
def countWords(s):
 
    # Check if the string is null
    # or empty then return zero
    if s.strip() == "":
        return 0
 
    # Splitting the string
 
    words = s.split()
 
    return len(words)
 
 
if __name__ == "__main__":
    s = "Oa\nhjpfo"
    print("No of words : ", countWords(s))
