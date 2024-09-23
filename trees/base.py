class Tree:
    """Abstract base class representing a tree structure."""

    # ----------------- nested Position class -------------------
    class Position:
        """An abstraction representing the location of a single element."""

        def element(self):
            """Return the element stored at the position."""
            raise NotImplementedError("must be implemented by subclass.")

        def __eq__(self, other: object) -> bool:
            """Return True if other position represents the same location."""
            raise NotImplementedError("must be implemented by subclass.")

        def __ne__(self, other: object) -> bool:
            """Return True if other does not represent the same location."""
            return not (self == other)

    # --------Abstract methods that concrete subclass should support.---------
    def root(self):
        """Return Position representing the Tree's root (None if empty)."""
        raise NotImplementedError("must be implemented by subclass.")

    def parent(self, p: Position):
        """Return Position representing p's parent (None if p is root.)"""
        raise NotImplementedError("must be implemented by subclass.")

    def num_children(self, p: Position):
        """Return the number of children that Position P has."""
        raise NotImplementedError("must be implemented by subclass.")

    def children(self, p: Position):
        """Generate an iteration of positions representing p's children."""
        raise NotImplementedError("must be implemented by subclass.")

    def __len__(self):
        """Return the total number of elements in the tree."""
        raise NotImplementedError("must be implemented by subclass.")

    # ----------Concrete methods implemented in this class--------------
    def is_root(self, p: Position) -> bool:
        """Return True if Position p represents the root of the tree."""
        return self.root() == p

    def is_leaf(self, p: Position) -> bool:
        """Return True if Position p does not have any children."""
        return self.num_children() == 0

    def is_empty(self) -> bool:
        """Return True if the tree is empty."""
        return len(self) == 0
