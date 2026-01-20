## move n - 1 disks from src to temp using dest (recursive)
## move remaining one bottom disk from src to dest (base)
## move n - 1 disks from temp to dest using src (recursive)


def move(n, src, dest, temp):
    if n >= 1:
        move(n - 1, src, temp, dest)
        print(f"Move {src} to {dest}")
        move(n - 1, temp, dest, src)


if __name__ == "__main__":
    src = 1
    temp = 2
    dest = 3
    num_disks = 3
    move(num_disks, src, dest, temp)
