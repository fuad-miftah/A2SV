def superDigit(n, k):
    # Write your code here
    
    if len(n) == 1:
        return n
  
    s = 0
    for num in n:
        s+=int(num)
    n = str(s * k)
    return superDigit(n,1)