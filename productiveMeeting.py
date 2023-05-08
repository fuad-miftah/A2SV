import heapq
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr2 = []
    for i, num in enumerate(arr):
        if num > 0:
            arr2.append((-1 * num,i))
    
    heapq.heapify(arr2)
    res = []
    while len(arr2) > 1:
        n1 = heapq.heappop(arr2)
        n2 = heapq.heappop(arr2)
        res.append((n1[1], n2[1]))
        if n1[0] + 1 != 0:
            heapq.heappush(arr2, (n1[0] + 1, n1[1]))
        if n2[0] + 1 != 0:
            heapq.heappush(arr2, (n2[0] + 1, n2[1]))
       
        
    print(len(res))
    for a, b in res:
        print(a+1,b+1)