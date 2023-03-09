def arrayManipulation(n, queries):
    # Write your code here
    prefix = [0.0]*n
    for i in range(len(queries)):
        a,b,k = queries[i]
        print(a,b,k)
        prefix[a-1]+=k
        if b < len(prefix):
            prefix[b]-=k
    #print(prefix)
    for i in range(1,len(prefix)):
        prefix[i] = prefix[i-1] + prefix[i]
    return int(max(prefix))