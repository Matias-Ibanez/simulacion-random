class _CongruencialMultiplicativo:
    @staticmethod
    def _new_seed(seed, a, m):
        return (seed*a) % m

    @staticmethod
    def multiplicative_congruential(seed, a, m, iterations ):
        numbers = []
        for _ in range(iterations):
            new_seed  = _CongruencialMultiplicativo._new_seed(seed, a, m)
            seed = new_seed
            u = int((new_seed / m) * 1000) / 1000
            numbers.append(u)
        return numbers