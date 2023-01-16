# class Solution:
#     def theatreSquare(self , n, m, a)
#         width = m//a
#         if width < m/a:
#             width += 1
#         height = n//a
#         if height < n/a:
#             height += 1
#         result = width * height
#         print(result)

# sol = Solution()
# sol.theatreSquare(6,6,3)

# n,m,a = map(int, input().split())
# if m%a == 0:
#     v1 = m // a
# else:
#     v1 = m // a+1
# if n%a == 0:
#     v2 = n // a
# else:
#     v2 = n // a+1

# print(v1*v2)


n,m,a = map(int, input().split())
width = m//a
if width < m/a:
    width += 1
height = n//a
if height < n/a:
    height += 1
result = width * height
print(result)