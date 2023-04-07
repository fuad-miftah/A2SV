n = int(input())
matrix = []
sources = []
sinks = []
for i in range(n):
    r = list(map(int, input().split()))
    j = 0
    while j < len(r):
        if r[j] != 0:
            break
        j += 1
    if j == len(r):
        sinks.append(i+1)
    matrix.append(r)
for i in range(len(matrix[0])):
    j = 0
    while j < len(matrix):
        if matrix[j][i] != 0:
            break
        j += 1
    if j == len(matrix):
        sources.append(i+1)
print(len(sources), *sources)
print(len(sinks), *sinks)