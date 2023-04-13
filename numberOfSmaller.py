n, m = list(map(int, input().split()))
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
l1 = 0
l2 = 0
res = []
while l2 < m:
    while l1 < n and arr1[l1] < arr2[l2]:
        l1 += 1
    res.append(l1)
 
    l2 += 1
 
print(*res)