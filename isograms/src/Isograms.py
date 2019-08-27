def is_isogram(input):
    input = input.lower()
    for s in input:
        if len(''.join([c for c in input if c in s])) > 1:
            return False
    return True


def is_isogram_2(input):
    return len(input) == len(set(input.lower()))
