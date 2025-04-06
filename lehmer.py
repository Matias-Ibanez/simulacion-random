def lehmer_method(number_of_values,seed, number, k):
    numbers = []
    for _ in range(number_of_values):
        new_number = str(seed * number)
        k_digits = new_number[:k]
        subtraction = int(new_number[k:]) - int(k_digits)
        u = float("0." + str(subtraction))
        numbers.append(u)
        seed = subtraction
    return numbers

class Lehmer:
    def __init__(self,seed, number_of_values, number):
        self.seed = seed
        self.number = number
        self.number_of_values = number_of_values
        self.k = len(str(self.number))
        self.numbers = lehmer_method(self.number_of_values, self.seed, self.number, self.k)






