def binary_search(arr,target):
    right = len(arr)-1
    left = 0
    while left<=right:
        mid=(left+right)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid+1
        else:
            right = mid-1
    return -1

arr = [2,9,10,20,29]
target = int(input())
print(binary_search(arr,target))
