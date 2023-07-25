'''
Given a string and the task is to count vowels, consonant, digits and special character in string. 
Special character also contains the white space.
Examples: 
 

Input : str = "geeks for geeks121"
Output : Vowels: 5
         Consonant: 8
         Digit: 3
         Special Character: 2

Input : str = " A1 B@ d  adc"
Output : Vowels: 2
         Consonant: 4
         Digit: 1
         Special Character: 6
'''
def count_vowels(s):
    vowels=['a','e','i','o','u','A','E','I','O','U']
    count_v=0
    count_c=0
    count_d=0
    count_s=0
    
    for i in s:
        if i in vowels:
            count_v+=1
        else:
            if (65<= ord(i) <=90 or 97<= ord(i) <=122) and i not in vowels:
                count_c+=1
            elif 48<= ord(i) <=57:
                count_d+=1
            else:
                count_s+=1
    print(f"vowels: {count_v} ,  consonents: {count_c}, digits: {count_d}, special: {count_s}")
    
    
def main():
    s="geeks for geeks121"
    count_vowels(s)
if __name__=="__main__":
    main()
              
