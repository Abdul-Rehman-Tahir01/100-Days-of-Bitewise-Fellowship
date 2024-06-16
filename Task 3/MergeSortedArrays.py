arr1 = [1, 3, 5]
arr2 = [2, 4, 6]
merged_array = []

# Merge the arrays
def merge_sorted_arrays(arr1, arr2):
    for i in range(len(arr1)):
        merged_array.append(arr1[i])
    for i in range(len(arr2)):
        merged_array.append(arr2[i])
    bubble_sort(merged_array)
    print(merged_array)

# Sort the arrays using bubble sort
def bubble_sort(merged_array):
    for i in range(len(merged_array)):
        for j in range(0, len(merged_array) - i - 1):
            if merged_array[j] > merged_array[j+1]:
                merged_array[j], merged_array[j+1] = merged_array[j+1], merged_array[j]



merge_sorted_arrays(arr1, arr2)