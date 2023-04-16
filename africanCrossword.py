import copy
n , m = list(map(int, input().split()))
matrix = []
for _ in range(n):
    arr = input()
    #arr = list(input().split())
    matrix.append(list(arr))
matrix2 = copy.deepcopy(matrix)
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        cur = matrix[i][j]
    
        for col in range(len(matrix[0])):
            if col != j and matrix2[i][col] == cur:
                matrix2[i][j] = 0
                matrix2[i][col] = 0
        for row in range(len(matrix)):
            if row != i and matrix2[row][j] == cur:
                matrix2[row][j] = 0
                matrix2[i][j] = 0
                
res = ""
 
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix2[i][j] != 0:
            res += matrix2[i][j]
            
print(res)