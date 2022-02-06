n = int(input())
for _ in range(n):
    word = input()
    if len(word) > 10:
        print(word[0],len(word)-2,word[-1], sep="")
    else:
        print(word)