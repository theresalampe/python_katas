def find_outlier(integers):
    odd_numbers = list(filter(lambda x: x % 2 == 0, integers))
    even_numbers = list(filter(lambda x: x % 2 != 0, integers))
    return even_numbers[0] if len(odd_numbers) > 1 else odd_numbers[0]
