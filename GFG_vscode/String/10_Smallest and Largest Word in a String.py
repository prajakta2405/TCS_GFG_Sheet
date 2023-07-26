'''
Given a string, find the minimum and the maximum length words in it. 

Examples: 

Input : "This is a test string"
Output : Minimum length word: a
         Maximum length word: string

Input : "GeeksforGeeks A computer Science portal for Geeks"
Output : Minimum length word: A
         Maximum length word: GeeksforGeeks
'''
def max_min_word(s):
    res=s.split()
    d=[]
    
    for i in res:
        d.append(len(i))
    hash=dict(zip(res,d))    
    a=max(hash.values())
    b=min(hash.values())
    for i in res:
        if hash[i]==b:
            print(i)
        if hash[i]==a:
            print(i)
            
if __name__=="__main__":
    s="This is a test string"
    max_min_word(s)