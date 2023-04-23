t = int(input())
for _ in range(t):
    num = int(input())
    count = bin(num).count("1")
    if count > 1:
        firstOne = ""
        while not num & 1:
            firstOne += "0"
            num >>= 1
        firstOne = "1" + firstOne
        print(int(firstOne,2))
            
    else:
        if num == 1:
            print(3)
        else:
            num += 1
            print(num)