def get_middle_values(n_digits, x, n):
    start = n_digits // 2
    return x[start:start + n]


def square_method(seed, n, number_of_values):
    numbers = []
    for _ in range(number_of_values):
        x = str(pow(seed, 2))
        dif = len(x) - n
        if is_even(dif):
            middle_numbers = get_middle_values(dif,x,n)
        else:
            correction = str(int(x)*10)
            dif = len(correction) - n
            middle_numbers = get_middle_values(dif, x, n)
        seed = int(middle_numbers)
        u = float("0." + middle_numbers)
        numbers.append(u)
    return numbers

def is_even(number):
    return number % 2 == 0

class ParteCentralDelCuadrado:
    def __init__(self,seed,n,number_of_values):
        self.n = n
        self.number_of_values = number_of_values
        self.seed = seed
        self.numbers = square_method(seed, n, number_of_values)

