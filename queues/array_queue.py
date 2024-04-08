class Empty(Exception):
    """Error at attempting to access an element from an empty container."""

    pass


class ArrayQueue:
    """FIFO implementation of Array Queue with python list as underlying storage."""

    DEFAULT_CAPACITY = 10

    def __init__(self) -> None:
        """Create an empty Queue."""
        self._data = [
            None
        ] * ArrayQueue.DEFAULT_CAPACITY  # variable that holds the queue.
        self._size = 0  # variable that holds the current size of the queue.
        self._front = 0  # variable that holds the current index of the front of the queue.

    def __len__(self) -> int:
        """Return the size of the queue."""
        return self._size

    def is_empty(self) -> bool:
        """Returns if the queue is empty."""
        return self._size == 0

    def first(self):
        """
        Return the first element (but not remove) from the queue.
        Raise empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty("Queue is empty")
        return self._data[self._front]

    def dequeue(self):
        """
        Remove and return the first element of the queue.
        Raise empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty("Queue is empty")
        element = self._data[self._front]
        self._data[self._front] = None  # help garbage collection
        self._front = (self._front + 1) % len(self._data)
        self._size = self._size - 1
        if (
            0 < self._size < len(self._data) // 4
        ):  # if the queue's current size falls below 1/4th of total array capacity, reduce the array capacity by 1/2th
            self._resize(len(self._data) // 2)
        return element

    def enqueue(self, element):
        """
        Add a new element to the back of the queue.
        """
        if self._size == len(self._data):
            self._resize(2 * len(self._data))  # resize the list
        new_idx = (self._front + self._size) % len(self._data)
        self._data[new_idx] = element
        self._size = self._size + 1

    def _resize(self, cap):
        """
        Resize the list to a new capacity >= len(self._data)
        """
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(
            len(self._size)
        ):  # consider only elements in current queue
            self._data[k] = old[walk]  # essentially shifting
            walk = (walk + 1) % len(old)
        self._front = 0  # reset the front index


class ArrayDeque:
    """
    Deque implementation with python list as underlying storage.
    """

    DEFAULT_CAPACITY = 10

    def __init__(self) -> None:
        """Create an empty Deque."""
        self._data = [
            None
        ] * ArrayDeque.DEFAULT_CAPACITY  # variable to hold the python list
        self._size = 0  # variable to hold the current size of the queue
        self._front = 0  # variable to hold the current index position of the front of the queue.

    def __repr__(self):
        return str(self._data)

    def __str__(self):
        return str(self._data)

    def __len__(self) -> int:
        """Returns the size of the queue."""
        return self._size

    def is_empty(self):
        """Return whether the queue is empty."""
        return self._size == 0

    @property
    def first(self):
        """Return the first element (without deleting) of the queue."""
        if self.is_empty():
            raise Empty("Queue is empty.")
        return self._data[self._front]

    @property
    def last(self):
        """Return the last element (without deleting) of the queue."""
        if self.is_empty():
            raise Empty("Queue is empty.")
        idx = (self._front + self._size - 1) % len(self._data)
        return self._data[idx]

    def add_first(self, element):
        """Add new element to the start of the queue."""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))  # resize the list
        self._front = (self._front - 1) % len(self._data)
        self._data[self._front] = element
        self._size = self._size + 1

    def add_last(self, element):
        """Add new element to the end of the queue."""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))  # resize the list
        back = (self._front + self._size) % len(self._data)
        self._data[back] = element
        self._size = self._size + 1

    def delete_first(self):
        """Remove element from the beginning of the queue."""
        if self.is_empty():
            raise Empty("Queue is empty.")
        element = self._data[self._front]
        self._data[self._front] = (
            None  # for reducing reference counting and aiding in garbage collection
        )
        self._front = (self._front + 1) % len(self._data)
        self._size = self._size - 1
        if (
            0 < self._size < len(self._data) // 4
        ):  # if the queue's current size falls below 1/4th of total array capacity
            self._resize(len(self._data) // 2)
        return element

    def delete_last(self):
        """Remove element from the end of the queue."""
        idx = (self._front + self._size - 1) % len(self._data)
        element = self._data[idx]
        self._data[idx] = None
        self._size = self._size - 1
        return element

    def _resize(self, cap):
        """resize the python list to a new capacity > len(self._data)"""
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(len(self._size)):
            self._data[k] = old[walk]
            walk = (walk + 1) % len(old)
        self._front = 0  # reset the front index
