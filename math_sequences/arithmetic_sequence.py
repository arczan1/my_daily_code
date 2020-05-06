class ArithmeticSequence:
    """
    Implementation of arithmetic sequence
    Formula of arithmetic sequence:
        an = a1 + (n - 1) * r
        an - nth element of sequence
        a1 - first element
        r - diffrence(diff)

    You can get value of element using [] operator
    Example:
        seq = ArithmeticSequence(2, 3)
        seq[1] - first element
        seq[3] - third element
    """

    def __init__(self, first_element: float, diff: float):
        self.first_element = first_element
        self.diff = diff

    def __getitem__(self, n: int) -> float:
        """Returns nth element of sequence(first index is 1 not 0!)"""

        # Wrong argument
        if not isinstance(n, int):
            raise TypeError("index must be integer")
        elif n < 1:
            raise IndexError("index must be greater or equeal  to 1")

        return self.first_element + self.diff * (n - 1)

    def sum(self, n: int) -> float:
        """Return sum of the first n elements"""

        # Wrong argument
        if not isinstance(n, int):
            raise TypeError("n argument must be integer")
        elif n <= 0:
            return 0

        # Sum = ((2*a1) + (n-1) * r) * (n / 2)
        return ((2 * self.first_element) + (n - 1) * self.diff) * (n / 2)


if __name__ == "__main__":
    seq1 = ArithmeticSequence(1, 2)
    seq2 = ArithmeticSequence(3, -2)

    # Print first sequence
    for i in range(10):
        print("{} ".format(seq1[i+1]))
    print("Sum: {}".format(seq1.sum(10)))
    # Print second sequence
    for i in range(10):
        print("{} ".format(seq2[i+1]))
    print("Sum: {}".format(seq2.sum(10)))
