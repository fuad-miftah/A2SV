def insertionSort1(n, arr)
    newArr = []
    for i in range(n-1):
        for j in range(n-1, 1 , -1):
            if arr[j] < arr[j - 1]:
                temp = arr[j]
                arr[j] = arr[j - 1]
                print(arr)
                arr[j - 1] = temp
    print(arr)

arr = [2,4,6,8,3]
insertionSort1(5, arr)
