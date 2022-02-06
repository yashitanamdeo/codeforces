# Problem Statement: https://codeforces.com/problemset/problem/231/A

solve_count = 0
for _ in range(int(input())):
    petya,vasya,tonya = map(int,input().split())
    if petya+vasya+tonya >=2:
        solve_count += 1
print(solve_count)