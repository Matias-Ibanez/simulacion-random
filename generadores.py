def square_method(seed, n, iteration):
    numbers = []
    for _ in range(iteration):
        x = str(pow(seed, 2))
        n_digits = len(x) - n
        if n_digits % 2 ==  0:
            start = n_digits // 2
            seed_str = x[start:start + n]
        else:
            correction = str(int(x)*10)
            n_digits = len(correction) - n
            start = n_digits // 2
            seed_str = x[start:start + n]

        seed = int(seed_str)
        u = float("0." + seed_str)
        numbers.append(u)

    return numbers

