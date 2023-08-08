from typing import List, Union
class MyHash:
    def __init__(self, bucket: int) -> None:
        self.size = bucket
        self.hash_table = [[] for _ in range(self.size)]
    
    def __str__(self) -> List[List]:
        return f"{self.hash_table}"
    
    def insert(self, element) -> List[List]:
        hash = element % self.size
        self.hash_table[hash].append(element)
        return self.hash_table
    
    def delete(self, element) -> Union[List[List], bool]:
        hash = element % self.size
        if element in self.hash_table[hash]:
            self.hash_table[hash].remove(element)
            return self.hash_table
        else:
            return False
    
    def search(self, element) -> bool:
        hash = element % self.size
        if element in self.hash_table[hash]:
            return True
        else:
            return False


def main():
    h = MyHash(bucket=7)
    h.insert(70)
    h.insert(71)
    h.insert(9)
    h.insert(56)
    h.insert(72)

    print(h)

    h.delete(70)
    h.delete(70)

    print(h)

    print(h.search(56))

if __name__ == "__main__":
    main()
