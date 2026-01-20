# Deleting from end of an array
def remove_end(arr, length):
    if length > 0:
        arr[length - 1] = 0  # or we could just create a sub-array with slicing


# Deleting from "i"th index
def remove_ith(arr, index, length):
    for i in range(index + 1, length):
        arr[i - 1] = arr[i]


# Insertion at the end
def insert_end(arr, n, length, capacity):
    if length < capacity:
        arr[length] = n


# Insertion at "i"th index
def insert_ith(arr, index, n, length):
    # shift elements to the right from end to index. To make space in index location
    for i in range(length - 1, index - 1, -1):
        arr[i + 1] = arr[i]
