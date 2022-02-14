'''Q1. Given two numbers N and M and an array of size N.
A triplet is defined if it satisfies any one of the following conditions:

All the numbers in the triplets are equal. [Eg, (1,1,1)]
The numbers are consecutive. [Eg, (1, 2, 3)]
Given the array, find the maximum number of triplets that can be formed. All elements of the array are <= M.

Note: Each element of the array can only be a part of one triplet.

Constraints:
1 <= N <= 10^5
1 <= M <= 10^4
1 <= arr[i] <= M
'''

def triplets(l):
    l.sort()
    i = 0
    cout,c = 0,1 
    while(i<len(l)):
        try:
            if l[i] == l[i+1]  and l[i+2] == l[i]:
                cout+= 1
                if i+3 <len(l):
                    i = i+3 
                else:
                    break
                continue
        except:
            pass
        try:
            if l[i]+1 == l[i+1] and l[i]+2 == l[i+2]:
                cout+= 1 
                if i+3 <len(l):
                    i=i+3
                else:
                    break
                continue
        except:
            pass
        i+=1
    return cout
arr = [1,2,2,2,5,8,9,10,11,12]
print(triplets(arr))
