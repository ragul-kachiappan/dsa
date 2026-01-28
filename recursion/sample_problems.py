import math


# 1. Find minimum and maximum vals in a list with recursion
def recursive_list(
    input_list: list[int], index: int, curr_min: int, curr_max: int
) -> tuple[int, int]:
    # base case
    if index == len(input_list):
        return (curr_min, curr_max)
    else:
        curr_min = min(curr_min, input_list[index])
        curr_max = max(curr_max, input_list[index])
        return recursive_list(input_list, index + 1, curr_min, curr_max)


# 2. Using recursion, compute integer part of base 2 logarithm of n using only addition and integer division
def find_log(n: int, log_val: int) -> int:
    # base condition
    if n // 2 == 0:
        return log_val
    else:
        log_val += 1
        return find_log(n // 2, log_val)


# 3. Product of two numbers with just addition and subtraction. Using recursion.
def prod_of_two(a: int, b: int, value: int) -> int:
    # base condition
    if b == 0:
        return value
    else:
        b -= 1
        value += a
        return prod_of_two(a, b, value)


# 4. is palindrome check with recursion
def is_palindrome(s: str, left_ptr: int, right_ptr: int) -> bool:
    # base condition
    if left_ptr >= right_ptr:
        return True
    elif s[left_ptr] != s[right_ptr]:
        return False
    else:
        return is_palindrome(s, left_ptr + 1, right_ptr - 1)


# 5. rearrange a sequence of numbers such that all evens appear before odds. Using recursion
def even_odd(numbers: list[int], left_ptr: int, right_ptr: int) -> list[int]:
    # base condition
    if left_ptr >= right_ptr:
        return numbers
    elif numbers[left_ptr] % 2 == 0:
        return even_odd(numbers, left_ptr + 1, right_ptr)
    elif numbers[right_ptr] % 2 != 0:
        return even_odd(numbers, left_ptr, right_ptr - 1)
    else:
        numbers[left_ptr], numbers[right_ptr] = numbers[right_ptr], numbers[left_ptr]
        return even_odd(numbers, left_ptr + 1, right_ptr - 1)


# 6. fibonacci series of given length
def base_fibonacci(length: int) -> list[int]:
    sequence: list[int] = []

    def fibonacci(n: int):
        if n <= 1:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

    for i in range(length):
        sequence.append(fibonacci(i))
    return sequence


if __name__ == "__main__":
    # 1. min and max vals
    input_list = [23, 53, 23, 32, 12, 93]
    min_max_tuple = recursive_list(input_list, 0, math.inf, -math.inf)
    print(f"minimum and maximum values are: {min_max_tuple}")

    # 2. integer part of base 2
    n = 512
    log_val = find_log(n, 0)
    print(f"Integer portion of log of {n} is {log_val}")

    # 3. product of 2 number with addition and subtraction
    a = 10
    b = 23
    prod = prod_of_two(a, b, 0)
    print(f"Product of {a} and {b} calculated only with add and subtract is {prod}")

    # 4. is palindrome check with recursion
    s = "malayalam"
    result = is_palindrome(s, left_ptr=0, right_ptr=len(s) - 1)
    print(f"The statement {s} is{' not' if not result else ''} palindrome")

    # 5. rearrange a sequence of numbers into even first and then odd
    numbers = [5, 2, 4, 1, 3, 5, 6, 8, 23]
    arranged_numbers = even_odd(numbers, left_ptr=0, right_ptr=len(numbers) - 1)
    print(f"rearrangement of {numbers} into even-odd sequence is {arranged_numbers}")

    # 6. fibonacci sequence for a given length
    length = 8
    fib_sequence = base_fibonacci(length)
    print(f"Fibonacci sequence for given {length=} is {fib_sequence}")
