def selection_sort(arr):
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        # Find the minimum element in the unsorted part
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr

input_str = input("Enter the numbers separated by spaces: ")
arr = list(map(int, input_str.split()))

sorted_arr = selection_sort(arr)

print("Sorted array:", sorted_arr)
