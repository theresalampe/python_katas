def count_bits_1(n):
    bit_string = ''
    while n != 0:
        bit_string = str(int(n % 2)) + bit_string
        n = int(n / 2)
    return bit_string.count('1')


def count_bits_2(n):
    return '{:b}'.format(n).count('1')


def count_bits_3(n):
    return sum(int(x) for x in bin(n)[2:])


def count_bits_4(n):
    return "{0:b}".format(n).count('1')


def count_bits_5(n):
    return bin(n)[2:].count('1')


def count_bits_6(n):
    return f'{n:b}'.count('1')


def count_bits_7(n):
    return sum(map(int, bin(n)[2:]))


def count_bits_8(n):
    return 0 if n == 0 else n % 2 + count_bits_8(n >> 1)


def count_bits(n):
    return bin(n).count("1")
