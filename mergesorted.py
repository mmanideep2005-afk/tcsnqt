def merged_sorted(arr1,arr2):
    merged=[]
    i=0
    j=0
    while i < len(arr1) and j<len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i+=1
        else:
            merged.append(arr2[j])
            j+=1
    merged.extend(arr1[i:])
    merged.extend(arr2[j:])
    return merged
arr1 = [31,50,1]
arr2 = [40,30,9,7,2]
print(merged_sorted(arr1,arr2))
