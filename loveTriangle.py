from collections import defaultdict
n = int(input())
planes = list(map(int, input().split()))
 
dic = defaultdict(list)
for i in range(1,n+1):
    dic[i] = planes[i-1]
 
 
i = 0
while i < n:
    first = dic[i+1]
    second = dic[first]
    third = dic[second]
    if third == i + 1:
        print("YES")
        break
    i += 1
 
if i == n:
    print("NO")