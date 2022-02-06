t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    print(max(a[i-1]*a[i] for i in range(1,n)))