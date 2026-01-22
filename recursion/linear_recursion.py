# Linear recursion indicate there's exactly one recursion call inside each invocation


#######################################################################################
# Sum of integers in a list
# can be devised as Sum of first n - 1 integers in the list plus the last element
def linear_sum(S: list[int], n):
    """Return the sum of first n numbers in the sequence"""
    if n == 0:
        return 0
    else:
        return linear_sum(S, n - 1) + S[n - 1]


#######################################################################################
# Reversing n elements of a sequence with recursion
# Kinda like 2 pointer approach, we swap first and last and iterate. At base case, either start == stop or start == stop - 1
def reverse(S: list[int], start, stop):
    if start < stop - 1:
        S[start], S[stop - 1] = S[stop - 1], S[start]
        reverse(S, start + 1, stop - 1)


#######################################################################################
# Computing power. Like pow(number, exp), O(n) time complexity
# solution 1: base n = 0 would produce 1, otherwise, its x * power(x, n-1)
def power1(x, n):
    """Compute the value of x**n with recursive approach"""
    if n == 0:
        return 1
    return x * power1(x, n - 1)


# solution 2: More optimal approach with squaring. O(log n) time complexity, saves in space complexity as well with reduced recursive depth at O(log n)
# power(x, n) = 1 for base case n = 0, power(x, n // 2) ^ 2 if n is even, x * power(x, n// 2) ^ 2 if n is odd
# It relies on the fact that once power(x, n // 2) is computed, we can resuse the result
def power2(x, n):
    if n == 0:
        return 1
    partial = power2(x, n // 2)
    result = partial * partial
    if n % 2 == 1:
        result *= x
    return result


if __name__ == "__main__":
    S = [1, 2, 3, 4, 5, 6]
    n = 4
    print(f"total: {linear_sum(S, n)}")
