class _CongruencialAditivo:
    @staticmethod
    def _new_seed(current_seed, last_seed, m):
        return (current_seed + last_seed) % m

    @staticmethod
    def addition_congruential(seed, m,  iterations, initial_seeds):
        """
            Genera una secuencia de números pseudoaleatorios.

            Parámetros:
                seed (int): Semilla adicional.
                m (int): Módulo.
                initial_seeds (list[int]): Lista de semillas iniciales.
                iterations (int): Cantidad de números a generar.

            Retorna:
                list[float]: Lista de números pseudoaleatorios.
            """

        numbers = []
        seeds = list(reversed(initial_seeds)) + [seed]

        for i in range(iterations):
            seed_current = seeds[i]
            seed_last = seeds[-1]
            new_seed = _CongruencialAditivo._new_seed(seed_current, seed_last, m)
            u = int((new_seed / m) * 1000) / 1000
            numbers.append(u)
            seeds.append(new_seed)

        return numbers



