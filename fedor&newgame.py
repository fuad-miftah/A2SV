n, m ,k = map(int, input().split())
nums = []
for i in range(m+1):
    nums.append(int(input()))
 
fedor = nums[-1]
res = 0
for i in range(len(nums)-1):
    friend = nums[i]
    cur = fedor ^ friend
    dif = 0
    
    while cur:
        dif += cur & 1
        cur >>= 1
    if dif <= k:
        res += 1
print(res)