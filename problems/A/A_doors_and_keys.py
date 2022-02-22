# Problem Statement: https://codeforces.com/contest/1644/problem/A

t = int(input())
for _ in range(t):
    string = input()
    hashmap = []   #to store keys
    ans = []  #if door can open -> append true else append false
    for i in range(len(string)):
        if string[i] == 'R':
            if 'r' not in hashmap: # door came before collecting key
               ans.append('False') # hence cannot open door
        if string[i] == 'G':
            if 'g' not in hashmap:
                ans.append('False')
        if string[i] == 'B':
            if 'b' not in hashmap:
                ans.append('False')
        else:
            hashmap.append(string[i]) #store keys in hashmap
    #print(hashmap)
    if 'False' in ans: # if any door could not open
        print("NO")
    else:
        print("YES") # all door came after collecting key