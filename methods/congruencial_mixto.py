from pickle import FROZENSET

from Tests.promedios import _Promedios
from Tests.frecuencia import _Frecuencia
from Tests.serie import _Serie

class _CongruencialMixto:
    @staticmethod
    def _new_seed(a, seed, c, m):
        return (a*seed + c) % m

    @staticmethod
    def mixed_congruent(seed, a, c, m, numbers_of_values):
        numbers = []
        for _ in range(numbers_of_values):
            new_seed = _CongruencialMixto._new_seed(a,seed,c,m)
            u = new_seed/m
            numbers.append(u)
            seed = new_seed
            #_Promedios.prueba_promedios(numbers)
        #_Frecuencia.prueba_frecuencia(numbers)
        _Serie.prueba_serie(numbers)

        return numbers
