def fib_sequence(count: int) -> list:
    '''
    Return fibonacci sequence as list

    Parameters
    ----------
    count : int
        This is count of numbers in sequence
    '''
    if count < 1:
        return []
    elif count == 1:
        return [0]

    sequence = [0, 1]
    while len(sequence) < count:
        sequence.append(sequence[-2] + sequence[-1])

    return sequence


def fib_number(n: int) -> int:
    '''
    Return nth fibonacci number

    Parameters
    ----------
    n : int
        Index of number(Start at 1)
    '''
    if n <= 1:
        return 0

    a, b = 0, 1
    for _ in range(n-2):
        b, a = a + b, b

    return b


if __name__ == '__main__':
    print(fib_sequence(1))
    print(fib_sequence(-5))
    print(fib_sequence(3))
    print(fib_sequence(5))
    print(fib_sequence(10))

    print(fib_number(1))
    print(fib_number(-5))
    print(fib_number(3))
    print(fib_number(5))
    print(fib_number(10))
