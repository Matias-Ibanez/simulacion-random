class _CongruencialAditivo:
    @staticmethod
    def _new_seed(seed, last_seed, m):
        return (seed + last_seed) % m

    @staticmethod
    def addition_congruential(seed,m, seeds):
        numbers = []
        seeds.reverse()
        seeds.append(seed)
        cuantity_iteration = len(seeds) + 1
        last_index = len(seeds) - 1
        index_seed = 0

        for seed in seeds:
            last_seed = seeds[last_index]
            new_seed = _CongruencialAditivo._new_seed(seed, last_seed, m)
            seed = new_seed
            u = float(f"{seed / m:.3f}")
            numbers.append(u)
            seeds.append(seed)
            last_index += 1
            index_seed += 1
            if index_seed == cuantity_iteration:
                break
        return numbers



