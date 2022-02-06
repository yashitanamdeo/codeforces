from math import ceil
n,m,a = map(int,input().split())
A = ceil(n/a) #first interation flags
B = ceil(m/a) #iteration length
print(int(A*B))