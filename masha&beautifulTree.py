def mergeSort(nums):
    if len(nums) == 1:
        return nums, 0
    if len(nums) == 2:
        if nums[0] > nums[1]:
            return [nums[1], nums[0]], 1
        return nums, 0
    l = mergeSort(nums[:len(nums) // 2])
    r = mergeSort(nums[len(nums) // 2:])
    if l[0][-1] < r[0][0]:
        return l[0] + r[0], l[1] + r[1]
    return r[0] + l[0], l[1] + r[1] + 1
 
 
testcases = int(input())
for _ in range(testcases):
    n = int(input())
    nums = list(map(int, input().split()))
    arr, moves = mergeSort(nums)
    check = True
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            check = False
            break
    if check:
        print(moves)
    else:
        print(-1)