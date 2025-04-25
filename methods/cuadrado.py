from Tests.promedios import _Promedios
from Tests.frecuencia import _Frecuencia
from Tests.serie import _Serie

class _ParteCentralDelCuadrado:
    @staticmethod
    def _get_middle_values(n_digits, x, n):
        start = n_digits // 2
        return x[start:start + n]

    @staticmethod
    def square_method(seed, n, number_of_values):
        numbers = []
        for _ in range(number_of_values):
            x = str(pow(seed, 2))
            dif = len(x) - n
            if _ParteCentralDelCuadrado._is_even(dif):
                middle_numbers =  _ParteCentralDelCuadrado._get_middle_values(dif, x, n)
            else:
                correction = str(int(x) * 10)
                dif = len(correction) - n
                middle_numbers =  _ParteCentralDelCuadrado._get_middle_values(dif, x, n)
            seed = int(middle_numbers)
            u = float("0." + middle_numbers)
            numbers.append(u)

        return numbers

    @staticmethod
    def _is_even(number):
        return number % 2 == 0

