def search_rotated(arr,target):
    l = 0
    r = len(arr)-1
    while l<=r:
        mid = (l+r)//2
        if arr[mid] == target:
            return mid
        if  arr[l] <= arr[r]:
            if arr[l] <= target < arr[mid]:
                r = mid - 1
            else:
                l = mid + 1
        else:
            if arr[mid] < target <= arr[r]:
                l = mid + 1
            else:
                r = mid - 1
    return -1

arr = [8,1,2,9,3]
target = 8
print(search_rotated(arr,target))