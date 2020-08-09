
def mergeSort(arr):

    if len(arr) > 1:
        mid = len(arr) // 2
        leftHalf = arr[:mid]
        rightHalf = arr[mid:]

        mergeSort(leftHalf)
        mergeSort(rightHalf)

        i = j = k = 0
        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] < rightHalf[j]:
                arr[k] = leftHalf[i]
                i += 1
            else:
                arr[k] = rightHalf[j]
                j += 1
            k +=1

        while i < len(leftHalf):
            arr[k] = leftHalf[i]
            k += 1
            i += 1

        while j < len(rightHalf):
            arr[k] = rightHalf[j]
            k += 1
            j += 1



arr = [3,4,5,6,1,3,6]
mergeSort(arr)