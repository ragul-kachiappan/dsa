# print this pattern for a given n:
# example: n=5
# pattern:
# 12345 12345
# 1234   2345
# 123     345
# 12       45
# 1         5
import argparse


def row_pattern(n: int, row: int) -> str:
    lspace = n - row + 1
    rspace = n + row + 1
    pattern = []
    for i in range(1, 2 * n + 2):
        if lspace <= i <= rspace:
            pattern.append(" ")
        elif i > rspace:
            pattern.append(str(i - n - 1))
        else:
            pattern.append(str(i))
    return "".join(pattern)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Define input argument for n")
    parser.add_argument("number", type=int, help="input number between 1 to 9")
    args = parser.parse_args()
    number = args.number
    if not 1 <= number <= 9:
        raise Exception("Enter a number between 1 to 9")
    for i in range(number):
        pattern = row_pattern(n=number, row=i)
        print(pattern)
