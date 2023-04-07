from collections import defaultdict
v = int(input())
k = int(input())
adjacency_list = defaultdict(list)

for i in range(k):
    r = list(map(int, input().split()))
    if r[0] == 2:
        print(*adjacency_list[r[1]])
    else:
        adjacency_list[r[1]].append(r[2])
        adjacency_list[r[2]].append(r[1])