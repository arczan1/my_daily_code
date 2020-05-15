from random import randint


def bubble_sort(array: list) -> None:
    """Sorts array using bubble sorting algorithm"""

    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j+1]:
                # Swap value of two elements
                array[j], array[j+1] = array[j+1], array[j]


if __name__ == "__main__":
    # Generate random array
    array = [randint(0, 9) for _ in range(20)]

    print("Array: ")
    for i in array:
        print("{} ".format(i), end='')

    bubble_sort(array)

    print("\nSorted array:")
    for i in array:
        print("{} ".format(i), end='')
    print("")
