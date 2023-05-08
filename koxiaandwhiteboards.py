import heapq
t = int(input())
for _ in range(t):
    n,m = map(int, input().split())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    heapq.heapify(arr1)
    while arr2:
        heapq.heappop(arr1)
        heapq.heappush(arr1,arr2.pop(0))
 
    print(sum(arr1))