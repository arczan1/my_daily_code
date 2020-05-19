class GeometricSequence:
    """
    Implementation of geometric sequence
    Formula of geometric sequence:
        an = a1 * r^(n-1)
        an - nth element of sequence
        a1 - first element
        r - common ratio

    You can get value of element using [] operator
    Example:
        seq = GeometricSequence(2, 3)
        seq[1] - first element
        seq[3] - third element
    """

    def __init__(self, first_element: float, common_ratio: float):
        self.first_element = first_element
        self.common_ratio = common_ratio

    def __getitem__(self, n: int) -> float:
        """Returns nth element of sequence(first index is 1 not 0!)"""

        # Wrong argument
        if not isinstance(n, int):
            raise TypeError("index must be integer")
        elif n < 1:
            raise IndexError("index must be greater or equeal  to 1")

        return self.first_element * (self.common_ratio ** (n - 1))

    def sum(self, n: int) -> float:
        """Return sum of the first n elements"""

        # Wrong argument
        if not isinstance(n, int):
            raise TypeError("n argument must be integer")
        elif n <= 0:
            return 0

        if self.common_ratio == 1:
            # Sum = a1 * n, for r == 1
            return self.first_element * n
        else:
            # Sum = a1 * ((1 - r^n) / (1 - r)), for r != 1
            return self.first_element * (
                    (1 - (self.common_ratio ** n)) / (1 - self.common_ratio))


if __name__ == "__main__":
    seq1 = GeometricSequence(3, 1)
    seq2 = GeometricSequence(1.5, -2)

    # Print first sequence
    for i in range(10):
        print("{} {}".format(seq1[i+1], seq1.sum(i+1)))
    # Print second sequence
    for i in range(10):
        print("{} {}".format(seq2[i+1], seq2.sum(i+1)))
