from random import randint


def selection_sort(array: list) -> None:
    """Sorts array using selection sort algorithm"""

    for i in range(len(array)-1):
        min_index = i

        # Find index of min value
        for index, value in enumerate(array[i+1:]):
            if value < array[min_index]:
                # New min value
                min_index = index + (i + 1)

        # Swap values
        array[i], array[min_index] = array[min_index], array[i]


if __name__ == "__main__":
    # Generate random array
    array = [randint(0, 9) for _ in range(20)]

    print("Array: ")
    for i in array:
        print("{} ".format(i), end='')

    selection_sort(array)

    print("\nSorted array:")
    for i in array:
        print("{} ".format(i), end='')
    print("")
