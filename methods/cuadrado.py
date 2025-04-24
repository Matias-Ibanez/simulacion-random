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
        #_Frecuencia.prueba_frecuencia(muestra)
        muestra = [
            0.129, 0.564, 0.723, 0.198, 0.317, 0.673,
            0.644, 0.297, 0.535, 0.248, 0.426, 0.960,
            0.713, 0.050, 0.990, 0.960, 0.594, 0.495,
            0.079, 0.455, 0.683, 0.366, 0.287, 0.050
        ]
        _Serie.prueba_serie(muestra)

        return numbers

    @staticmethod
    def _is_even(number):
        return number % 2 == 0

