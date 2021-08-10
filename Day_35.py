print('Day 35: Check if two strings are anagram or not')

print("\n-------------Approach 1-------------")
from collections import Counter

def anagram(s1, s2):
    if Counter(s1) == Counter(s2):
        return f'{s1} & {s2} are anagram'
    return f'{s1} & {s2} are not anagram'

str1, str2 = 'smart', 'trams'
print(f'Input: String1 = {str1} & String2 = {str2}')
print('\nOutput:',anagram(str1.lower(),str2.lower()))

print("\n-------------Approach 2-------------")
def check(s1, s2):
    if sorted(s1) == sorted(s2):
        return f'{s1} & {s2} are anagram'
    return f'{s1} & {s2} are not anagram'

str3, str4 = 'smartwork', 'artworks'
print(f'Input: String1 = {str3} & String2 = {str4}')
print('\nOutput:',check(str3.lower(),str4.lower()))
