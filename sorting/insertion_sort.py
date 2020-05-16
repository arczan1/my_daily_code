from random import randint


def insertion_sort(array: list) -> None:
    """Sorts array using insertion sort algorithm"""

    for index, value in enumerate(array):
        j = index

        # Move all greater values on place right
        while(j > 0 and value < array[j-1]):
            array[j] = array[j-1]
            j -= 1

        # Insert value
        array[j] = value


if __name__ == "__main__":
    # Generate random array
    array = [randint(0, 9) for _ in range(20)]

    print("Array: ")
    for i in array:
        print("{} ".format(i), end='')

    insertion_sort(array)

    print("\nSorted array:")
    for i in array:
        print("{} ".format(i), end='')
    print("")
