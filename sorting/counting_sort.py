from random import randint


def counting_sort(array: list) -> None:
    """Sorts array using counting sort algorithm"""
    # If array is empty, don't do anything
    if len(array) <= 0:
        return

    max_value = max(array)
    min_value = min(array)

    # Create array to count values
    count = [0 for _ in range((max_value + 1) - min_value)]

    # Count values
    for i in array:
        count[i-min_value] += 1

    # Empty array
    array[:] = []
    # Fill array with sorted values
    for value, count in enumerate(count):
        array += [(value + min_value) for _ in range(count)]


if __name__ == "__main__":
    # Generate random array
    array = [randint(-2, 9) for _ in range(20)]

    print("Array: ")
    for i in array:
        print("{} ".format(i), end='')

    counting_sort(array)

    print("\nSorted array:")
    for i in array:
        print("{} ".format(i), end='')
    print("")
