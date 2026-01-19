def binary_search(data: list[int], target: int, low: int, high: int) -> bool:
    if low > high:
        return False
    else:
        mid = (high + low) // 2
        if target == data[mid]:
            return True
        elif target > data[mid]:
            low = mid + 1
            return binary_search(data, target, low, high)
        else:
            high = mid - 1
            return binary_search(data, target, low, high)


if __name__ == "__main__":
    data: list[int] = [23, 34, 46, 64, 88, 99, 101, 105]
    target: int = 45
    result = binary_search(data, target, 0, len(data) - 1)
    print(f"result: {result}")
