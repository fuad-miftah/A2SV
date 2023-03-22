N = int(input())
for i in range(N):
    a,b = list(map(int, input().split()))
    res = (a+b)//4
    if res > min(a,b):
        print(min(a,b))
    else:
        print(res)

