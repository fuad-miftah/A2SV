#class Solution(object):
def square(m, n):
    result = 0
    if m > 1 or n > 1:
        if m%2 != 0:
           result = round(m * (n/2))
        else:
           result = round(n * (m/2)) 
    return result
        
print(square(3,3))
#sol = Solution()
#print(sol.square(4,4))

