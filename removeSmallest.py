t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    cont = True
    while cont and len(arr) > 1:
        if arr[-1] <= arr[-2] + 1:
            arr.pop()
        else:
            cont = False
    if len(arr) > 1:
        print("NO")
    else:
        print("YES")