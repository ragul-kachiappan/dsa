def unique1(s: list[int]) -> bool:
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                return False
    return True


def unique2(s: list[int]) -> bool:
    temp = sorted(s)
    for i in range(1, len(s)):
        if temp[i - 1] == temp[i]:
            return False
    return True


if __name__ == "__main__":
    s = [1, 2, 3, 4, 2]
    answer1 = unique1(s)
    print(f"Answer with unique1: {answer1}")

    answer2 = unique2(s)
    print(f"Answer with unique2: {answer2}")
