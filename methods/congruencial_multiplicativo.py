class _CongruencialMultiplicativo:
    @staticmethod
    def _new_seed(seed, a, m):
        return (seed*a) % m

    @staticmethod
    def multiplicative_congruential(seed, a, m, numbers_of_values ):
        numbers = []
        for _ in range(numbers_of_values):
            new_seed  = _CongruencialMultiplicativo._new_seed(seed, a, m)
            seed = new_seed
            u =float(f"{seed/m:.3f}")
            numbers.append(u)
        return numbers