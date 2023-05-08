t = int(input())
for _ in range(t):
    n , x = map(int, input().split())
    nums = list(map(int, input().split()))
    res = ((x + 1) * (x)) // 2
    for num in nums:
        if num <= x:
            res -= 2 * num
    print(res)