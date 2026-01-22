# compute disk usage for a given file system path recursively. Example of multiple recursion as we make recursive call for every path under a directory
import os


## os.path.getsize(path) to get size of a path which might be a file or dir
## os.path.isdir(path) whether given path is a directory or not
## os.listdir(path) list of strs containing all paths within the given dir path


def disk_usage(path: str) -> int:
    """Return the number of bytes used by file or folder and its descendants"""
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for filename in os.listdir(path):
            child_path = os.path.join(path, filename)
            total += disk_usage(child_path)

    print("{0:<7}".format(total), path)
    return total


if __name__ == "__main__":
    path = "/home/ragul/my_projects/dsa"
    total = disk_usage(path)
    print(f"Total disk usage for given {path}: {total}")
