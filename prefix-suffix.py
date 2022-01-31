'''
Statement:- Given a string s, find the length of the longest prefix which is also suffix. The prefix and suffix should not be overlap.
Input: abcdabc
Output: 3

Input: ababa
Output: 1
'''
s = input()
if len(s)%2==0:
    for i in range(0,len(s)//2):
        if s[:i+1:] == s[(len(s)//2):(len(s)//2)+i+1:]:
            continue
        else:
            break
else:
    for i in range(0,len(s)//2):
        if s[:i+1:] == s[(len(s)//2)+1:(len(s)//2)+i+2:]:
            continue
        else:
            break
print(i+1)
