t = int(input())
for i in range(t):
    n = input()
    nums = list(map(int, input().split()))
    s = 0
    for j in range(len(nums)):
        s ^ nums[j]
    for k in range(len(nums)):
        if s ^ nums[k] == nums[k]:
            print(nums[k])
            break