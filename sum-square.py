'''
Statement:
Take input from the user in the given format(consist of name and code).
Find the sum of square of digits from code. If the sum of squares of digits of the code are:
    -- Even:- Then add the last 2 characters in the beginning.
    -- Odd:-  Then add first character at the end.
    
Input: abcd:1234,bcdgfgf:127836,sdjks:1245
Output: cdab cdgfhfb kssdj
'''

l=list(map(str,input().split(",")))
ans=[]
for i in range(len(l)):
    name,digit = l[i].split(":")
    sums = 0
 
    for j in digit:
        sums = sums + int(j)**2
    if sums%2 == 0:
        ans.append(name[-2::]+name[:-2:])
    else:
        ans.append(name[1::]+name[:1:])
print(' '.join(ans))
