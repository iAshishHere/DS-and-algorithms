
def Partition(arr, start, end):
    pivot = arr[end]
    pIndex = start

    for i in range(start,end):
        if arr[i] <= pivot:
            temp = arr[i]
            arr[i] = arr[pIndex]
            arr[pIndex] = temp
            pIndex += 1
    temp = arr[end]
    arr[end] = arr[pIndex]
    arr[pIndex] = temp

    return pIndex


def QuickSort(arr, start, end):

    if (start < end):
        partitionIndex = Partition(arr, start, end)
        QuickSort(arr, start, partitionIndex-1)
        QuickSort(arr, partitionIndex + 1, end)



A = [8,2,4,100,1,9,2]
QuickSort(A,0, 6)
print(A)
