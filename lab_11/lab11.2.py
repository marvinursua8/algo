def merge(left, right):
    merged_list = []
    i = 0
    j = 0


    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged_list.append(left[i])
            i += 1
        elif left[i] > right[j]:
            merged_list.append(right[j])
            j += 1
        else: 
            merged_list.append(left[i])
            merged_list.append(right[j])
            i += 1
            j += 1

    merged_list.extend(left[i:])
    merged_list.extend(right[j:])
    
    return merged_list


print(merge([1,2,3], [1,2,6]))
print(merge([1, 2, 2, 7], [2, 4, 7]))
print(merge([], [2, 4, 6]))
print(merge([1, 3, 5], []))
print(merge([], []))