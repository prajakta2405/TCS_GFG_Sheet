'''
Given two strings a and b consisting of lowercase characters. The task is to check whether two given strings are an anagram of each other or not. An anagram of a string is another string that contains the same characters, only the order of characters can be different. For example, act and tac are an anagram of each other.

Note:-

If the strings are anagrams you have to return True or else return False

|s| represents the length of string s.


Example 1:

Input:a = geeksforgeeks, b = forgeeksgeeks
Output: YES
Explanation: Both the string have same characters with
        same frequency. So, both are anagrams.
'''
#User function Template for python3

from collections import Counter
class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def isAnagram(self,a,b):
        map=dict()
        for i in a:
            map[i]=map.get(i,0)+1
        for i in b:
            map[i]=map.get(i,0)-1
        for i in map.keys():
            if map[i]!=0:
                return False
        return True
                