# Problem Statement: https://codeforces.com/contest/1657/problem/A

def checkInt(num):
    if num == int(num):
        return True
    return False
    
def findDistance(x2,y2):
    x1,y1 = 0,0
    distance = ((x1-x2)**2 + (y1-y2)**2)**0.5
    return distance
 
t = int(input())
for _ in range(t):
    count = 1
    x2,y2 = map(int,input().split())
    
    # print(distance)
    if x2 == 0 and y2 == 0:
        print(0)
        continue
    distance = findDistance(x2,y2)
    while checkInt(distance):
        if (checkInt(distance)):
            print(count)
            break
    else:
        x2 -= 1
        y2 -= 1
        count += 1
        checkInt(findDistance(x2,y2))
        print(count)