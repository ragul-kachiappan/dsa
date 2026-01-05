def prefix_average1(s: list[int]) -> list[int]:
    n = len(s)
    a = [0] * n
    for j in range(n):
        total = 0
        for i in range(j + 1):
            total += s[i]
        a[j] = total / (j + 1)
    return a


def prefix_average2(s: list[int]) -> list[int]:
    n = len(s)
    a = [0] * n
    for i in range(n):
        a[i] = sum(s[0 : i + 1]) / (i + 1)
    return a


def prefix_average3(s: list[int]) -> list[int]:
    n = len(s)
    a = [0] * n
    total = 0
    for i in range(n):
        total += s[i]
        a[i] = total / (i + 1)
    return a


if __name__ == "__main__":
    s = [1, 2, 3, 4, 5]
    a1 = prefix_average1(s)
    a2 = prefix_average2(s)
    a3 = prefix_average3(s)

    print(f"Prefix average of {s} using prefix_average1 is {a1}")
    print(f"Prefix average of {s} using prefix_average2 is {a2}")
    print(f"Prefix average of {s} using prefix_average3 is {a3}")
