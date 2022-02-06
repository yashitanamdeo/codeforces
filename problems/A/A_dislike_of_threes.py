t = int(input())
for i in range(t):
    lis = []
    n = int(input())
    i = 1
    count = 1
    while count <= n:
        if i%3!=0 and i%10!=3:
            lis.append(i)
            count += 1
        i += 1
    print(lis[-1])