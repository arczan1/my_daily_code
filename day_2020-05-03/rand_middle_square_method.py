# This script implements middle-square method of
# generating pseudorandom numbers


def get_generator(number_len: int, seed: int):
    '''
    This is generator that generates pseudorandom numbers using
    middle-square method

    Arguments:
        number_len - len of numbers to generate
        seed - seed used to randomize generated numbers(the len must
            equal to number_len)
    '''

    # All returned numbers should be saved because first time when returned
    # number repeats the generator will generate same numbers in loop
    returned_numbers = set()

    # When seed hits 0 all next numbers will be 0
    while seed != 0:
        # Square as string because it's easier to operate on string than int
        square_str = '{}'.format(seed*seed)
        if number_len >= len(square_str):
            seed = int(square_str)
        else:
            digits_to_cut = (len(square_str) - number_len) // 2
            # Cutting digits
            seed = int(square_str[digits_to_cut:digits_to_cut+number_len])

        if seed in returned_numbers:
            # The generator starts returning same numbers in loop
            break
        returned_numbers.add(seed)

        yield seed


if __name__ == '__main__':
    seed = 3849
    print('Seed used: {}'.format(seed))
    generator = get_generator(4, seed)
    for i in generator:
        print(i)
