t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    maximum = []
    cur = nums[0]
    for i in range(1,len(nums)):
        if (cur > 0 and nums[i] > 0) or (cur < 0 and nums[i] < 0):
            cur = max(cur, nums[i])
        else:
            maximum.append(cur)
            cur = nums[i]
    maximum.append(cur)
    print(sum(maximum))