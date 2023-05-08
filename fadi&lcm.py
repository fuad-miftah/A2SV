import math
n = int(input())
res = [1,n]
 
for i in range(1,int(math.sqrt(n)) + 1):
    if n % i == 0 and (i * n // i) // math.gcd(i , n // i) == n:
        res = [i,n//i]
     
print(*res)