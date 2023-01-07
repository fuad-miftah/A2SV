import math
def countSwaps(a)
    swapTimes = 0
    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j] > a[j + 1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapTimes = swapTimes + 1
    swapt = "Array is sorted in {} swaps" 
    firstElement = "First element : {}"
    lastElement = "Last element : {}"
    print(swapt.format(swapTimes))
    print(firstElement.format(a[0]))
    print(lastElement.format(len(a)))


a = [3 , 2, 1]
countSwaps(a)
