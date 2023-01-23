
n,m,a = map(int, input().split())
width = m//a
if width < m/a:
    width += 1
height = n//a
if height < n/a:
    height += 1
result = width * height
print(result)