'''def insertion_sort(nums):
    for i in range(1,len(nums)):
        key = nums[i]
        j = i-1
        while j >=0 and  nums[j] > key:
            nums[j+1]=nums[j]
            j-=1
        nums[j+1]=key
    return nums

nums = [30,10,90,23,9,2]
print(insertion_sort(nums))'''
#inserting an element at correct position
def insert_into(arr,x):
    arr.append(0)
    i = len(arr) - 2
    while i >=0 and arr[i] > x:
        arr[i+1]=arr[i]
        i-=1
    arr[i+1] = x
    return arr

arr = [10,23,2,1,3,9]
x = int(input())
print(insert_into(arr,x)) 
 


