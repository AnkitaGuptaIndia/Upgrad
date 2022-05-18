# Alphabetic patterns
# Description
# Given a positive integer 'n' less than or equal to 26, you are required to print the below pattern 
 
# Sample Input: 5 
 
# Sample Output : 
# --------e-------- 
# ------e-d-e------ 
# ----e-d-c-d-e---- 
# --e-d-c-b-c-d-e-- 
# e-d-c-b-a-b-c-d-e 
# --e-d-c-b-c-d-e-- 
# ----e-d-c-d-e---- 
# ------e-d-e------ 
# --------e-------- 

import string
n = int(input())

# Write your code below
s = string.ascii_lowercase[:n]
col = (n*2-1)*2 - 1
row = (n*2-1)

if n > 1:
    for i in range(n-1, 0, -1):
        if i != n-1:
            a = "-".join(["-".join(s[n:i:-1]), "-".join(s[i:n])])
            # a = "-".join(s[n:i:-1]) + "-" + "-".join(s[i:n])
            l = len(a)
            print("-"*(int((col-l)/2)) + a + "-"*(int((col-l)/2)))
        else:
            a = "-".join(["-".join(s[n:i:-1]), "-".join(s[i:n])])
            # a = "-".join(s[n:i:-1]) + "-" + "-".join(s[i:n])
            l = len(a)
            print("-"*(int((col-l)/2)) + a + "-"*(int((col-l)/2)) + "-")    

    for i in range(n):
        if i != n-1: 
            a = "-".join(["-".join(s[n:i:-1]), "-".join(s[i:n])])
            # a = "-".join(s[n:i:-1]) + "-" + "-".join(s[i:n])
            l = len(a)
            print("-"*(int((col-l)/2)) + a + "-"*(int((col-l)/2)))
        else:
            a = "-".join(["-".join(s[n:i:-1]), "-".join(s[i:n])])
            # a = "-".join(s[n:i:-1]) + "-" + "-".join(s[i:n])
            l = len(a)
            print("-"*(int((col-l)/2)) + a + "-"*(int((col-l)/2)) + "-")

elif n == 1:
    print('a')
