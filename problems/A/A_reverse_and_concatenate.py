# Problem Statement: https://codeforces.com/contest/1634/problem/A

def isPalindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False
    
t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    s = str(input())
    
    if k == 0:
        print(1)
    if k == 1:
        if isPalindrome(s):
            print(1)
        else:
            print(2)
    if k > 1:
        if isPalindrome(s):
            print(1)
        else:
            print(2)