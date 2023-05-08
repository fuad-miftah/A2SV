n , t = map(int, input().split())
cells = list(map(int, input().split()))
 
cur = 0
while cur < t-1:
    cur += cells[cur]
if cur == t-1:
    print("YES")
else:
    print("NO")