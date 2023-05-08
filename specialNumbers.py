t = int(input())
for i in range(t):
    n,k = list(map(int, input().split()))
    res = 0
    count = 0
    while k > 0:
        if k & 1:
            res += n ** count
        count+=1
        k >>= 1
    print(res % (10  ** 9 + 7))