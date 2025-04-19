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
        return numbers
