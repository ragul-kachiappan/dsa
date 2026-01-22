# when function makes two recursive calls, it is binary recursion


# Summing n elements in list S with binary recursion
# We could design it as sum of (start + mid - 1) and (mid, stop - 1) and add these two together.
# reduction in space complexity at O(log n), but time complexity is still O(n) with 2n - 1 function calls
def binary_sum(S, start, stop):
    """Return the sum of numbers in implicit slice S[start:stop]"""
    if start >= stop:
        return 0
    elif start == stop - 1:
        return S[start]
    else:
        mid = (start + stop) // 2
        return binary_sum(S, start, mid) + binary_sum(S, mid, stop)
