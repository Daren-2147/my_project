def selection_sort(arr):
    n = len(arr)
    for k in range(n):
        min_idx = 0
        for i in range(n):
            if arr[min_idx]>arr[i]:
                min_idx = i
        arr[k] = arr[min_idx]
    return arr
print(selection_sort([1,5,4,2,7,6,5,9,10,11,15,24,26]))