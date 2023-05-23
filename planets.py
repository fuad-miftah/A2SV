from collections import Counter
t = int(input())
for _ in range(t):
    n,k = map(int, input().split())
    arr = list(map(int, input().split()))
    count = Counter(arr)
    ans = 0
    for key in count:
        if count[key] > k:
            ans += k
        else:
            ans += count[key]
    print(ans)