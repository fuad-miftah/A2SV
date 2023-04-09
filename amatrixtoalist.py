n = int(input())
count = 0
for i in range(n):
    row = list(map(int,input().split()))
    res = []
    for i in range(len(row)):
        if row[i] == 1:
            res.append(i+1)
    print(len(res),*res)
