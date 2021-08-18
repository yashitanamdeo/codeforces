t = int(input())
for i in range(t):
    a,b,c = map(int,input().split())
    num = 2*abs(b-a)
    ans = 0
    
    if (b>num or a>num or c>num):
        ans -= 1
    else:
        ans = c + num/2
        if ans>num:
            ans = c - num/2
    print(int(ans))