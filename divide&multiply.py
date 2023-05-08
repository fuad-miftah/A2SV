import math
t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    res = sum(arr)
    
    cont = True
    firstEven = -1
    arr.sort()
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            firstEven = i
            break
    if firstEven == -1:
        cont = False
    if len(arr) > 1:
        while cont:
            if firstEven != len(arr) -1 :
                arr[-1] = arr[-1] * 2
                arr[firstEven] = arr[firstEven] // 2
 
                arr.sort()
                res = max(res, sum(arr))
                firstEven = -1
                for i in range(len(arr)):
                    if arr[i] % 2 == 0:
                        firstEven = i
                        break
 
                if firstEven == len(arr)-1:
                    curr = arr[-1]
                    nextM = arr[-2]
 
                    count = 0
                    while curr % 2 == 0 and curr > 1:
                        count += 1
                        curr = curr // 2
 
                    if nextM * (2 ** count) < arr[-1]:
                        cont = False
            else:
                curr = arr[-1]
                nextM = arr[-2]
 
                count = 0
                while curr % 2 == 0 and curr > 1:
                    count += 1
                    curr = curr // 2
 
                arr[-1] = curr
                arr[-2] = nextM * (2 ** count)
                arr.sort()
                res = max(res, sum(arr))
                for k in range(len(arr)):
                    if arr[k] % 2 == 0:
                        firstEven = k
                        break
 
                cont = False
                    
            
        print(res)
    else:
        print(arr[0])