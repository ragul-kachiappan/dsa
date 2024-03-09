def bin_search(arr: list, x: int) -> int:
    low = 0
    high = len(arr) - 1
    occurence = len(arr)

    while low <= high:
        mid = (low + high) // 2
        if x == arr[mid]:
            occurence = mid if mid < occurence else occurence
            high = mid - 1
        elif x < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    if occurence < len(arr):
        return occurence
    else:
        return -1


def main():
    arr = [1, 10, 10, 10, 20, 20, 40]
    print(bin_search(arr, 10))


main()
