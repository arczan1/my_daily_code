# This is the simplest algorithm that checks if a number is prime number,
# It tries to divide the number by each smaller natural number(except 1)

def is_prime(number: int) -> bool:
    if number <= 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


if __name__ == "__main__":
    print(f"39 {'is' if is_prime(39) else 'is not'} a prime number")
    print(f"17 {'is' if is_prime(17) else 'is not'} a prime number")
    print(f"1 {'is' if is_prime(1) else 'is not'} a prime number")
    print(f"2 {'is' if is_prime(2) else 'is not'} a prime number")
    print(f"-7 {'is' if is_prime(-7) else 'is not'} a prime number")
    print(f"7 {'is' if is_prime(7) else 'is not'} a prime number")
    print(f"37 {'is' if is_prime(37) else 'is not'} a prime number")
