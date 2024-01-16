import ctypes

class DynamicArray:
    """A dynamic array class akin to a simplified python list."""

    def __init__(self):
        self._n = 0 # actual number of elements
        self._capacity = 1 # default array capacity
        self._A = self._make_array(self._capacity) # low-level array

    def __len__(self):
        """Return the number of elements stored in the array."""
        return self._n
    
    def __getitem__(self, k):
        """Return element at index K."""
        if not 0 <= k <= self._n:
            raise IndexError('Invalid index')
        return self._A[k]
    
    def append(self, obj):
        """Add object to the end of the array."""

        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1
    
    def _resize(self, c):
        """Resize internal array to capacity c."""
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c
    
    def _make_array(self, c):
        """Return a new array with capacity c."""
        return (c * ctypes.py_object)()
    
    def __str__(self):
        """Human readable representation of the array."""
        return "This is a dynamic array"