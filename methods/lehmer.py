class _Lehmer:
    @staticmethod
    def lehmer_method(seed,number, number_of_values):
        k = len(str(number))
        numbers = []
        for _ in range(number_of_values):
            new_number = str(seed * number)
            k_digits = new_number[:k]
            subtraction = int(new_number[k:]) - int(k_digits)
            u = float("0." + str(subtraction))
            numbers.append(u)
            seed = subtraction
        return numbers





