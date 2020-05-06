def gcd(a: int, b: int) -> int:
    '''
    Greates common divisor of two integers(Euclidean algorithm)

    Parameters
    ----------
    a, b : int
        The algorithm will use abslute values
        Example: gcd(-3, 9) == gcd(3, 9)
    '''
    a, b = abs(a), abs(b)

    while b != 0:
        b, a = a % b, b
    return a


if __name__ == '__main__':
    print('GCD({}, {}) = {}'.format(9, 12, gcd(9, 12)))
    print('GCD({}, {}) = {}'.format(-3, 32, gcd(-3, 32)))
    print('GCD({}, {}) = {}'.format(14, 21, gcd(14, 21)))
    print('GCD({}, {}) = {}'.format(3, 0, gcd(3, 0)))
    print('GCD({}, {}) = {}'.format(0, 0, gcd(0, 0)))
