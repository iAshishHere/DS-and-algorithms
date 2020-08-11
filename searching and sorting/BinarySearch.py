

def binarySearch(arr, start, end, element):
    if end >= start:
        mid = (end + start)  // 2

        if arr[mid] == element:
            return mid


        elif arr[mid] > element:
            return binarySearch(arr,start,mid-1,element)

        else:
            return binarySearch(arr,mid+1,end,element)

    else:
        return -1




arr = [1,2,3,4,5,6,7,8]

result = binarySearch(arr,0,len(arr)-1,9)
print(result)
