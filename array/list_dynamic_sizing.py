import sys


data = []
n = 10

for _ in range(n):
    a = len(data)
    b = sys.getsizeof(data)
    print(f"Length: {a:3d}; Size in bytes: {b:4d}")
    data.append(None)
