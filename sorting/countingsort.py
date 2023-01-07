def countingSort(arr)
    freqArr = []
    for i in range(100):
        freqArr.append(0)
    print(len(freqArr))

    for i in range(len(arr)):
        freqArr[arr[i]] = freqArr[arr[i]] + 1
    print(freqArr)





arr = [1,1,3,2,1,0,0,44,5,99]
countingSort(arr)
